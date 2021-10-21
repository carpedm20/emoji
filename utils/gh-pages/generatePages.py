"""Generate the files index.html and all.html that will contain a table of all supported emoji
Run with -minify to minify HTML for production"""

import sys
import os
import codecs
import django.conf
import django.template
from htmlmin.minify import html_minify

try:
    import emoji
except ImportError:
    include = os.path.relpath(os.path.join(os.path.dirname(__file__), "../.."))
    sys.path.insert(0, include)
    import emoji
    print("Imported emoji from %s" %
          os.path.abspath(os.path.join(include, "emoji")))

# Configuration
OUT_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_FILE = os.path.join(TEMPLATE_DIR, "template.html")
data = {"defaultListName": 'UNICODE_EMOJI_ENGLISH'}

languages = {
    "EMOJI_UNICODE_ENGLISH": emoji.emojize(":United_Kingdom:"),
    "EMOJI_ALIAS_UNICODE_ENGLISH": emoji.emojize(":United_Kingdom:alias"),
    "EMOJI_UNICODE_SPANISH": emoji.emojize(":Spain:"),
    "EMOJI_UNICODE_PORTUGUESE": emoji.emojize(":Portugal:"),
    "EMOJI_UNICODE_ITALIAN": emoji.emojize(":Italy:"),
    "EMOJI_UNICODE_FRENCH": emoji.emojize(":France:"),
    "EMOJI_UNICODE_GERMAN": emoji.emojize(":Germany:")
}
language_args = {
    "EMOJI_ALIAS_UNICODE_ENGLISH": 'language="en", use_aliases=True'
}


minify_enabled = sys.argv[-1] == '-minify'
if not minify_enabled:
    print("Run with -minify to minify HTML")


print("Collecting emoji data...")
for code, unicode_emojis in emoji.UNICODE_EMOJI.items():
    for var_name in emoji.__all__:
        if var_name == data["defaultListName"]:
            language_args[var_name] = ""
        elif unicode_emojis == getattr(emoji, var_name):
            language_args[var_name] = f'language="{code}"'
            break

data["lists"] = lists = []
for var_name in emoji.__all__:
    if not var_name.startswith(("EMOJI_UNICODE_", "EMOJI_ALIAS_UNICODE_")):
        continue

    var_name_pretty = languages[var_name] if var_name in languages else var_name
    language_arg = language_args[var_name] if var_name in language_args else "[TODO]"

    emoji_list = []
    for name, code in getattr(emoji, var_name).items():
        emoji_list.append({
            "code": code,
            "name": name,
            "unicode": code.encode('ascii', 'backslashreplace').decode('ascii'),
            "charname": code.encode('ascii', 'namereplace').decode('ascii'),
            "xml": code.encode('ascii', 'xmlcharrefreplace').decode('ascii')
        })

    listentry = {
        "name": var_name,
        "pretty": var_name_pretty,
        "languageArg": language_arg,
        "emojis": emoji_list
    }
    lists.append(listentry)


# Render with django
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
    }
]

django.conf.settings.configure(TEMPLATES=TEMPLATES)
django.setup()
template = django.template.loader.get_template(TEMPLATE_FILE)

print("Render 'all.html' ...")
with codecs.open(os.path.join(OUT_DIR, "all.html"), "w", encoding="utf-8") as f:
    html = template.render(data)
    if minify_enabled:
        print("Minify 'all.html' ...")
        html = html_minify(html)
    f.write(html)
    print(f"Wrote to {os.path.join(OUT_DIR, 'all.html')}")

print("Render 'index.html' ...")
# Remove emoji except for default list
for listentry in lists:
    if listentry["name"] != data["defaultListName"]:
        listentry["emojis"] = []

with codecs.open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as f:
    html = template.render(data)
    if minify_enabled:
        print("Minify 'index.html' ...")
        html = html_minify(html)
    f.write(html)
    print(f"Wrote to {os.path.join(OUT_DIR, 'index.html')}")

print("Done.")
