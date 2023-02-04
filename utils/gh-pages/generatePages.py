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
data = {"defaultLang": "en"}

languages = {
    "en": emoji.emojize("en :United_Kingdom:"),
    "alias":  emoji.emojize("alias :United_Kingdom:"),
    "es": emoji.emojize("es :Spain:"),
    "pt": emoji.emojize("pt :Portugal:"),
    "it": emoji.emojize("it :Italy:"),
    "fr": emoji.emojize("fr :France:"),
    "de": emoji.emojize("de :Germany:"),
    "fa": emoji.emojize("fa :Iran:"),
    "id": emoji.emojize("id :Indonesia:"),
    "zh": emoji.emojize("zh :China:"),
}
language_args = {}


minify_enabled = sys.argv[-1] == '-minify'
if not minify_enabled:
    print("Run with -minify to minify HTML")


print("Collecting emoji data...")

data["lists"] = lists = []
for language in languages:

    if language in language_args:
        language_arg = language_args[language]
    elif language == data["defaultLang"]:
        language_arg = ''
    else:
        language_arg = f'language="{language}"'

    emoji_list = []
    for code, emoji_data in emoji.EMOJI_DATA.items():
        if language not in emoji_data:
            continue
        names = [emoji_data[language]] if isinstance(emoji_data[language], str) else emoji_data[language]
        for name in names:
            emoji_list.append({
                "code": code,
                "name": name,
                "unicode": code.encode('ascii', 'backslashreplace').decode('ascii'),
                "charname": code.encode('ascii', 'namereplace').decode('ascii'),
                "xml": code.encode('ascii', 'xmlcharrefreplace').decode('ascii')
            })

    listentry = {
        "name": language,
        "pretty": languages[language],
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
    if listentry["name"] != data["defaultLang"]:
        listentry["emojis"] = []

with codecs.open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as f:
    html = template.render(data)
    if minify_enabled:
        print("Minify 'index.html' ...")
        html = html_minify(html)
    f.write(html)
    print(f"Wrote to {os.path.join(OUT_DIR, 'index.html')}")

print("Done.")
