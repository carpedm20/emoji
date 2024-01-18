emoji
=====

v2.10.0 (2024-01-18)
-----
* Added Arabic and Turkish translations

v2.9.0 (2023-12-05)
-----
* Added Russian translation

v2.8.0 (2023-08-16)
-----
* Update translations to unicode release-43-1
* Include "derived annotations"-translations from unicode CLDR
* Fix translations for emoji that have multiple forms with/out \uFE0F (Fixes Partially missing languages #272 )
* Remove multiple underscore __,  ___, ____ and _-_ from translations

v2.7.0 (2023-07-25)
-----
* Extract aliases from cheat sheet and youtube
* Fix extracting translations from emojiterra
* Update EMOJI_DATA with new aliases and translations

v2.6.0 (2023-06-28)
-----
* Added new function purely_emoji() | Check if a string contains only emojis

v2.5.1 (2023-06-15)
-----
* Fix Malformed zero width joiner (\u200d) causes IndexError

v2.5.0 (2023-06-08)
-----
* Added support for Multi-person skintones
* Removed support for Python 2, 3.4, 3.5
* The logic from demojize() is moved to two separate private function tokenize() and filter_tokens() in a new file emoji/tokenizer.py
* A new public function analyze() is available and that supports the multi-person skintones

v2.4.0 (2023-03-12)
-----
* Added Japanese and Korean

v2.3.0 (2023-02-04)
-----
* Added Indonesian and Simplified Chinese
* Bug fixing

v2.2.0 (2022-10-31)
-----
* Added support for Unicode Version 15
* Added more translations for existing languages: (similar to the Turkish Language)
* Added Readme on how to add a language
* Fix 2.0.0: sphinx warnings reference target not found

v2.1.0 (2022-09-17)
-----
* Added Farsi support
* Added Trove classifiers for Python 3.10 and 3.11

v2.0.0 (2022-06-30)
-----
* Removed the old dicts EMOJI_UNICODE_*, UNICODE_EMOJI_*
* Removed unused language=None parameters
* Removed use_alias parameter
* Removed the get_regexp method
* Removed emoji_lis
* Removed distinct_emoji_lis
* Made the list of languages public: emoji.LANGUAGES = ['en','es','pt','it','fr','de']
* Updated translations to release-41 (no changes compared to release-40)
* Generate documentation for the public functions from the docstrings with Sphinx
* Added some more examples to the README: e.g. how to replace/remove emojis
* Total count of emojis:  4702

v1.7.0 (2022-03-07)
-----
* Added `emoji_list()` and `distinct_emoji_list()`
* Added deprecation warnings for several functions and variables that will be removed in version 2.0.0.
  If you don't want to see these warnings, you can stay with 1.6.x. For example, in pip/requirements.txt you can pin to 1.6.x with `emoji~=1.6.3`.

v1.6.3 (2022-01-15)
-----
* Added support for counting unique emojis

v1.6.2 (2021-12-06)
-----
* Improve performance of demojize()
* Added more tests
* Added warning when someone uses any other language than 'en' with use_aliases=True in emojize()

v1.6.1 (2021-10-13)
-----
* Allow multiple aliases
* Restored aliases from 1.5.0

v1.6.0 (2021-10-04)
-----
* Fix Unicode of some emoji in the language files
* is_emoji function added
* Added dict of dict with emoji data include emoji versions and statuses
* emoji.version(string) method added
* Included 'variant' in the dict of dicts

v1.5.2 (2021-09-25)
-----
* is_emoji function added

v1.5.1 (2021-09-25)
-----
* Fix Unicode of some emoji in the language files

v1.5.0 (2021-09-17)
-----
* Emojis of English version updated to the Emoji Charts v14.0
* Current count of emojis - 3633
* Fix matching of non-ASCII emoji names on Python 2

v1.4.2 (2021-07-30)
-----
* Delimiter for German time naming changed from ":" to "."

v1.4.1 (2021-07-18)
-----
* Fix some French emoji names not being matched
* Drop seemingly accidentally added colons from German emoji names

v1.4.0 (2021-06-22)
-----
* Added support for German naming of emojis

v1.3.0 (2021-06-02)
-----
* Added support for French naming of emojis

v1.2.1 (2021-03-13)
-----
* Added replace_emoji

v1.2.0 (2021-01-27)
-----
* Emojis of English version updated to the Emoji Charts v13.1
* Added all emoji modifiers
* Current count of emojis - 3521

v1.1.1 (2021-01-25)
-----
* Emoji extractor refactored 

v1.1.0 (2021-01-23)
-----
* Added support for Italian naming of emojis
* Added Python 3.8 and 3.9 as supported versions

v1.0.1 (2021-01-23)
-----
* Bug fixing

v1.0.0 (2021-01-22)
-----
* Added support for Spanish naming of emojis
* Added support for Portuguese naming of emojis
* Emoji packs split by language to different modules

v0.3.5
-----
* Use codecs.open() instead of open() when processing readme in setup.py - #2, #5

v0.3.4 (2015-05-19)
-----
* Restored default functionality - #6
* Removed `emoji.decode()` - #10
* Added `use_aliases` to `emoji.emojize()` to enable the GitHub aliases and others - #8

v0.2.0
---
* Added ~400 codes to bring the emoji list up to date
* emojize() regex now matches &.ô’Åéãíç
* Unittests for API and to validate emoji formatting and parsing
* decode() function to lookup emoji by their Unicode code
