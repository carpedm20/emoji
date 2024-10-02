# Adding a new language

## Unicode repository

Find out if the language exists in the Unicode repository:
https://github.com/unicode-org/cldr/tree/main/common/annotations

If the language exists, open the `{language-code}.xml` file and check if there are actually translations for emoji.
We use the entries that have the attribute `type="tts"` because they only contain one translation, so we don't have
to decide which translation to use.
For example for Spanish, we can look at [`es.xml`](https://github.com/unicode-org/cldr/blob/main/common/annotations/es.xml).
Let's look at the entries for 😼:

```xml
<annotation cp="😼">cara | gato | gato haciendo una mueca | irónico | sonrisa</annotation>
<annotation cp="😼" type="tts">gato haciendo una mueca</annotation>
```

We use the second one with the `type="tts"`. This would result in the emoji name `:gato_haciendo_una_mueca:`


## Emojiterra

The data on https://emojiterra.com/ is also sourced from the unicode repository and very similar. Most notably the
countries/flags are included on emojiterra but no in the Unicode repository (they are located in a different file
on the Unicode respository).

We use the URL of the "Copy and Paste"-section to extract the data. Go to https://emojiterra.com/keyboard/ and
then select the language from the dropdown menu.
Note that the URL is sometimes localized. For example the Spanish url is `https://emojiterra.com/es/teclado/` but
the Turkish url is `https://emojiterra.com/keyboard/tr/`


## Generate JSON files

To generate all the emoji sequences, English names and aliases automatically from all the data, we use
[`utils/generate_emoji.py`](generate_emoji.py)

To update to a newer Unicode version, change the parameters of these lines:

```python
   emoji_source = get_emoji_from_url(16.0)
    emoji_sequences_source = get_emoji_variation_sequence_from_url('16.0.0')
```

The translations are generated with the script [`utils/generate_emoji_translations.py`](generate_emoji_translations.py)

Open the script and add the two-letter code of the language to the dict `languages = {`. For example, we can add `es`:

```python
languages = {
    'es': extract_names(get_language_data_from_url(github_tag, 'es'), 'es', get_emojiterra_from_url('https://emojiterra.com/es/copiar/')),
}
```

If you run the script, the JSON files in the directory `emoji/unicode_codes/` are replaced with the new files.

```sh
python -m pip install -r requirements.txt
python utils/generate_emoji.py
python utils/generate_emoji_translations.py
```

If you have added a new language you need to add the language to the `LANGUAGES` variable in [`emoji/unicode_codes/data_dict.py`](../emoji/unicode_codes/data_dict.py).

You can also add the new langauge to the `languages` dict in [`utils/gh-pages/generatePages.py`](gh-pages/generatePages.py#L26-L35).

## Test the new data

The final step is to run the tests to check that everything works as it should:

```sh
pytest

```

If the tests fail, the first step can be to run the test `test_emojize_name_only` alone to see if the regular expression
`emoji.core._EMOJI_NAME_PATTERN` contains all the necessary characters:

```sh
pytest -k test_emojize_name_only

```

If this test fails, it will print the character that is missing e.g.

```text
Regular expression is missing a character:
'،' ('\u0327') is not in the regular expression
```

It means that one of the emoji names contains the character `\u0327` but that character is not matched by `emoji.core._EMOJI_NAME_PATTERN`.
Instead of the character itself, it could also be another possible unicode form of the same letter.
Some letters (usually the ones with a diacritic) can be described in different forms in Unicode. There are at most four possible forms.
For example the `ç` in `:Curaçao:` has two different Unicode forms that we need to be able to find with our regular expression pattern:

```python
name = ':Curaçao:'
unicodedata.normalize('NFKC', name)  # ':Cura\\xe7ao:'
unicodedata.normalize('NFC', name)   # ':Cura\\xe7ao:'
unicodedata.normalize('NFKD', name)  # ':Curac\\u0327ao:'
unicodedata.normalize('NFD', name)   # ':Curac\\u0327ao:'
```

To solve this, you can strip/replace the offending character from the emoji name by changing the `adapt_emoji_name()` in `generateutils.py`.
There are already special cases for some languages.

You could also change the entries in the JSON file by hand if it is only a few special cases.

If you think the character should be kept in the name, then you have to add the character (and possibly the other Unicode forms of it)
to the regular expression `emoji.core._EMOJI_NAME_PATTERN`.
