## Documentation at https://carpedm20.github.io/emoji/docs/

| **Module contents**                                                                           |                                                              |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| [`emojize()`](https://carpedm20.github.io/emoji/docs/#emoji.emojize)                          | Replace emoji names in with Unicode codes                    |
| [`demojize()`](https://carpedm20.github.io/emoji/docs/#emoji.demojize)                        | Replace Unicode emoji with emoji shortcodes                  |
| [`replace_emoji()`](https://carpedm20.github.io/emoji/docs/#emoji.replace_emoji)              | Replace Unicode emoji with a customizable string             |
| [`emoji_list()`](https://carpedm20.github.io/emoji/docs/#emoji.emoji_list)                    | Location of all emoji in a string                            |
| [`distinct_emoji_list()`](https://carpedm20.github.io/emoji/docs/#emoji.distinct_emoji_list)  | Distinct list of emojis in the string                        |
| [`emoji_count()`](https://carpedm20.github.io/emoji/docs/#emoji.emoji_count)                  | Number of emojis in a string                                 |
| [`is_emoji()`](https://carpedm20.github.io/emoji/docs/#emoji.is_emoji)                        | Check if a string/character is an emoji                      |
| [`version()`](https://carpedm20.github.io/emoji/docs/#emoji.version)                          | Unicode/Emoji version of an emoji                            |
| [`EMOJI_DATA`](https://carpedm20.github.io/emoji/docs/#emoji.EMOJI_DATA)                      | Dict of all emoji                                            |
| [`STATUS`](https://carpedm20.github.io/emoji/docs/#emoji.STATUS)                              | Dict of Unicode/Emoji status                                 |


Building the documentation with [Sphinx](https://www.sphinx-doc.org/):

```bash
git clone https://github.com/carpedm20/emoji.git
cd emoji/docs
python -m pip install -r requirements.txt
make html
```

Check for warnings:

```bash
make clean
sphinx-build -n -T -b html . _build
```

Test code in code blocks:

```bash
make doctest
```

Test coverage of documentation:

```bash
make coverage
```
