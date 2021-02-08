# -*- coding: utf-8 -*-

"""
Download emoji.json from https://github.com/iamcal/emoji-data and find missing shortcodes
"""

import emoji
import requests

WARN_DIFFERENT = True
LIST_MISSING = True
COMMENTS = False
SUMMARY = True

def extract_emoji_data(url) -> dict:
    count=0
    output = {}
    response = requests.get(url)
    response.raise_for_status()
    emoji_data = response.json()
    count = 0
    short_names = {}
    for e in emoji_data:
        code = e['unified'].split('-')
        code = [f'\\U{int(x,16):0>8X}' for x in code]
        code = "".join(code).encode().decode('unicode-escape')
        if len(code) == 2:
            code = code.rstrip('\uFE0F')

        if code in short_names:
            print(f"Duplicate emoji! {code}")
            sys.exit(1)

        short_names[code] = [f":{n}:" for n in e['short_names']]

    return short_names


if __name__ == '__main__':
    emoji_data_url = 'https://raw.githubusercontent.com/iamcal/emoji-data/master/emoji_pretty.json'
    emoji_data = extract_emoji_data(emoji_data_url)

    different = {}
    variant ={} 
    missing_emoji = {}
    missing_alias = {}
    matched = 0 

    remove_variant = { ord('\uFE0F'): None }
    for code, names in emoji_data.items():
        matched_name = ''
        for name in names:
            if name in emoji.EMOJI_ALIAS_UNICODE_ENGLISH:
                if emoji.EMOJI_ALIAS_UNICODE_ENGLISH[name] == code:
                    # Exact match, just count it
                    matched += 1
                elif emoji.EMOJI_ALIAS_UNICODE_ENGLISH[name].translate(remove_variant) == code.translate(remove_variant):
                    # Name matches, unicode matches if we ignore variants
                    variant[name] = code
                else:
                    # Name found, but unicode is different
                    different[name] = code
            else:
                if code in emoji.UNICODE_EMOJI_ENGLISH:
                    # Name not found, but unicode is an exact match, it's a definite missing alias
                    missing_alias[name] = code
                else:
                    found = False
                    for c, e in emoji.UNICODE_EMOJI_ENGLISH.items():
                        if c.translate(remove_variant) == code.translate(remove_variant):
                            # Found a unicode match ignoring variants, missing alias
                            missing_alias[name] = c
                            found = True
                            break
                    if not found:
                        # Didn't find name or unicode, it's a complete unknown
                        missing_emoji[name] = code

    if LIST_MISSING:
        if missing_alias:
            print("\nMissing Alias:")
            for n,c in sorted(missing_alias.items()):
                line = f"    u'{n}': u'{c.encode('unicode-escape').decode()}',"
                if COMMENTS:
                    line = f"{line:<48} # {emoji.demojize(c)} "
                    line = f"{line:<72} {c}"
                print(line)

        if missing_emoji:
            print("\nMissing Emoji:")
            for n,c in sorted(missing_emoji.items()):
                line = f"    u'{n}': u'{c.encode('unicode-escape').decode()}',"
                if COMMENTS:
                    line = f"{line:<48} # {emoji.demojize(c)} "
                    line = f"{line:<72} {c}"
                print(line)

    if WARN_DIFFERENT:
        if variant:
            print("\nName found, different variant:")
            for n,c in sorted(variant.items()):
                print(f"  {n:>30} {c.encode('unicode-escape')} {c} ~= {emoji.EMOJI_ALIAS_UNICODE_ENGLISH[n]} {emoji.EMOJI_ALIAS_UNICODE_ENGLISH[n].encode('unicode-escape')}")

        if different:
            print("\nName found, different unicode:")
            for n,c in sorted(different.items()):
                print(f"  {n:>30} {c.encode('unicode-escape')} {c} != {emoji.EMOJI_ALIAS_UNICODE_ENGLISH[n]} {emoji.EMOJI_ALIAS_UNICODE_ENGLISH[n].encode('unicode-escape')}")

    if SUMMARY:
        print('\nSummary:')
        print('  Name and unicode matched: ', matched)
        print('  Name present but variant differs: ', len(variant))
        print('  Name present but unicode differs: ', len(different))
        print('  Unicode found but missing alias: ', len(missing_alias))
        print('  Missing name and no matching unicode: ', len(missing_emoji))
        print(f"  Total: {len(emoji_data)} emoji with {sum([len(n) for c,n in emoji_data.items()])} names\n")

