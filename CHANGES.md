emoji
=====

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
