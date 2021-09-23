# -*- coding: utf-8 -*-

"""
Extract the full list of emoji and names from the Unicode emoji data files
https://unicode.org/Public/emoji/{v}/emoji-test.txt
and apply as much formatting as possible so the codes can be dropped into the
emoji registry file.
"""

import requests


def get_source_from_url(version: float) -> list:
    """Get splitlines of emojis list from unicode.org"""

    url = f"https://unicode.org/Public/emoji/{version}/emoji-test.txt"
    source = requests.get(url)
    return source.text.splitlines()


def extract_emojis(emojis_lines: list) -> dict:
    """Extract emojis line by line to dict"""

    output = {}
    for line in emojis_lines:
        if not line == "" and not line.startswith("#"):
            emoji_status = line.split(";")[1].strip().split(" ")[0]
            codes = line.split(";")[0].strip().split(" ")
            if emoji_status == "fully-qualified":
                separated_name = line.split("   #")[-1].strip().split(" ")[2:]
                emoji_name = (
                    "_".join(separated_name)
                    .removeprefix("flag:_")
                    .replace(":", "")
                    .replace(",", "")
                    .replace("\u201c", "")
                    .replace("\u201d", "")
                    .replace("\u229b", "")
                    .strip()
                    .replace(" ", "_")
                )

                emoji_code = "".join(
                    [
                        "\\U0000" + code if len(code) == 4 else "\\U000" + code
                        for code in codes
                    ]
                )
                output[emoji_name] = emoji_code
    return output


if __name__ == "__main__":
    emoji_source = get_source_from_url(14.0)
    emojis = extract_emojis(emoji_source)

    for name, code in emojis.items():
        print(f"    u':{name}:': u'{code}'", end=",\n")
    print("\nTotal count of emojis: ", len(emojis))
