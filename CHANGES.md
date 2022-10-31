emoji
=====

2.2.0
-----
* Add support for Unicode Version 15
* Add more translations for existing languages: (similar to Turkish Language)
* Add Readme on how to add a language
* Fix 2.0.0: sphinx warnings reference target not found

2.1.0
-----
* Added Farsi support
* Added Trove classifiers for Python 3.10 and 3.11

2.0.0
-----
* Removed the old dicts EMOJI_UNICODE_*, UNICODE_EMOJI_*
* Removed unused language=None parameters
* Removed use_alias parameter
* Removed the get_regexp method
* Removed emoji_lis
* Removed distinct_emoji_lis
* Made the list of languages public: emoji.LANGUAGES = ['en','es','pt','it','fr','de']
* Updated translations to release-41 (no changes compared to release-40)
* Generate a documentation for the public functions from the docstrings with Sphinx
* Added some more examples to the README: e.g. how to replace/remove emojis
* Total count of emojis:  4702

1.7.0
-----
* Added `emoji_list()` and `distinct_emoji_list()`
* Added deprecation warnings for several functions and variables that will be removed in version 2.0.0.
  If you don't want to see these warnings, you can stay with 1.6.x. For example in pip/requirements.txt you can pin to 1.6.x with `emoji~=1.6.3`.

1.6.3
-----
* Added support for counting unique emojis

1.6.2
-----
* Improve performance of demojize()
* Added more tests
* Added warning when someone uses any other language than 'en' with use_aliases=True in emojize()

1.6.1
-----
* Allow multiple aliases
* Restored aliases from 1.5.0

1.6.0
-----
* Fix Unicode of some emoji in the language files
* is_emoji function added
* Added dict of dict with emoji data include emoji versions and statuses
* emoji.version(string) method added
* Included 'variant' in the dict of dicts

1.5.0
-----
* Emojis of English version updated to the Emoji Charts v14.0
* Current count of emojis - 3633
* Fix matching of non-ASCII emoji names on Python 2

1.4.2
-----
* Delimiter for German time naming changed from ":" to "."

1.4.1
-----
* Fix some French emoji names not being matched
* Drop seemingly accidentally added colons from German emoji names

1.4.0
-----
* Added support for German naming of emojis

1.3.0
-----
* Added support for French naming of emojis

1.2.1
-----
* Added replace_emoji

1.2.0
-----
* Emojis of English version updated to the Emoji Charts v13.1
* Added all emoji modifiers
* Current count of emojis - 3521

1.1.1
-----
* Emoji extractor refactored 

1.1.0
-----
* Added support for Italian naming of emojis
* Added Python 3.8 and 3.9 as supported versions

1.0.1
-----
* Bug fixing

1.0.0
-----
* Added support for Spanish naming of emojis
* Added support for Portuguese naming of emojis
* Emoji packs split by language to different modules

0.3.5
-----
* Use codecs.open() instead of open() when processing readme in setup.py - #2, #5

0.3.4
-----
* Restored default functionality - #6
* Removed `emoji.decode()` - #10
* Added `use_aliases` to `emoji.emojize()` to enable the GitHub aliases and others - #8

0.2
---
* Added ~400 codes to bring the emoji list up to date
* emojize() regex now matches &.ô’Åéãíç
* Unittests for API and to validate emoji formatting and parsing
* decode() function to lookup emoji by their Unicode code
