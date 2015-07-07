emoji
=====

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
