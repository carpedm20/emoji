emoji
=====

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
* decode() function to lookup emoji by their unicode code
