# -*- coding: utf-8 -*-

"""
Extract the full list of emoji and names from the Unicode Consortium and
apply as much formatting as possible so the codes can be dropped into the
emoji registry file.

Written and run with Python3.  Not tested on Python2 and definitely not
intended for production use.
"""

import requests
from bs4 import BeautifulSoup


def extract_emojis(url) -> dict:
    output = {}
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    names = [n.text for n in table.find_all(attrs={"class": "name"})]
    codes = [c.text for c in table.find_all(attrs={"class": "code"})]
    for name, code in zip(names, codes):
        """
        replace semi-colons, commas, open smart quote, close smart quote,
        and asterisk (⊛) symbol used to denote newly added emojis,
        replace spaces after trimming for the asterisk case
        """
        name = name.removeprefix('flag: ')\
                   .replace(':', '') \
                   .replace(',', '') \
                   .replace(u'\u201c', '') \
                   .replace(u'\u201d', '') \
                   .replace(u'\u229b', '') \
                   .strip() \
                   .replace(' ', '_')

        _code = []
        for c in code.split(' '):
            if len(c) == 6:
                _code.append(c.replace('U+', '\\U0000'))
            else:
                _code.append(c.replace('U+', '\\U000'))
            code = ''.join(_code)
        output[name] = code
    return output


if __name__ == '__main__':
    emoji_url = 'http://www.unicode.org/emoji/charts/full-emoji-list.html'
    emoji_modifiers_url = 'http://www.unicode.org/emoji/charts/full-emoji-modifiers.html'

    emojis = extract_emojis(emoji_url)
    emoji_modifiers = extract_emojis(emoji_modifiers_url)
    total = emojis | emoji_modifiers

    for emoji_name, emoji_code in sorted(total.items()):
        print(f"    u':{emoji_name}:': u'{emoji_code}'", end=',\n')
    print('\nTotal count of emojis: ', len(total))
