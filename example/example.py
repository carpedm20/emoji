# -*- coding: UTF-8 -*-
import emoji

print(emoji.emojize('Water! :water_wave:'))
print(emoji.demojize(u' at runtime expect NOT to see a picture here, but regular text instead -->    🌊')) # for Python 2.x
# print(emoji.demojize('🌊')) # for Python 3.x   ##  also NO pic to be seen here. it is  "emo" and "demo" function i.e. un-emoize.
