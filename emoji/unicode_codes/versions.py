# -*- coding: utf-8 -*-

"""Data containing all current emoji
   Extracted from https://unicode.org/Public/emoji/latest/emoji-test.txt
   and https://www.unicode.org/Public/UCD/latest/ucd/emoji/emoji-variation-sequences.txt
   See utils/get_codes_from_unicode_emoji_data_files.py

   +----------------+-------------+------------------+-------------------+
   | Emoji Version  |    Date     | Unicode Version  | Data File Comment |
   +----------------+-------------+------------------+-------------------+
   | N/A            | 2010-10-11  | Unicode 6.0      | E0.6              |
   | N/A            | 2014-06-16  | Unicode 7.0      | E0.7              |
   | Emoji 1.0      | 2015-06-09  | Unicode 8.0      | E1.0              |
   | Emoji 2.0      | 2015-11-12  | Unicode 8.0      | E2.0              |
   | Emoji 3.0      | 2016-06-03  | Unicode 9.0      | E3.0              |
   | Emoji 4.0      | 2016-11-22  | Unicode 9.0      | E4.0              |
   | Emoji 5.0      | 2017-06-20  | Unicode 10.0     | E5.0              |
   | Emoji 11.0     | 2018-05-21  | Unicode 11.0     | E11.0             |
   | Emoji 12.0     | 2019-03-05  | Unicode 12.0     | E12.0             |
   | Emoji 12.1     | 2019-10-21  | Unicode 12.1     | E12.1             |
   | Emoji 13.0     | 2020-03-10  | Unicode 13.0     | E13.0             |
   | Emoji 13.1     | 2020-09-15  | Unicode 13.0     | E13.1             |
   | Emoji 14.0     | 2021-09-14  | Unicode 14.0     | E14.0             |

                          http://www.unicode.org/reports/tr51/#Versioning

"""

__all__ = [
    'EMOJI_DATA', 'fully_qualified'
]

component = 1
fully_qualified = 2
minimally_qualified = 3
unqualified = 4


EMOJI_DATA = {
    u'\U0001F947': {
        'en' : u':1st_place_medal:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F948': {
        'en' : u':2nd_place_medal:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F949': {
        'en' : u':3rd_place_medal:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F18E': {
        'en' : u':AB_button_(blood_type):',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3E7': {
        'en' : u':ATM_sign:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F170\U0000FE0F': {
        'en' : u':A_button_(blood_type):',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F170': {
        'en' : u':A_button_(blood_type):',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F1E6\U0001F1EB': {
        'en' : u':Afghanistan:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E6\U0001F1F1': {
        'en' : u':Albania:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E9\U0001F1FF': {
        'en' : u':Algeria:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E6\U0001F1F8': {
        'en' : u':American_Samoa:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E6\U0001F1E9': {
        'en' : u':Andorra:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E6\U0001F1F4': {
        'en' : u':Angola:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E6\U0001F1EE': {
        'en' : u':Anguilla:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E6\U0001F1F6': {
        'en' : u':Antarctica:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E6\U0001F1EC': {
        'en' : u':Antigua_&_Barbuda:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U00002652': {
        'en' : u':Aquarius:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F1E6\U0001F1F7': {
        'en' : u':Argentina:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U00002648': {
        'en' : u':Aries:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F1E6\U0001F1F2': {
        'en' : u':Armenia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E6\U0001F1FC': {
        'en' : u':Aruba:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E6\U0001F1E8': {
        'en' : u':Ascension_Island:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E6\U0001F1FA': {
        'en' : u':Australia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E6\U0001F1F9': {
        'en' : u':Austria:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E6\U0001F1FF': {
        'en' : u':Azerbaijan:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F519': {
        'en' : u':BACK_arrow:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F171\U0000FE0F': {
        'en' : u':B_button_(blood_type):',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F171': {
        'en' : u':B_button_(blood_type):',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F1E7\U0001F1F8': {
        'en' : u':Bahamas:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E7\U0001F1ED': {
        'en' : u':Bahrain:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E7\U0001F1E9': {
        'en' : u':Bangladesh:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E7\U0001F1E7': {
        'en' : u':Barbados:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E7\U0001F1FE': {
        'en' : u':Belarus:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E7\U0001F1EA': {
        'en' : u':Belgium:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E7\U0001F1FF': {
        'en' : u':Belize:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E7\U0001F1EF': {
        'en' : u':Benin:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E7\U0001F1F2': {
        'en' : u':Bermuda:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E7\U0001F1F9': {
        'en' : u':Bhutan:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E7\U0001F1F4': {
        'en' : u':Bolivia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E7\U0001F1E6': {
        'en' : u':Bosnia_&_Herzegovina:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E7\U0001F1FC': {
        'en' : u':Botswana:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E7\U0001F1FB': {
        'en' : u':Bouvet_Island:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E7\U0001F1F7': {
        'en' : u':Brazil:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EE\U0001F1F4': {
        'en' : u':British_Indian_Ocean_Territory:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1FB\U0001F1EC': {
        'en' : u':British_Virgin_Islands:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E7\U0001F1F3': {
        'en' : u':Brunei:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E7\U0001F1EC': {
        'en' : u':Bulgaria:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E7\U0001F1EB': {
        'en' : u':Burkina_Faso:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E7\U0001F1EE': {
        'en' : u':Burundi:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F191': {
        'en' : u':CL_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F192': {
        'en' : u':COOL_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1F0\U0001F1ED': {
        'en' : u':Cambodia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E8\U0001F1F2': {
        'en' : u':Cameroon:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E8\U0001F1E6': {
        'en' : u':Canada:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EE\U0001F1E8': {
        'en' : u':Canary_Islands:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0000264B': {
        'en' : u':Cancer:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F1E8\U0001F1FB': {
        'en' : u':Cape_Verde:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U00002651': {
        'en' : u':Capricorn:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F1E7\U0001F1F6': {
        'en' : u':Caribbean_Netherlands:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F0\U0001F1FE': {
        'en' : u':Cayman_Islands:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E8\U0001F1EB': {
        'en' : u':Central_African_Republic:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EA\U0001F1E6': {
        'en' : u':Ceuta_&_Melilla:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F9\U0001F1E9': {
        'en' : u':Chad:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E8\U0001F1F1': {
        'en' : u':Chile:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E8\U0001F1F3': {
        'en' : u':China:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1E8\U0001F1FD': {
        'en' : u':Christmas_Island:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F384': {
        'en' : u':Christmas_tree:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1E8\U0001F1F5': {
        'en' : u':Clipperton_Island:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E8\U0001F1E8': {
        'en' : u':Cocos_(Keeling)_Islands:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E8\U0001F1F4': {
        'en' : u':Colombia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F0\U0001F1F2': {
        'en' : u':Comoros:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E8\U0001F1EC': {
        'en' : u':Congo_-_Brazzaville:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E8\U0001F1E9': {
        'en' : u':Congo_-_Kinshasa:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E8\U0001F1F0': {
        'en' : u':Cook_Islands:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E8\U0001F1F7': {
        'en' : u':Costa_Rica:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1ED\U0001F1F7': {
        'en' : u':Croatia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E8\U0001F1FA': {
        'en' : u':Cuba:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E8\U0001F1FC': {
        'en' : u':Curaçao:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E8\U0001F1FE': {
        'en' : u':Cyprus:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E8\U0001F1FF': {
        'en' : u':Czechia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E8\U0001F1EE': {
        'en' : u':Côte_d’Ivoire:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E9\U0001F1F0': {
        'en' : u':Denmark:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E9\U0001F1EC': {
        'en' : u':Diego_Garcia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E9\U0001F1EF': {
        'en' : u':Djibouti:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E9\U0001F1F2': {
        'en' : u':Dominica:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E9\U0001F1F4': {
        'en' : u':Dominican_Republic:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F51A': {
        'en' : u':END_arrow:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1EA\U0001F1E8': {
        'en' : u':Ecuador:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EA\U0001F1EC': {
        'en' : u':Egypt:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F8\U0001F1FB': {
        'en' : u':El_Salvador:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F3F4\U000E0067\U000E0062\U000E0065\U000E006E\U000E0067\U000E007F': {
        'en' : u':England:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F1EC\U0001F1F6': {
        'en' : u':Equatorial_Guinea:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EA\U0001F1F7': {
        'en' : u':Eritrea:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EA\U0001F1EA': {
        'en' : u':Estonia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F8\U0001F1FF': {
        'en' : u':Eswatini:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EA\U0001F1F9': {
        'en' : u':Ethiopia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EA\U0001F1FA': {
        'en' : u':European_Union:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F193': {
        'en' : u':FREE_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1EB\U0001F1F0': {
        'en' : u':Falkland_Islands:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EB\U0001F1F4': {
        'en' : u':Faroe_Islands:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EB\U0001F1EF': {
        'en' : u':Fiji:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EB\U0001F1EE': {
        'en' : u':Finland:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EB\U0001F1F7': {
        'en' : u':France:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1EC\U0001F1EB': {
        'en' : u':French_Guiana:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F5\U0001F1EB': {
        'en' : u':French_Polynesia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F9\U0001F1EB': {
        'en' : u':French_Southern_Territories:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EC\U0001F1E6': {
        'en' : u':Gabon:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EC\U0001F1F2': {
        'en' : u':Gambia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0000264A': {
        'en' : u':Gemini:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F1EC\U0001F1EA': {
        'en' : u':Georgia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E9\U0001F1EA': {
        'en' : u':Germany:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1EC\U0001F1ED': {
        'en' : u':Ghana:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EC\U0001F1EE': {
        'en' : u':Gibraltar:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EC\U0001F1F7': {
        'en' : u':Greece:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EC\U0001F1F1': {
        'en' : u':Greenland:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EC\U0001F1E9': {
        'en' : u':Grenada:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EC\U0001F1F5': {
        'en' : u':Guadeloupe:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EC\U0001F1FA': {
        'en' : u':Guam:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EC\U0001F1F9': {
        'en' : u':Guatemala:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EC\U0001F1EC': {
        'en' : u':Guernsey:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EC\U0001F1F3': {
        'en' : u':Guinea:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EC\U0001F1FC': {
        'en' : u':Guinea-Bissau:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EC\U0001F1FE': {
        'en' : u':Guyana:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1ED\U0001F1F9': {
        'en' : u':Haiti:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1ED\U0001F1F2': {
        'en' : u':Heard_&_McDonald_Islands:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1ED\U0001F1F3': {
        'en' : u':Honduras:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1ED\U0001F1F0': {
        'en' : u':Hong_Kong_SAR_China:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1ED\U0001F1FA': {
        'en' : u':Hungary:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F194': {
        'en' : u':ID_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1EE\U0001F1F8': {
        'en' : u':Iceland:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EE\U0001F1F3': {
        'en' : u':India:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EE\U0001F1E9': {
        'en' : u':Indonesia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EE\U0001F1F7': {
        'en' : u':Iran:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EE\U0001F1F6': {
        'en' : u':Iraq:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EE\U0001F1EA': {
        'en' : u':Ireland:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EE\U0001F1F2': {
        'en' : u':Isle_of_Man:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EE\U0001F1F1': {
        'en' : u':Israel:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EE\U0001F1F9': {
        'en' : u':Italy:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1EF\U0001F1F2': {
        'en' : u':Jamaica:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EF\U0001F1F5': {
        'en' : u':Japan:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F251': {
        'en' : u':Japanese_acceptable_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F238': {
        'en' : u':Japanese_application_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F250': {
        'en' : u':Japanese_bargain_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3EF': {
        'en' : u':Japanese_castle:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00003297\U0000FE0F': {
        'en' : u':Japanese_congratulations_button:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00003297': {
        'en' : u':Japanese_congratulations_button:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F239': {
        'en' : u':Japanese_discount_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F38E': {
        'en' : u':Japanese_dolls:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F21A': {
        'en' : u':Japanese_free_of_charge_button:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F201': {
        'en' : u':Japanese_here_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F237\U0000FE0F': {
        'en' : u':Japanese_monthly_amount_button:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F237': {
        'en' : u':Japanese_monthly_amount_button:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F235': {
        'en' : u':Japanese_no_vacancy_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F236': {
        'en' : u':Japanese_not_free_of_charge_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F23A': {
        'en' : u':Japanese_open_for_business_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F234': {
        'en' : u':Japanese_passing_grade_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3E3': {
        'en' : u':Japanese_post_office:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F232': {
        'en' : u':Japanese_prohibited_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F22F': {
        'en' : u':Japanese_reserved_button:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00003299\U0000FE0F': {
        'en' : u':Japanese_secret_button:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00003299': {
        'en' : u':Japanese_secret_button:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F202\U0000FE0F': {
        'en' : u':Japanese_service_charge_button:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F202': {
        'en' : u':Japanese_service_charge_button:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F530': {
        'en' : u':Japanese_symbol_for_beginner:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F233': {
        'en' : u':Japanese_vacancy_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1EF\U0001F1EA': {
        'en' : u':Jersey:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EF\U0001F1F4': {
        'en' : u':Jordan:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F0\U0001F1FF': {
        'en' : u':Kazakhstan:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F0\U0001F1EA': {
        'en' : u':Kenya:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F0\U0001F1EE': {
        'en' : u':Kiribati:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1FD\U0001F1F0': {
        'en' : u':Kosovo:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F0\U0001F1FC': {
        'en' : u':Kuwait:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F0\U0001F1EC': {
        'en' : u':Kyrgyzstan:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F1\U0001F1E6': {
        'en' : u':Laos:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F1\U0001F1FB': {
        'en' : u':Latvia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F1\U0001F1E7': {
        'en' : u':Lebanon:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0000264C': {
        'en' : u':Leo:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F1F1\U0001F1F8': {
        'en' : u':Lesotho:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F1\U0001F1F7': {
        'en' : u':Liberia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0000264E': {
        'en' : u':Libra:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F1F1\U0001F1FE': {
        'en' : u':Libya:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F1\U0001F1EE': {
        'en' : u':Liechtenstein:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F1\U0001F1F9': {
        'en' : u':Lithuania:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F1\U0001F1FA': {
        'en' : u':Luxembourg:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1F4': {
        'en' : u':Macao_SAR_China:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1EC': {
        'en' : u':Madagascar:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1FC': {
        'en' : u':Malawi:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1FE': {
        'en' : u':Malaysia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1FB': {
        'en' : u':Maldives:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1F1': {
        'en' : u':Mali:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1F9': {
        'en' : u':Malta:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1ED': {
        'en' : u':Marshall_Islands:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1F6': {
        'en' : u':Martinique:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1F7': {
        'en' : u':Mauritania:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1FA': {
        'en' : u':Mauritius:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1FE\U0001F1F9': {
        'en' : u':Mayotte:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1FD': {
        'en' : u':Mexico:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EB\U0001F1F2': {
        'en' : u':Micronesia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1E9': {
        'en' : u':Moldova:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1E8': {
        'en' : u':Monaco:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1F3': {
        'en' : u':Mongolia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1EA': {
        'en' : u':Montenegro:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1F8': {
        'en' : u':Montserrat:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1E6': {
        'en' : u':Morocco:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1FF': {
        'en' : u':Mozambique:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F936': {
        'en' : u':Mrs._Claus:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F936\U0001F3FF': {
        'en' : u':Mrs._Claus_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F936\U0001F3FB': {
        'en' : u':Mrs._Claus_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F936\U0001F3FE': {
        'en' : u':Mrs._Claus_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F936\U0001F3FC': {
        'en' : u':Mrs._Claus_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F936\U0001F3FD': {
        'en' : u':Mrs._Claus_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F1F2\U0001F1F2': {
        'en' : u':Myanmar_(Burma):',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F195': {
        'en' : u':NEW_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F196': {
        'en' : u':NG_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1F3\U0001F1E6': {
        'en' : u':Namibia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F3\U0001F1F7': {
        'en' : u':Nauru:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F3\U0001F1F5': {
        'en' : u':Nepal:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F3\U0001F1F1': {
        'en' : u':Netherlands:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F3\U0001F1E8': {
        'en' : u':New_Caledonia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F3\U0001F1FF': {
        'en' : u':New_Zealand:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F3\U0001F1EE': {
        'en' : u':Nicaragua:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F3\U0001F1EA': {
        'en' : u':Niger:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F3\U0001F1EC': {
        'en' : u':Nigeria:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F3\U0001F1FA': {
        'en' : u':Niue:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F3\U0001F1EB': {
        'en' : u':Norfolk_Island:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F0\U0001F1F5': {
        'en' : u':North_Korea:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1F0': {
        'en' : u':North_Macedonia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1F5': {
        'en' : u':Northern_Mariana_Islands:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F3\U0001F1F4': {
        'en' : u':Norway:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F197': {
        'en' : u':OK_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F44C': {
        'en' : u':OK_hand:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F44C\U0001F3FF': {
        'en' : u':OK_hand_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44C\U0001F3FB': {
        'en' : u':OK_hand_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44C\U0001F3FE': {
        'en' : u':OK_hand_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44C\U0001F3FC': {
        'en' : u':OK_hand_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44C\U0001F3FD': {
        'en' : u':OK_hand_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F51B': {
        'en' : u':ON!_arrow:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F17E\U0000FE0F': {
        'en' : u':O_button_(blood_type):',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F17E': {
        'en' : u':O_button_(blood_type):',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F1F4\U0001F1F2': {
        'en' : u':Oman:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U000026CE': {
        'en' : u':Ophiuchus:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F17F\U0000FE0F': {
        'en' : u':P_button:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F17F': {
        'en' : u':P_button:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F1F5\U0001F1F0': {
        'en' : u':Pakistan:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F5\U0001F1FC': {
        'en' : u':Palau:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F5\U0001F1F8': {
        'en' : u':Palestinian_Territories:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F5\U0001F1E6': {
        'en' : u':Panama:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F5\U0001F1EC': {
        'en' : u':Papua_New_Guinea:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F5\U0001F1FE': {
        'en' : u':Paraguay:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F5\U0001F1EA': {
        'en' : u':Peru:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F5\U0001F1ED': {
        'en' : u':Philippines:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U00002653': {
        'en' : u':Pisces:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F1F5\U0001F1F3': {
        'en' : u':Pitcairn_Islands:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F5\U0001F1F1': {
        'en' : u':Poland:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F5\U0001F1F9': {
        'en' : u':Portugal:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F5\U0001F1F7': {
        'en' : u':Puerto_Rico:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F6\U0001F1E6': {
        'en' : u':Qatar:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F7\U0001F1F4': {
        'en' : u':Romania:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F7\U0001F1FA': {
        'en' : u':Russia:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1F7\U0001F1FC': {
        'en' : u':Rwanda:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F7\U0001F1EA': {
        'en' : u':Réunion:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F51C': {
        'en' : u':SOON_arrow:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F198': {
        'en' : u':SOS_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00002650': {
        'en' : u':Sagittarius:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F1FC\U0001F1F8': {
        'en' : u':Samoa:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F8\U0001F1F2': {
        'en' : u':San_Marino:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F385': {
        'en' : u':Santa_Claus:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F385\U0001F3FF': {
        'en' : u':Santa_Claus_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F385\U0001F3FB': {
        'en' : u':Santa_Claus_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F385\U0001F3FE': {
        'en' : u':Santa_Claus_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F385\U0001F3FC': {
        'en' : u':Santa_Claus_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F385\U0001F3FD': {
        'en' : u':Santa_Claus_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F1F8\U0001F1E6': {
        'en' : u':Saudi_Arabia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0000264F': {
        'en' : u':Scorpio:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F3F4\U000E0067\U000E0062\U000E0073\U000E0063\U000E0074\U000E007F': {
        'en' : u':Scotland:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F1F8\U0001F1F3': {
        'en' : u':Senegal:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F7\U0001F1F8': {
        'en' : u':Serbia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F8\U0001F1E8': {
        'en' : u':Seychelles:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F8\U0001F1F1': {
        'en' : u':Sierra_Leone:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F8\U0001F1EC': {
        'en' : u':Singapore:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F8\U0001F1FD': {
        'en' : u':Sint_Maarten:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F8\U0001F1F0': {
        'en' : u':Slovakia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F8\U0001F1EE': {
        'en' : u':Slovenia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F8\U0001F1E7': {
        'en' : u':Solomon_Islands:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F8\U0001F1F4': {
        'en' : u':Somalia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1FF\U0001F1E6': {
        'en' : u':South_Africa:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EC\U0001F1F8': {
        'en' : u':South_Georgia_&_South_Sandwich_Islands:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F0\U0001F1F7': {
        'en' : u':South_Korea:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1F8\U0001F1F8': {
        'en' : u':South_Sudan:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EA\U0001F1F8': {
        'en' : u':Spain:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1F1\U0001F1F0': {
        'en' : u':Sri_Lanka:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E7\U0001F1F1': {
        'en' : u':St._Barthélemy:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F8\U0001F1ED': {
        'en' : u':St._Helena:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F0\U0001F1F3': {
        'en' : u':St._Kitts_&_Nevis:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F1\U0001F1E8': {
        'en' : u':St._Lucia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F2\U0001F1EB': {
        'en' : u':St._Martin:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F5\U0001F1F2': {
        'en' : u':St._Pierre_&_Miquelon:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1FB\U0001F1E8': {
        'en' : u':St._Vincent_&_Grenadines:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F5FD': {
        'en' : u':Statue_of_Liberty:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1F8\U0001F1E9': {
        'en' : u':Sudan:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F8\U0001F1F7': {
        'en' : u':Suriname:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F8\U0001F1EF': {
        'en' : u':Svalbard_&_Jan_Mayen:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F8\U0001F1EA': {
        'en' : u':Sweden:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E8\U0001F1ED': {
        'en' : u':Switzerland:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F8\U0001F1FE': {
        'en' : u':Syria:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F8\U0001F1F9': {
        'en' : u':São_Tomé_&_Príncipe:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F996': {
        'en' : u':T-Rex:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F51D': {
        'en' : u':TOP_arrow:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1F9\U0001F1FC': {
        'en' : u':Taiwan:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F9\U0001F1EF': {
        'en' : u':Tajikistan:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F9\U0001F1FF': {
        'en' : u':Tanzania:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U00002649': {
        'en' : u':Taurus:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F1F9\U0001F1ED': {
        'en' : u':Thailand:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F9\U0001F1F1': {
        'en' : u':Timor-Leste:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F9\U0001F1EC': {
        'en' : u':Togo:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F9\U0001F1F0': {
        'en' : u':Tokelau:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F5FC': {
        'en' : u':Tokyo_tower:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1F9\U0001F1F4': {
        'en' : u':Tonga:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F9\U0001F1F9': {
        'en' : u':Trinidad_&_Tobago:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F9\U0001F1E6': {
        'en' : u':Tristan_da_Cunha:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F9\U0001F1F3': {
        'en' : u':Tunisia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F9\U0001F1F7': {
        'en' : u':Turkey:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F9\U0001F1F2': {
        'en' : u':Turkmenistan:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F9\U0001F1E8': {
        'en' : u':Turks_&_Caicos_Islands:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1F9\U0001F1FB': {
        'en' : u':Tuvalu:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1FA\U0001F1F2': {
        'en' : u':U.S._Outlying_Islands:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1FB\U0001F1EE': {
        'en' : u':U.S._Virgin_Islands:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F199': {
        'en' : u':UP!_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1FA\U0001F1EC': {
        'en' : u':Uganda:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1FA\U0001F1E6': {
        'en' : u':Ukraine:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1E6\U0001F1EA': {
        'en' : u':United_Arab_Emirates:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EC\U0001F1E7': {
        'en' : u':United_Kingdom:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1FA\U0001F1F3': {
        'en' : u':United_Nations:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F1FA\U0001F1F8': {
        'en' : u':United_States:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1FA\U0001F1FE': {
        'en' : u':Uruguay:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1FA\U0001F1FF': {
        'en' : u':Uzbekistan:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F19A': {
        'en' : u':VS_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1FB\U0001F1FA': {
        'en' : u':Vanuatu:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1FB\U0001F1E6': {
        'en' : u':Vatican_City:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1FB\U0001F1EA': {
        'en' : u':Venezuela:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1FB\U0001F1F3': {
        'en' : u':Vietnam:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0000264D': {
        'en' : u':Virgo:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F3F4\U000E0067\U000E0062\U000E0077\U000E006C\U000E0073\U000E007F': {
        'en' : u':Wales:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F1FC\U0001F1EB': {
        'en' : u':Wallis_&_Futuna:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1EA\U0001F1ED': {
        'en' : u':Western_Sahara:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1FE\U0001F1EA': {
        'en' : u':Yemen:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1FF\U0001F1F2': {
        'en' : u':Zambia:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F1FF\U0001F1FC': {
        'en' : u':Zimbabwe:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F9EE': {
        'en' : u':abacus:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001FA97': {
        'en' : u':accordion:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001FA79': {
        'en' : u':adhesive_bandage:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F39F\U0000FE0F': {
        'en' : u':admission_tickets:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F39F': {
        'en' : u':admission_tickets:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6A1': {
        'en' : u':aerial_tramway:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U00002708\U0000FE0F': {
        'en' : u':airplane:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002708': {
        'en' : u':airplane:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F6EC': {
        'en' : u':airplane_arrival:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6EB': {
        'en' : u':airplane_departure:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U000023F0': {
        'en' : u':alarm_clock:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00002697\U0000FE0F': {
        'en' : u':alembic:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U00002697': {
        'en' : u':alembic:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0001F47D': {
        'en' : u':alien:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F47E': {
        'en' : u':alien_monster:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F691': {
        'en' : u':ambulance:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F3C8': {
        'en' : u':american_football:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3FA': {
        'en' : u':amphora:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001FAC0': {
        'en' : u':anatomical_heart:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U00002693': {
        'en' : u':anchor:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F4A2': {
        'en' : u':anger_symbol:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F620': {
        'en' : u':angry_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F47F': {
        'en' : u':angry_face_with_horns:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F627': {
        'en' : u':anguished_face:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F41C': {
        'en' : u':ant:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4F6': {
        'en' : u':antenna_bars:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F630': {
        'en' : u':anxious_face_with_sweat:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F69B': {
        'en' : u':articulated_lorry:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F9D1\U0000200D\U0001F3A8': {
        'en' : u':artist:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F3A8': {
        'en' : u':artist_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F3A8': {
        'en' : u':artist_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F3A8': {
        'en' : u':artist_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F3A8': {
        'en' : u':artist_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F3A8': {
        'en' : u':artist_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F3A8': {
        'en' : u':artist_palette:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F632': {
        'en' : u':astonished_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9D1\U0000200D\U0001F680': {
        'en' : u':astronaut:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F680': {
        'en' : u':astronaut_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F680': {
        'en' : u':astronaut_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F680': {
        'en' : u':astronaut_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F680': {
        'en' : u':astronaut_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F680': {
        'en' : u':astronaut_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0000269B\U0000FE0F': {
        'en' : u':atom_symbol:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0000269B': {
        'en' : u':atom_symbol:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0001F6FA': {
        'en' : u':auto_rickshaw:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F697': {
        'en' : u':automobile:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F951': {
        'en' : u':avocado:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001FA93': {
        'en' : u':axe:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F476': {
        'en' : u':baby:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F47C': {
        'en' : u':baby_angel:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F47C\U0001F3FF': {
        'en' : u':baby_angel_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F47C\U0001F3FB': {
        'en' : u':baby_angel_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F47C\U0001F3FE': {
        'en' : u':baby_angel_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F47C\U0001F3FC': {
        'en' : u':baby_angel_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F47C\U0001F3FD': {
        'en' : u':baby_angel_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F37C': {
        'en' : u':baby_bottle:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F424': {
        'en' : u':baby_chick:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F476\U0001F3FF': {
        'en' : u':baby_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F476\U0001F3FB': {
        'en' : u':baby_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F476\U0001F3FE': {
        'en' : u':baby_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F476\U0001F3FC': {
        'en' : u':baby_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F476\U0001F3FD': {
        'en' : u':baby_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6BC': {
        'en' : u':baby_symbol:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F447': {
        'en' : u':backhand_index_pointing_down:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F447\U0001F3FF': {
        'en' : u':backhand_index_pointing_down_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F447\U0001F3FB': {
        'en' : u':backhand_index_pointing_down_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F447\U0001F3FE': {
        'en' : u':backhand_index_pointing_down_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F447\U0001F3FC': {
        'en' : u':backhand_index_pointing_down_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F447\U0001F3FD': {
        'en' : u':backhand_index_pointing_down_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F448': {
        'en' : u':backhand_index_pointing_left:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F448\U0001F3FF': {
        'en' : u':backhand_index_pointing_left_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F448\U0001F3FB': {
        'en' : u':backhand_index_pointing_left_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F448\U0001F3FE': {
        'en' : u':backhand_index_pointing_left_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F448\U0001F3FC': {
        'en' : u':backhand_index_pointing_left_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F448\U0001F3FD': {
        'en' : u':backhand_index_pointing_left_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F449': {
        'en' : u':backhand_index_pointing_right:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F449\U0001F3FF': {
        'en' : u':backhand_index_pointing_right_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F449\U0001F3FB': {
        'en' : u':backhand_index_pointing_right_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F449\U0001F3FE': {
        'en' : u':backhand_index_pointing_right_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F449\U0001F3FC': {
        'en' : u':backhand_index_pointing_right_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F449\U0001F3FD': {
        'en' : u':backhand_index_pointing_right_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F446': {
        'en' : u':backhand_index_pointing_up:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F446\U0001F3FF': {
        'en' : u':backhand_index_pointing_up_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F446\U0001F3FB': {
        'en' : u':backhand_index_pointing_up_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F446\U0001F3FE': {
        'en' : u':backhand_index_pointing_up_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F446\U0001F3FC': {
        'en' : u':backhand_index_pointing_up_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F446\U0001F3FD': {
        'en' : u':backhand_index_pointing_up_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F392': {
        'en' : u':backpack:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F953': {
        'en' : u':bacon:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F9A1': {
        'en' : u':badger:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F3F8': {
        'en' : u':badminton:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F96F': {
        'en' : u':bagel:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F6C4': {
        'en' : u':baggage_claim:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F956': {
        'en' : u':baguette_bread:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U00002696\U0000FE0F': {
        'en' : u':balance_scale:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U00002696': {
        'en' : u':balance_scale:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0001F9B2': {
        'en' : u':bald:',
        'status' : component,
        'E' : 11
    },
    u'\U0001FA70': {
        'en' : u':ballet_shoes:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F388': {
        'en' : u':balloon:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F5F3\U0000FE0F': {
        'en' : u':ballot_box_with_ballot:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5F3': {
        'en' : u':ballot_box_with_ballot:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F34C': {
        'en' : u':banana:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FA95': {
        'en' : u':banjo:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F3E6': {
        'en' : u':bank:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4CA': {
        'en' : u':bar_chart:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F488': {
        'en' : u':barber_pole:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U000026BE': {
        'en' : u':baseball:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F9FA': {
        'en' : u':basket:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F3C0': {
        'en' : u':basketball:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F987': {
        'en' : u':bat:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F6C1': {
        'en' : u':bathtub:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F50B': {
        'en' : u':battery:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3D6\U0000FE0F': {
        'en' : u':beach_with_umbrella:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3D6': {
        'en' : u':beach_with_umbrella:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F601': {
        'en' : u':beaming_face_with_smiling_eyes:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FAD8': {
        'en' : u':beans:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F43B': {
        'en' : u':bear:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F493': {
        'en' : u':beating_heart:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9AB': {
        'en' : u':beaver:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F6CF\U0000FE0F': {
        'en' : u':bed:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6CF': {
        'en' : u':bed:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F37A': {
        'en' : u':beer_mug:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FAB2': {
        'en' : u':beetle:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F514': {
        'en' : u':bell:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FAD1': {
        'en' : u':bell_pepper:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F515': {
        'en' : u':bell_with_slash:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6CE\U0000FE0F': {
        'en' : u':bellhop_bell:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6CE': {
        'en' : u':bellhop_bell:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F371': {
        'en' : u':bento_box:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9C3': {
        'en' : u':beverage_box:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F6B2': {
        'en' : u':bicycle:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F459': {
        'en' : u':bikini:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9E2': {
        'en' : u':billed_cap:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U00002623\U0000FE0F': {
        'en' : u':biohazard:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U00002623': {
        'en' : u':biohazard:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0001F426': {
        'en' : u':bird:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F382': {
        'en' : u':birthday_cake:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9AC': {
        'en' : u':bison:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001FAE6': {
        'en' : u':biting_lip:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F408\U0000200D\U00002B1B': {
        'en' : u':black_cat:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U000026AB': {
        'en' : u':black_circle:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F3F4': {
        'en' : u':black_flag:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F5A4': {
        'en' : u':black_heart:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U00002B1B': {
        'en' : u':black_large_square:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000025FE': {
        'en' : u':black_medium-small_square:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000025FC\U0000FE0F': {
        'en' : u':black_medium_square:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000025FC': {
        'en' : u':black_medium_square:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002712\U0000FE0F': {
        'en' : u':black_nib:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002712': {
        'en' : u':black_nib:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000025AA\U0000FE0F': {
        'en' : u':black_small_square:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000025AA': {
        'en' : u':black_small_square:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F532': {
        'en' : u':black_square_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F33C': {
        'en' : u':blossom:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F421': {
        'en' : u':blowfish:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4D8': {
        'en' : u':blue_book:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F535': {
        'en' : u':blue_circle:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F499': {
        'en' : u':blue_heart:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F7E6': {
        'en' : u':blue_square:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001FAD0': {
        'en' : u':blueberries:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F417': {
        'en' : u':boar:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4A3': {
        'en' : u':bomb:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F9B4': {
        'en' : u':bone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F516': {
        'en' : u':bookmark:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4D1': {
        'en' : u':bookmark_tabs:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4DA': {
        'en' : u':books:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001FA83': {
        'en' : u':boomerang:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F37E': {
        'en' : u':bottle_with_popping_cork:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F490': {
        'en' : u':bouquet:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3F9': {
        'en' : u':bow_and_arrow:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F963': {
        'en' : u':bowl_with_spoon:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F3B3': {
        'en' : u':bowling:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F94A': {
        'en' : u':boxing_glove:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F466': {
        'en' : u':boy:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F466\U0001F3FF': {
        'en' : u':boy_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F466\U0001F3FB': {
        'en' : u':boy_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F466\U0001F3FE': {
        'en' : u':boy_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F466\U0001F3FC': {
        'en' : u':boy_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F466\U0001F3FD': {
        'en' : u':boy_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F9E0': {
        'en' : u':brain:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F35E': {
        'en' : u':bread:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F931': {
        'en' : u':breast-feeding:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F931\U0001F3FF': {
        'en' : u':breast-feeding_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F931\U0001F3FB': {
        'en' : u':breast-feeding_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F931\U0001F3FE': {
        'en' : u':breast-feeding_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F931\U0001F3FC': {
        'en' : u':breast-feeding_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F931\U0001F3FD': {
        'en' : u':breast-feeding_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9F1': {
        'en' : u':brick:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F309': {
        'en' : u':bridge_at_night:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4BC': {
        'en' : u':briefcase:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FA72': {
        'en' : u':briefs:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F506': {
        'en' : u':bright_button:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F966': {
        'en' : u':broccoli:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F494': {
        'en' : u':broken_heart:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9F9': {
        'en' : u':broom:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F7E4': {
        'en' : u':brown_circle:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F90E': {
        'en' : u':brown_heart:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F7EB': {
        'en' : u':brown_square:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CB': {
        'en' : u':bubble_tea:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001FAE7': {
        'en' : u':bubbles:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAA3': {
        'en' : u':bucket:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F41B': {
        'en' : u':bug:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3D7\U0000FE0F': {
        'en' : u':building_construction:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3D7': {
        'en' : u':building_construction:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F685': {
        'en' : u':bullet_train:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3AF': {
        'en' : u':bullseye:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F32F': {
        'en' : u':burrito:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F68C': {
        'en' : u':bus:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F68F': {
        'en' : u':bus_stop:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F464': {
        'en' : u':bust_in_silhouette:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F465': {
        'en' : u':busts_in_silhouette:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F9C8': {
        'en' : u':butter:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F98B': {
        'en' : u':butterfly:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F335': {
        'en' : u':cactus:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4C5': {
        'en' : u':calendar:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F919': {
        'en' : u':call_me_hand:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F919\U0001F3FF': {
        'en' : u':call_me_hand_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F919\U0001F3FB': {
        'en' : u':call_me_hand_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F919\U0001F3FE': {
        'en' : u':call_me_hand_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F919\U0001F3FC': {
        'en' : u':call_me_hand_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F919\U0001F3FD': {
        'en' : u':call_me_hand_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F42A': {
        'en' : u':camel:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F4F7': {
        'en' : u':camera:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F4F8': {
        'en' : u':camera_with_flash:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3D5\U0000FE0F': {
        'en' : u':camping:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3D5': {
        'en' : u':camping:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F56F\U0000FE0F': {
        'en' : u':candle:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F56F': {
        'en' : u':candle:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F36C': {
        'en' : u':candy:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F96B': {
        'en' : u':canned_food:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F6F6': {
        'en' : u':canoe:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F5C3\U0000FE0F': {
        'en' : u':card_file_box:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5C3': {
        'en' : u':card_file_box:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F4C7': {
        'en' : u':card_index:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F5C2\U0000FE0F': {
        'en' : u':card_index_dividers:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5C2': {
        'en' : u':card_index_dividers:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3A0': {
        'en' : u':carousel_horse:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F38F': {
        'en' : u':carp_streamer:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FA9A': {
        'en' : u':carpentry_saw:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F955': {
        'en' : u':carrot:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F3F0': {
        'en' : u':castle:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F408': {
        'en' : u':cat:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F431': {
        'en' : u':cat_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F639': {
        'en' : u':cat_with_tears_of_joy:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F63C': {
        'en' : u':cat_with_wry_smile:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U000026D3\U0000FE0F': {
        'en' : u':chains:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000026D3': {
        'en' : u':chains:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001FA91': {
        'en' : u':chair:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F4C9': {
        'en' : u':chart_decreasing:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4C8': {
        'en' : u':chart_increasing:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4B9': {
        'en' : u':chart_increasing_with_yen:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00002611\U0000FE0F': {
        'en' : u':check_box_with_check:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002611': {
        'en' : u':check_box_with_check:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002714\U0000FE0F': {
        'en' : u':check_mark:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002714': {
        'en' : u':check_mark:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002705': {
        'en' : u':check_mark_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9C0': {
        'en' : u':cheese_wedge:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3C1': {
        'en' : u':chequered_flag:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F352': {
        'en' : u':cherries:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F338': {
        'en' : u':cherry_blossom:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0000265F\U0000FE0F': {
        'en' : u':chess_pawn:',
        'status' : fully_qualified,
        'E' : 11,
        'variant': True,
    },
    u'\U0000265F': {
        'en' : u':chess_pawn:',
        'status' : unqualified,
        'E' : 11,
        'variant': True,
    },
    u'\U0001F330': {
        'en' : u':chestnut:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F414': {
        'en' : u':chicken:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9D2': {
        'en' : u':child:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D2\U0001F3FF': {
        'en' : u':child_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D2\U0001F3FB': {
        'en' : u':child_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D2\U0001F3FE': {
        'en' : u':child_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D2\U0001F3FC': {
        'en' : u':child_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D2\U0001F3FD': {
        'en' : u':child_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F6B8': {
        'en' : u':children_crossing:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F43F\U0000FE0F': {
        'en' : u':chipmunk:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F43F': {
        'en' : u':chipmunk:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F36B': {
        'en' : u':chocolate_bar:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F962': {
        'en' : u':chopsticks:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U000026EA': {
        'en' : u':church:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F6AC': {
        'en' : u':cigarette:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3A6': {
        'en' : u':cinema:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U000024C2\U0000FE0F': {
        'en' : u':circled_M:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000024C2': {
        'en' : u':circled_M:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F3AA': {
        'en' : u':circus_tent:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3D9\U0000FE0F': {
        'en' : u':cityscape:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3D9': {
        'en' : u':cityscape:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F306': {
        'en' : u':cityscape_at_dusk:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F5DC\U0000FE0F': {
        'en' : u':clamp:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5DC': {
        'en' : u':clamp:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3AC': {
        'en' : u':clapper_board:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F44F': {
        'en' : u':clapping_hands:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F44F\U0001F3FF': {
        'en' : u':clapping_hands_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44F\U0001F3FB': {
        'en' : u':clapping_hands_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44F\U0001F3FE': {
        'en' : u':clapping_hands_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44F\U0001F3FC': {
        'en' : u':clapping_hands_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44F\U0001F3FD': {
        'en' : u':clapping_hands_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3DB\U0000FE0F': {
        'en' : u':classical_building:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3DB': {
        'en' : u':classical_building:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F37B': {
        'en' : u':clinking_beer_mugs:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F942': {
        'en' : u':clinking_glasses:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F4CB': {
        'en' : u':clipboard:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F503': {
        'en' : u':clockwise_vertical_arrows:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4D5': {
        'en' : u':closed_book:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4EA': {
        'en' : u':closed_mailbox_with_lowered_flag:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F4EB': {
        'en' : u':closed_mailbox_with_raised_flag:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F302': {
        'en' : u':closed_umbrella:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00002601\U0000FE0F': {
        'en' : u':cloud:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002601': {
        'en' : u':cloud:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F329\U0000FE0F': {
        'en' : u':cloud_with_lightning:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F329': {
        'en' : u':cloud_with_lightning:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000026C8\U0000FE0F': {
        'en' : u':cloud_with_lightning_and_rain:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000026C8': {
        'en' : u':cloud_with_lightning_and_rain:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F327\U0000FE0F': {
        'en' : u':cloud_with_rain:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F327': {
        'en' : u':cloud_with_rain:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F328\U0000FE0F': {
        'en' : u':cloud_with_snow:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F328': {
        'en' : u':cloud_with_snow:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F921': {
        'en' : u':clown_face:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U00002663\U0000FE0F': {
        'en' : u':club_suit:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002663': {
        'en' : u':club_suit:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F45D': {
        'en' : u':clutch_bag:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9E5': {
        'en' : u':coat:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001FAB3': {
        'en' : u':cockroach:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F378': {
        'en' : u':cocktail_glass:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F965': {
        'en' : u':coconut:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U000026B0\U0000FE0F': {
        'en' : u':coffin:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U000026B0': {
        'en' : u':coffin:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0001FA99': {
        'en' : u':coin:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F976': {
        'en' : u':cold_face:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F4A5': {
        'en' : u':collision:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00002604\U0000FE0F': {
        'en' : u':comet:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U00002604': {
        'en' : u':comet:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0001F9ED': {
        'en' : u':compass:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F4BD': {
        'en' : u':computer_disk:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F5B1\U0000FE0F': {
        'en' : u':computer_mouse:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5B1': {
        'en' : u':computer_mouse:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F38A': {
        'en' : u':confetti_ball:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F616': {
        'en' : u':confounded_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F615': {
        'en' : u':confused_face:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6A7': {
        'en' : u':construction:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F477': {
        'en' : u':construction_worker:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F477\U0001F3FF': {
        'en' : u':construction_worker_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F477\U0001F3FB': {
        'en' : u':construction_worker_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F477\U0001F3FE': {
        'en' : u':construction_worker_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F477\U0001F3FC': {
        'en' : u':construction_worker_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F477\U0001F3FD': {
        'en' : u':construction_worker_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F39B\U0000FE0F': {
        'en' : u':control_knobs:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F39B': {
        'en' : u':control_knobs:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3EA': {
        'en' : u':convenience_store:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9D1\U0000200D\U0001F373': {
        'en' : u':cook:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F373': {
        'en' : u':cook_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F373': {
        'en' : u':cook_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F373': {
        'en' : u':cook_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F373': {
        'en' : u':cook_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F373': {
        'en' : u':cook_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F35A': {
        'en' : u':cooked_rice:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F36A': {
        'en' : u':cookie:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F373': {
        'en' : u':cooking:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U000000A9\U0000FE0F': {
        'en' : u':copyright:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000000A9': {
        'en' : u':copyright:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001FAB8': {
        'en' : u':coral:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F6CB\U0000FE0F': {
        'en' : u':couch_and_lamp:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6CB': {
        'en' : u':couch_and_lamp:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F504': {
        'en' : u':counterclockwise_arrows_button:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F491': {
        'en' : u':couple_with_heart:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F491\U0001F3FF': {
        'en' : u':couple_with_heart_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F491\U0001F3FB': {
        'en' : u':couple_with_heart_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468': {
        'en' : u':couple_with_heart_man_man:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F468\U0000200D\U00002764\U0000200D\U0001F468': {
        'en' : u':couple_with_heart_man_man:',
        'status' : minimally_qualified,
        'E' : 2
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':couple_with_heart_man_man_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':couple_with_heart_man_man_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':couple_with_heart_man_man_dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':couple_with_heart_man_man_dark_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':couple_with_heart_man_man_dark_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':couple_with_heart_man_man_dark_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':couple_with_heart_man_man_dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':couple_with_heart_man_man_dark_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':couple_with_heart_man_man_dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':couple_with_heart_man_man_dark_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':couple_with_heart_man_man_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':couple_with_heart_man_man_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':couple_with_heart_man_man_light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':couple_with_heart_man_man_light_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':couple_with_heart_man_man_light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':couple_with_heart_man_man_light_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':couple_with_heart_man_man_light_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':couple_with_heart_man_man_light_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':couple_with_heart_man_man_light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':couple_with_heart_man_man_light_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':couple_with_heart_man_man_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':couple_with_heart_man_man_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':couple_with_heart_man_man_medium-dark_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':couple_with_heart_man_man_medium-dark_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':couple_with_heart_man_man_medium-dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':couple_with_heart_man_man_medium-dark_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':couple_with_heart_man_man_medium-dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':couple_with_heart_man_man_medium-dark_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':couple_with_heart_man_man_medium-dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':couple_with_heart_man_man_medium-dark_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':couple_with_heart_man_man_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':couple_with_heart_man_man_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':couple_with_heart_man_man_medium-light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':couple_with_heart_man_man_medium-light_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':couple_with_heart_man_man_medium-light_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':couple_with_heart_man_man_medium-light_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':couple_with_heart_man_man_medium-light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':couple_with_heart_man_man_medium-light_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':couple_with_heart_man_man_medium-light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':couple_with_heart_man_man_medium-light_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':couple_with_heart_man_man_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':couple_with_heart_man_man_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':couple_with_heart_man_man_medium_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':couple_with_heart_man_man_medium_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':couple_with_heart_man_man_medium_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':couple_with_heart_man_man_medium_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':couple_with_heart_man_man_medium_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':couple_with_heart_man_man_medium_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':couple_with_heart_man_man_medium_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':couple_with_heart_man_man_medium_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F491\U0001F3FE': {
        'en' : u':couple_with_heart_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F491\U0001F3FC': {
        'en' : u':couple_with_heart_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F491\U0001F3FD': {
        'en' : u':couple_with_heart_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F9D1\U0001F3FB': {
        'en' : u':couple_with_heart_person_person_dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F9D1\U0001F3FB': {
        'en' : u':couple_with_heart_person_person_dark_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F9D1\U0001F3FE': {
        'en' : u':couple_with_heart_person_person_dark_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F9D1\U0001F3FE': {
        'en' : u':couple_with_heart_person_person_dark_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F9D1\U0001F3FC': {
        'en' : u':couple_with_heart_person_person_dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F9D1\U0001F3FC': {
        'en' : u':couple_with_heart_person_person_dark_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F9D1\U0001F3FD': {
        'en' : u':couple_with_heart_person_person_dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F9D1\U0001F3FD': {
        'en' : u':couple_with_heart_person_person_dark_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F9D1\U0001F3FF': {
        'en' : u':couple_with_heart_person_person_light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F9D1\U0001F3FF': {
        'en' : u':couple_with_heart_person_person_light_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F9D1\U0001F3FE': {
        'en' : u':couple_with_heart_person_person_light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F9D1\U0001F3FE': {
        'en' : u':couple_with_heart_person_person_light_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F9D1\U0001F3FC': {
        'en' : u':couple_with_heart_person_person_light_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F9D1\U0001F3FC': {
        'en' : u':couple_with_heart_person_person_light_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F9D1\U0001F3FD': {
        'en' : u':couple_with_heart_person_person_light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F9D1\U0001F3FD': {
        'en' : u':couple_with_heart_person_person_light_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F9D1\U0001F3FF': {
        'en' : u':couple_with_heart_person_person_medium-dark_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F9D1\U0001F3FF': {
        'en' : u':couple_with_heart_person_person_medium-dark_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F9D1\U0001F3FB': {
        'en' : u':couple_with_heart_person_person_medium-dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F9D1\U0001F3FB': {
        'en' : u':couple_with_heart_person_person_medium-dark_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F9D1\U0001F3FC': {
        'en' : u':couple_with_heart_person_person_medium-dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F9D1\U0001F3FC': {
        'en' : u':couple_with_heart_person_person_medium-dark_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F9D1\U0001F3FD': {
        'en' : u':couple_with_heart_person_person_medium-dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F9D1\U0001F3FD': {
        'en' : u':couple_with_heart_person_person_medium-dark_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F9D1\U0001F3FF': {
        'en' : u':couple_with_heart_person_person_medium-light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F9D1\U0001F3FF': {
        'en' : u':couple_with_heart_person_person_medium-light_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F9D1\U0001F3FB': {
        'en' : u':couple_with_heart_person_person_medium-light_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F9D1\U0001F3FB': {
        'en' : u':couple_with_heart_person_person_medium-light_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F9D1\U0001F3FE': {
        'en' : u':couple_with_heart_person_person_medium-light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F9D1\U0001F3FE': {
        'en' : u':couple_with_heart_person_person_medium-light_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F9D1\U0001F3FD': {
        'en' : u':couple_with_heart_person_person_medium-light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F9D1\U0001F3FD': {
        'en' : u':couple_with_heart_person_person_medium-light_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F9D1\U0001F3FF': {
        'en' : u':couple_with_heart_person_person_medium_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F9D1\U0001F3FF': {
        'en' : u':couple_with_heart_person_person_medium_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F9D1\U0001F3FB': {
        'en' : u':couple_with_heart_person_person_medium_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F9D1\U0001F3FB': {
        'en' : u':couple_with_heart_person_person_medium_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F9D1\U0001F3FE': {
        'en' : u':couple_with_heart_person_person_medium_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F9D1\U0001F3FE': {
        'en' : u':couple_with_heart_person_person_medium_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F9D1\U0001F3FC': {
        'en' : u':couple_with_heart_person_person_medium_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F9D1\U0001F3FC': {
        'en' : u':couple_with_heart_person_person_medium_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468': {
        'en' : u':couple_with_heart_woman_man:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F469\U0000200D\U00002764\U0000200D\U0001F468': {
        'en' : u':couple_with_heart_woman_man:',
        'status' : minimally_qualified,
        'E' : 2
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':couple_with_heart_woman_man_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':couple_with_heart_woman_man_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':couple_with_heart_woman_man_dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':couple_with_heart_woman_man_dark_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':couple_with_heart_woman_man_dark_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':couple_with_heart_woman_man_dark_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':couple_with_heart_woman_man_dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':couple_with_heart_woman_man_dark_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':couple_with_heart_woman_man_dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':couple_with_heart_woman_man_dark_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':couple_with_heart_woman_man_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':couple_with_heart_woman_man_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':couple_with_heart_woman_man_light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':couple_with_heart_woman_man_light_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':couple_with_heart_woman_man_light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':couple_with_heart_woman_man_light_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':couple_with_heart_woman_man_light_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':couple_with_heart_woman_man_light_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':couple_with_heart_woman_man_light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':couple_with_heart_woman_man_light_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':couple_with_heart_woman_man_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':couple_with_heart_woman_man_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':couple_with_heart_woman_man_medium-dark_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':couple_with_heart_woman_man_medium-dark_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':couple_with_heart_woman_man_medium-dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':couple_with_heart_woman_man_medium-dark_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':couple_with_heart_woman_man_medium-dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':couple_with_heart_woman_man_medium-dark_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':couple_with_heart_woman_man_medium-dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':couple_with_heart_woman_man_medium-dark_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':couple_with_heart_woman_man_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':couple_with_heart_woman_man_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':couple_with_heart_woman_man_medium-light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':couple_with_heart_woman_man_medium-light_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':couple_with_heart_woman_man_medium-light_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':couple_with_heart_woman_man_medium-light_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':couple_with_heart_woman_man_medium-light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':couple_with_heart_woman_man_medium-light_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':couple_with_heart_woman_man_medium-light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':couple_with_heart_woman_man_medium-light_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':couple_with_heart_woman_man_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':couple_with_heart_woman_man_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':couple_with_heart_woman_man_medium_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':couple_with_heart_woman_man_medium_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':couple_with_heart_woman_man_medium_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':couple_with_heart_woman_man_medium_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':couple_with_heart_woman_man_medium_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':couple_with_heart_woman_man_medium_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':couple_with_heart_woman_man_medium_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':couple_with_heart_woman_man_medium_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469': {
        'en' : u':couple_with_heart_woman_woman:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F469\U0000200D\U00002764\U0000200D\U0001F469': {
        'en' : u':couple_with_heart_woman_woman:',
        'status' : minimally_qualified,
        'E' : 2
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':couple_with_heart_woman_woman_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':couple_with_heart_woman_woman_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':couple_with_heart_woman_woman_dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':couple_with_heart_woman_woman_dark_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':couple_with_heart_woman_woman_dark_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':couple_with_heart_woman_woman_dark_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':couple_with_heart_woman_woman_dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':couple_with_heart_woman_woman_dark_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':couple_with_heart_woman_woman_dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':couple_with_heart_woman_woman_dark_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':couple_with_heart_woman_woman_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':couple_with_heart_woman_woman_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':couple_with_heart_woman_woman_light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':couple_with_heart_woman_woman_light_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':couple_with_heart_woman_woman_light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':couple_with_heart_woman_woman_light_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':couple_with_heart_woman_woman_light_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':couple_with_heart_woman_woman_light_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':couple_with_heart_woman_woman_light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':couple_with_heart_woman_woman_light_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':couple_with_heart_woman_woman_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':couple_with_heart_woman_woman_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':couple_with_heart_woman_woman_medium-dark_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':couple_with_heart_woman_woman_medium-dark_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':couple_with_heart_woman_woman_medium-dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':couple_with_heart_woman_woman_medium-dark_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':couple_with_heart_woman_woman_medium-dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':couple_with_heart_woman_woman_medium-dark_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':couple_with_heart_woman_woman_medium-dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':couple_with_heart_woman_woman_medium-dark_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':couple_with_heart_woman_woman_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':couple_with_heart_woman_woman_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':couple_with_heart_woman_woman_medium-light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':couple_with_heart_woman_woman_medium-light_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':couple_with_heart_woman_woman_medium-light_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':couple_with_heart_woman_woman_medium-light_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':couple_with_heart_woman_woman_medium-light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':couple_with_heart_woman_woman_medium-light_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':couple_with_heart_woman_woman_medium-light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':couple_with_heart_woman_woman_medium-light_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':couple_with_heart_woman_woman_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':couple_with_heart_woman_woman_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':couple_with_heart_woman_woman_medium_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':couple_with_heart_woman_woman_medium_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':couple_with_heart_woman_woman_medium_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':couple_with_heart_woman_woman_medium_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':couple_with_heart_woman_woman_medium_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':couple_with_heart_woman_woman_medium_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':couple_with_heart_woman_woman_medium_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':couple_with_heart_woman_woman_medium_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F404': {
        'en' : u':cow:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F42E': {
        'en' : u':cow_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F920': {
        'en' : u':cowboy_hat_face:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F980': {
        'en' : u':crab:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F58D\U0000FE0F': {
        'en' : u':crayon:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F58D': {
        'en' : u':crayon:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F4B3': {
        'en' : u':credit_card:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F319': {
        'en' : u':crescent_moon:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F997': {
        'en' : u':cricket:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F3CF': {
        'en' : u':cricket_game:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F40A': {
        'en' : u':crocodile:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F950': {
        'en' : u':croissant:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0000274C': {
        'en' : u':cross_mark:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0000274E': {
        'en' : u':cross_mark_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F91E': {
        'en' : u':crossed_fingers:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F91E\U0001F3FF': {
        'en' : u':crossed_fingers_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F91E\U0001F3FB': {
        'en' : u':crossed_fingers_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F91E\U0001F3FE': {
        'en' : u':crossed_fingers_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F91E\U0001F3FC': {
        'en' : u':crossed_fingers_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F91E\U0001F3FD': {
        'en' : u':crossed_fingers_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F38C': {
        'en' : u':crossed_flags:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00002694\U0000FE0F': {
        'en' : u':crossed_swords:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U00002694': {
        'en' : u':crossed_swords:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0001F451': {
        'en' : u':crown:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FA7C': {
        'en' : u':crutch:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F63F': {
        'en' : u':crying_cat:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F622': {
        'en' : u':crying_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F52E': {
        'en' : u':crystal_ball:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F952': {
        'en' : u':cucumber:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F964': {
        'en' : u':cup_with_straw:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9C1': {
        'en' : u':cupcake:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F94C': {
        'en' : u':curling_stone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9B1': {
        'en' : u':curly_hair:',
        'status' : component,
        'E' : 11
    },
    u'\U000027B0': {
        'en' : u':curly_loop:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4B1': {
        'en' : u':currency_exchange:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F35B': {
        'en' : u':curry_rice:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F36E': {
        'en' : u':custard:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F6C3': {
        'en' : u':customs:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F969': {
        'en' : u':cut_of_meat:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F300': {
        'en' : u':cyclone:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F5E1\U0000FE0F': {
        'en' : u':dagger:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5E1': {
        'en' : u':dagger:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F361': {
        'en' : u':dango:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3FF': {
        'en' : u':dark_skin_tone:',
        'status' : component,
        'E' : 1
    },
    u'\U0001F4A8': {
        'en' : u':dashing_away:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9CF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':deaf_man:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0000200D\U00002642': {
        'en' : u':deaf_man:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':deaf_man_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FF\U0000200D\U00002642': {
        'en' : u':deaf_man_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':deaf_man_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FB\U0000200D\U00002642': {
        'en' : u':deaf_man_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':deaf_man_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FE\U0000200D\U00002642': {
        'en' : u':deaf_man_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':deaf_man_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FC\U0000200D\U00002642': {
        'en' : u':deaf_man_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':deaf_man_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FD\U0000200D\U00002642': {
        'en' : u':deaf_man_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CF': {
        'en' : u':deaf_person:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FF': {
        'en' : u':deaf_person_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FB': {
        'en' : u':deaf_person_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FE': {
        'en' : u':deaf_person_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FC': {
        'en' : u':deaf_person_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FD': {
        'en' : u':deaf_person_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':deaf_woman:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0000200D\U00002640': {
        'en' : u':deaf_woman:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':deaf_woman_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FF\U0000200D\U00002640': {
        'en' : u':deaf_woman_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':deaf_woman_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FB\U0000200D\U00002640': {
        'en' : u':deaf_woman_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':deaf_woman_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FE\U0000200D\U00002640': {
        'en' : u':deaf_woman_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':deaf_woman_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FC\U0000200D\U00002640': {
        'en' : u':deaf_woman_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':deaf_woman_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CF\U0001F3FD\U0000200D\U00002640': {
        'en' : u':deaf_woman_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F333': {
        'en' : u':deciduous_tree:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F98C': {
        'en' : u':deer:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F69A': {
        'en' : u':delivery_truck:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3EC': {
        'en' : u':department_store:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3DA\U0000FE0F': {
        'en' : u':derelict_house:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3DA': {
        'en' : u':derelict_house:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3DC\U0000FE0F': {
        'en' : u':desert:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3DC': {
        'en' : u':desert:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3DD\U0000FE0F': {
        'en' : u':desert_island:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3DD': {
        'en' : u':desert_island:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5A5\U0000FE0F': {
        'en' : u':desktop_computer:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5A5': {
        'en' : u':desktop_computer:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F575\U0000FE0F': {
        'en' : u':detective:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F575': {
        'en' : u':detective:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F575\U0001F3FF': {
        'en' : u':detective_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F575\U0001F3FB': {
        'en' : u':detective_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F575\U0001F3FE': {
        'en' : u':detective_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F575\U0001F3FC': {
        'en' : u':detective_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F575\U0001F3FD': {
        'en' : u':detective_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U00002666\U0000FE0F': {
        'en' : u':diamond_suit:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002666': {
        'en' : u':diamond_suit:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F4A0': {
        'en' : u':diamond_with_a_dot:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F505': {
        'en' : u':dim_button:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F61E': {
        'en' : u':disappointed_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F978': {
        'en' : u':disguised_face:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U00002797': {
        'en' : u':divide:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F93F': {
        'en' : u':diving_mask:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001FA94': {
        'en' : u':diya_lamp:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F4AB': {
        'en' : u':dizzy:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9EC': {
        'en' : u':dna:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9A4': {
        'en' : u':dodo:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F415': {
        'en' : u':dog:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F436': {
        'en' : u':dog_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4B5': {
        'en' : u':dollar_banknote:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F42C': {
        'en' : u':dolphin:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F6AA': {
        'en' : u':door:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FAE5': {
        'en' : u':dotted_line_face:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F52F': {
        'en' : u':dotted_six-pointed_star:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U000027BF': {
        'en' : u':double_curly_loop:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000203C\U0000FE0F': {
        'en' : u':double_exclamation_mark:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0000203C': {
        'en' : u':double_exclamation_mark:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F369': {
        'en' : u':doughnut:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F54A\U0000FE0F': {
        'en' : u':dove:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F54A': {
        'en' : u':dove:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U00002199\U0000FE0F': {
        'en' : u':down-left_arrow:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002199': {
        'en' : u':down-left_arrow:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002198\U0000FE0F': {
        'en' : u':down-right_arrow:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002198': {
        'en' : u':down-right_arrow:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002B07\U0000FE0F': {
        'en' : u':down_arrow:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002B07': {
        'en' : u':down_arrow:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F613': {
        'en' : u':downcast_face_with_sweat:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F53D': {
        'en' : u':downwards_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F409': {
        'en' : u':dragon:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F432': {
        'en' : u':dragon_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F457': {
        'en' : u':dress:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F924': {
        'en' : u':drooling_face:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001FA78': {
        'en' : u':drop_of_blood:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F4A7': {
        'en' : u':droplet:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F941': {
        'en' : u':drum:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F986': {
        'en' : u':duck:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F95F': {
        'en' : u':dumpling:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F4C0': {
        'en' : u':dvd:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4E7': {
        'en' : u':e-mail:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F985': {
        'en' : u':eagle:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F442': {
        'en' : u':ear:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F442\U0001F3FF': {
        'en' : u':ear_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F442\U0001F3FB': {
        'en' : u':ear_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F442\U0001F3FE': {
        'en' : u':ear_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F442\U0001F3FC': {
        'en' : u':ear_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F442\U0001F3FD': {
        'en' : u':ear_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F33D': {
        'en' : u':ear_of_corn:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9BB': {
        'en' : u':ear_with_hearing_aid:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9BB\U0001F3FF': {
        'en' : u':ear_with_hearing_aid_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9BB\U0001F3FB': {
        'en' : u':ear_with_hearing_aid_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9BB\U0001F3FE': {
        'en' : u':ear_with_hearing_aid_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9BB\U0001F3FC': {
        'en' : u':ear_with_hearing_aid_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9BB\U0001F3FD': {
        'en' : u':ear_with_hearing_aid_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F95A': {
        'en' : u':egg:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F346': {
        'en' : u':eggplant:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00002734\U0000FE0F': {
        'en' : u':eight-pointed_star:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002734': {
        'en' : u':eight-pointed_star:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002733\U0000FE0F': {
        'en' : u':eight-spoked_asterisk:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002733': {
        'en' : u':eight-spoked_asterisk:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F563': {
        'en' : u':eight-thirty:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F557': {
        'en' : u':eight_o’clock:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000023CF\U0000FE0F': {
        'en' : u':eject_button:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U000023CF': {
        'en' : u':eject_button:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0001F50C': {
        'en' : u':electric_plug:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F418': {
        'en' : u':elephant:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F6D7': {
        'en' : u':elevator:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F566': {
        'en' : u':eleven-thirty:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F55A': {
        'en' : u':eleven_o’clock:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F9DD': {
        'en' : u':elf:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FF': {
        'en' : u':elf_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FB': {
        'en' : u':elf_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FE': {
        'en' : u':elf_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FC': {
        'en' : u':elf_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FD': {
        'en' : u':elf_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001FAB9': {
        'en' : u':empty_nest:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U00002709\U0000FE0F': {
        'en' : u':envelope:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002709': {
        'en' : u':envelope:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F4E9': {
        'en' : u':envelope_with_arrow:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4B6': {
        'en' : u':euro_banknote:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F332': {
        'en' : u':evergreen_tree:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F411': {
        'en' : u':ewe:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00002049\U0000FE0F': {
        'en' : u':exclamation_question_mark:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002049': {
        'en' : u':exclamation_question_mark:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F92F': {
        'en' : u':exploding_head:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F611': {
        'en' : u':expressionless_face:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F441\U0000FE0F': {
        'en' : u':eye:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F441': {
        'en' : u':eye:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F441\U0000FE0F\U0000200D\U0001F5E8\U0000FE0F': {
        'en' : u':eye_in_speech_bubble:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F441\U0000200D\U0001F5E8\U0000FE0F': {
        'en' : u':eye_in_speech_bubble:',
        'status' : unqualified,
        'E' : 2
    },
    u'\U0001F441\U0000FE0F\U0000200D\U0001F5E8': {
        'en' : u':eye_in_speech_bubble:',
        'status' : unqualified,
        'E' : 2
    },
    u'\U0001F441\U0000200D\U0001F5E8': {
        'en' : u':eye_in_speech_bubble:',
        'status' : unqualified,
        'E' : 2
    },
    u'\U0001F440': {
        'en' : u':eyes:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F618': {
        'en' : u':face_blowing_a_kiss:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F62E\U0000200D\U0001F4A8': {
        'en' : u':face_exhaling:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F979': {
        'en' : u':face_holding_back_tears:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F636\U0000200D\U0001F32B\U0000FE0F': {
        'en' : u':face_in_clouds:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F636\U0000200D\U0001F32B': {
        'en' : u':face_in_clouds:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F60B': {
        'en' : u':face_savoring_food:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F631': {
        'en' : u':face_screaming_in_fear:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F92E': {
        'en' : u':face_vomiting:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F635': {
        'en' : u':face_with_crossed-out_eyes:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FAE4': {
        'en' : u':face_with_diagonal_mouth:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F92D': {
        'en' : u':face_with_hand_over_mouth:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F915': {
        'en' : u':face_with_head-bandage:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F637': {
        'en' : u':face_with_medical_mask:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9D0': {
        'en' : u':face_with_monocle:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001FAE2': {
        'en' : u':face_with_open_eyes_and_hand_over_mouth:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F62E': {
        'en' : u':face_with_open_mouth:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001FAE3': {
        'en' : u':face_with_peeking_eye:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F928': {
        'en' : u':face_with_raised_eyebrow:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F644': {
        'en' : u':face_with_rolling_eyes:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F635\U0000200D\U0001F4AB': {
        'en' : u':face_with_spiral_eyes:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F624': {
        'en' : u':face_with_steam_from_nose:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F92C': {
        'en' : u':face_with_symbols_on_mouth:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F602': {
        'en' : u':face_with_tears_of_joy:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F912': {
        'en' : u':face_with_thermometer:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F61B': {
        'en' : u':face_with_tongue:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F636': {
        'en' : u':face_without_mouth:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3ED': {
        'en' : u':factory:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F9D1\U0000200D\U0001F3ED': {
        'en' : u':factory_worker:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F3ED': {
        'en' : u':factory_worker_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F3ED': {
        'en' : u':factory_worker_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F3ED': {
        'en' : u':factory_worker_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F3ED': {
        'en' : u':factory_worker_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F3ED': {
        'en' : u':factory_worker_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9DA': {
        'en' : u':fairy:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FF': {
        'en' : u':fairy_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FB': {
        'en' : u':fairy_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FE': {
        'en' : u':fairy_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FC': {
        'en' : u':fairy_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FD': {
        'en' : u':fairy_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9C6': {
        'en' : u':falafel:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F342': {
        'en' : u':fallen_leaf:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F46A': {
        'en' : u':family:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F468\U0000200D\U0001F466': {
        'en' : u':family_man_boy:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U0001F466\U0000200D\U0001F466': {
        'en' : u':family_man_boy_boy:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U0001F467': {
        'en' : u':family_man_girl:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U0001F467\U0000200D\U0001F466': {
        'en' : u':family_man_girl_boy:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U0001F467\U0000200D\U0001F467': {
        'en' : u':family_man_girl_girl:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U0001F468\U0000200D\U0001F466': {
        'en' : u':family_man_man_boy:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F468\U0000200D\U0001F468\U0000200D\U0001F466\U0000200D\U0001F466': {
        'en' : u':family_man_man_boy_boy:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F468\U0000200D\U0001F468\U0000200D\U0001F467': {
        'en' : u':family_man_man_girl:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F468\U0000200D\U0001F468\U0000200D\U0001F467\U0000200D\U0001F466': {
        'en' : u':family_man_man_girl_boy:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F468\U0000200D\U0001F468\U0000200D\U0001F467\U0000200D\U0001F467': {
        'en' : u':family_man_man_girl_girl:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F468\U0000200D\U0001F469\U0000200D\U0001F466': {
        'en' : u':family_man_woman_boy:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F468\U0000200D\U0001F469\U0000200D\U0001F466\U0000200D\U0001F466': {
        'en' : u':family_man_woman_boy_boy:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F468\U0000200D\U0001F469\U0000200D\U0001F467': {
        'en' : u':family_man_woman_girl:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F468\U0000200D\U0001F469\U0000200D\U0001F467\U0000200D\U0001F466': {
        'en' : u':family_man_woman_girl_boy:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F468\U0000200D\U0001F469\U0000200D\U0001F467\U0000200D\U0001F467': {
        'en' : u':family_man_woman_girl_girl:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F469\U0000200D\U0001F466': {
        'en' : u':family_woman_boy:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U0001F466\U0000200D\U0001F466': {
        'en' : u':family_woman_boy_boy:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U0001F467': {
        'en' : u':family_woman_girl:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U0001F467\U0000200D\U0001F466': {
        'en' : u':family_woman_girl_boy:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U0001F467\U0000200D\U0001F467': {
        'en' : u':family_woman_girl_girl:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U0001F469\U0000200D\U0001F466': {
        'en' : u':family_woman_woman_boy:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F469\U0000200D\U0001F469\U0000200D\U0001F466\U0000200D\U0001F466': {
        'en' : u':family_woman_woman_boy_boy:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F469\U0000200D\U0001F469\U0000200D\U0001F467': {
        'en' : u':family_woman_woman_girl:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F469\U0000200D\U0001F469\U0000200D\U0001F467\U0000200D\U0001F466': {
        'en' : u':family_woman_woman_girl_boy:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F469\U0000200D\U0001F469\U0000200D\U0001F467\U0000200D\U0001F467': {
        'en' : u':family_woman_woman_girl_girl:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F9D1\U0000200D\U0001F33E': {
        'en' : u':farmer:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F33E': {
        'en' : u':farmer_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F33E': {
        'en' : u':farmer_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F33E': {
        'en' : u':farmer_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F33E': {
        'en' : u':farmer_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F33E': {
        'en' : u':farmer_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U000023E9': {
        'en' : u':fast-forward_button:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000023EC': {
        'en' : u':fast_down_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U000023EA': {
        'en' : u':fast_reverse_button:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000023EB': {
        'en' : u':fast_up_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4E0': {
        'en' : u':fax_machine:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F628': {
        'en' : u':fearful_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FAB6': {
        'en' : u':feather:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U00002640\U0000FE0F': {
        'en' : u':female_sign:',
        'status' : fully_qualified,
        'E' : 4,
        'variant': True,
    },
    u'\U00002640': {
        'en' : u':female_sign:',
        'status' : unqualified,
        'E' : 4,
        'variant': True,
    },
    u'\U0001F3A1': {
        'en' : u':ferris_wheel:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U000026F4\U0000FE0F': {
        'en' : u':ferry:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000026F4': {
        'en' : u':ferry:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3D1': {
        'en' : u':field_hockey:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F5C4\U0000FE0F': {
        'en' : u':file_cabinet:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5C4': {
        'en' : u':file_cabinet:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F4C1': {
        'en' : u':file_folder:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F39E\U0000FE0F': {
        'en' : u':film_frames:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F39E': {
        'en' : u':film_frames:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F4FD\U0000FE0F': {
        'en' : u':film_projector:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F4FD': {
        'en' : u':film_projector:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F525': {
        'en' : u':fire:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F692': {
        'en' : u':fire_engine:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9EF': {
        'en' : u':fire_extinguisher:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9E8': {
        'en' : u':firecracker:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9D1\U0000200D\U0001F692': {
        'en' : u':firefighter:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F692': {
        'en' : u':firefighter_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F692': {
        'en' : u':firefighter_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F692': {
        'en' : u':firefighter_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F692': {
        'en' : u':firefighter_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F692': {
        'en' : u':firefighter_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F386': {
        'en' : u':fireworks:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F313': {
        'en' : u':first_quarter_moon:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F31B': {
        'en' : u':first_quarter_moon_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F41F': {
        'en' : u':fish:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F365': {
        'en' : u':fish_cake_with_swirl:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3A3': {
        'en' : u':fishing_pole:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F560': {
        'en' : u':five-thirty:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F554': {
        'en' : u':five_o’clock:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000026F3': {
        'en' : u':flag_in_hole:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F9A9': {
        'en' : u':flamingo:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F526': {
        'en' : u':flashlight:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F97F': {
        'en' : u':flat_shoe:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001FAD3': {
        'en' : u':flatbread:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0000269C\U0000FE0F': {
        'en' : u':fleur-de-lis:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0000269C': {
        'en' : u':fleur-de-lis:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0001F4AA': {
        'en' : u':flexed_biceps:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4AA\U0001F3FF': {
        'en' : u':flexed_biceps_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F4AA\U0001F3FB': {
        'en' : u':flexed_biceps_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F4AA\U0001F3FE': {
        'en' : u':flexed_biceps_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F4AA\U0001F3FC': {
        'en' : u':flexed_biceps_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F4AA\U0001F3FD': {
        'en' : u':flexed_biceps_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F4BE': {
        'en' : u':floppy_disk:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3B4': {
        'en' : u':flower_playing_cards:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F633': {
        'en' : u':flushed_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FAB0': {
        'en' : u':fly:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F94F': {
        'en' : u':flying_disc:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F6F8': {
        'en' : u':flying_saucer:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F32B\U0000FE0F': {
        'en' : u':fog:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F32B': {
        'en' : u':fog:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F301': {
        'en' : u':foggy:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F64F': {
        'en' : u':folded_hands:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F64F\U0001F3FF': {
        'en' : u':folded_hands_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64F\U0001F3FB': {
        'en' : u':folded_hands_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64F\U0001F3FE': {
        'en' : u':folded_hands_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64F\U0001F3FC': {
        'en' : u':folded_hands_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64F\U0001F3FD': {
        'en' : u':folded_hands_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001FAD5': {
        'en' : u':fondue:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F9B6': {
        'en' : u':foot:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B6\U0001F3FF': {
        'en' : u':foot_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B6\U0001F3FB': {
        'en' : u':foot_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B6\U0001F3FE': {
        'en' : u':foot_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B6\U0001F3FC': {
        'en' : u':foot_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B6\U0001F3FD': {
        'en' : u':foot_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F463': {
        'en' : u':footprints:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F374': {
        'en' : u':fork_and_knife:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F37D\U0000FE0F': {
        'en' : u':fork_and_knife_with_plate:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F37D': {
        'en' : u':fork_and_knife_with_plate:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F960': {
        'en' : u':fortune_cookie:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U000026F2': {
        'en' : u':fountain:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F58B\U0000FE0F': {
        'en' : u':fountain_pen:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F58B': {
        'en' : u':fountain_pen:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F55F': {
        'en' : u':four-thirty:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F340': {
        'en' : u':four_leaf_clover:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F553': {
        'en' : u':four_o’clock:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F98A': {
        'en' : u':fox:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F5BC\U0000FE0F': {
        'en' : u':framed_picture:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5BC': {
        'en' : u':framed_picture:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F35F': {
        'en' : u':french_fries:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F364': {
        'en' : u':fried_shrimp:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F438': {
        'en' : u':frog:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F425': {
        'en' : u':front-facing_baby_chick:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00002639\U0000FE0F': {
        'en' : u':frowning_face:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U00002639': {
        'en' : u':frowning_face:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F626': {
        'en' : u':frowning_face_with_open_mouth:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U000026FD': {
        'en' : u':fuel_pump:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F315': {
        'en' : u':full_moon:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F31D': {
        'en' : u':full_moon_face:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U000026B1\U0000FE0F': {
        'en' : u':funeral_urn:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U000026B1': {
        'en' : u':funeral_urn:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0001F3B2': {
        'en' : u':game_die:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9C4': {
        'en' : u':garlic:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U00002699\U0000FE0F': {
        'en' : u':gear:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U00002699': {
        'en' : u':gear:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0001F48E': {
        'en' : u':gem_stone:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9DE': {
        'en' : u':genie:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F47B': {
        'en' : u':ghost:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F992': {
        'en' : u':giraffe:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F467': {
        'en' : u':girl:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F467\U0001F3FF': {
        'en' : u':girl_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F467\U0001F3FB': {
        'en' : u':girl_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F467\U0001F3FE': {
        'en' : u':girl_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F467\U0001F3FC': {
        'en' : u':girl_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F467\U0001F3FD': {
        'en' : u':girl_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F95B': {
        'en' : u':glass_of_milk:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F453': {
        'en' : u':glasses:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F30E': {
        'en' : u':globe_showing_Americas:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F30F': {
        'en' : u':globe_showing_Asia-Australia:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F30D': {
        'en' : u':globe_showing_Europe-Africa:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F310': {
        'en' : u':globe_with_meridians:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F9E4': {
        'en' : u':gloves:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F31F': {
        'en' : u':glowing_star:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F945': {
        'en' : u':goal_net:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F410': {
        'en' : u':goat:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F47A': {
        'en' : u':goblin:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F97D': {
        'en' : u':goggles:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F98D': {
        'en' : u':gorilla:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F393': {
        'en' : u':graduation_cap:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F347': {
        'en' : u':grapes:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F34F': {
        'en' : u':green_apple:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4D7': {
        'en' : u':green_book:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F7E2': {
        'en' : u':green_circle:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F49A': {
        'en' : u':green_heart:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F957': {
        'en' : u':green_salad:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F7E9': {
        'en' : u':green_square:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F62C': {
        'en' : u':grimacing_face:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F63A': {
        'en' : u':grinning_cat:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F638': {
        'en' : u':grinning_cat_with_smiling_eyes:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F600': {
        'en' : u':grinning_face:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F603': {
        'en' : u':grinning_face_with_big_eyes:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F604': {
        'en' : u':grinning_face_with_smiling_eyes:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F605': {
        'en' : u':grinning_face_with_sweat:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F606': {
        'en' : u':grinning_squinting_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F497': {
        'en' : u':growing_heart:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F482': {
        'en' : u':guard:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F482\U0001F3FF': {
        'en' : u':guard_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F482\U0001F3FB': {
        'en' : u':guard_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F482\U0001F3FE': {
        'en' : u':guard_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F482\U0001F3FC': {
        'en' : u':guard_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F482\U0001F3FD': {
        'en' : u':guard_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F9AE': {
        'en' : u':guide_dog:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F3B8': {
        'en' : u':guitar:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F354': {
        'en' : u':hamburger:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F528': {
        'en' : u':hammer:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00002692\U0000FE0F': {
        'en' : u':hammer_and_pick:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U00002692': {
        'en' : u':hammer_and_pick:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0001F6E0\U0000FE0F': {
        'en' : u':hammer_and_wrench:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6E0': {
        'en' : u':hammer_and_wrench:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001FAAC': {
        'en' : u':hamsa:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F439': {
        'en' : u':hamster:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F590\U0000FE0F': {
        'en' : u':hand_with_fingers_splayed:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F590': {
        'en' : u':hand_with_fingers_splayed:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F590\U0001F3FF': {
        'en' : u':hand_with_fingers_splayed_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F590\U0001F3FB': {
        'en' : u':hand_with_fingers_splayed_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F590\U0001F3FE': {
        'en' : u':hand_with_fingers_splayed_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F590\U0001F3FC': {
        'en' : u':hand_with_fingers_splayed_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F590\U0001F3FD': {
        'en' : u':hand_with_fingers_splayed_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001FAF0': {
        'en' : u':hand_with_index_finger_and_thumb_crossed:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF0\U0001F3FF': {
        'en' : u':hand_with_index_finger_and_thumb_crossed_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF0\U0001F3FB': {
        'en' : u':hand_with_index_finger_and_thumb_crossed_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF0\U0001F3FE': {
        'en' : u':hand_with_index_finger_and_thumb_crossed_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF0\U0001F3FC': {
        'en' : u':hand_with_index_finger_and_thumb_crossed_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF0\U0001F3FD': {
        'en' : u':hand_with_index_finger_and_thumb_crossed_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F45C': {
        'en' : u':handbag:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F91D': {
        'en' : u':handshake:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F91D\U0001F3FF': {
        'en' : u':handshake_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001FAF1\U0001F3FF\U0000200D\U0001FAF2\U0001F3FB': {
        'en' : u':handshake_dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF1\U0001F3FF\U0000200D\U0001FAF2\U0001F3FE': {
        'en' : u':handshake_dark_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF1\U0001F3FF\U0000200D\U0001FAF2\U0001F3FC': {
        'en' : u':handshake_dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF1\U0001F3FF\U0000200D\U0001FAF2\U0001F3FD': {
        'en' : u':handshake_dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F91D\U0001F3FB': {
        'en' : u':handshake_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001FAF1\U0001F3FB\U0000200D\U0001FAF2\U0001F3FF': {
        'en' : u':handshake_light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF1\U0001F3FB\U0000200D\U0001FAF2\U0001F3FE': {
        'en' : u':handshake_light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF1\U0001F3FB\U0000200D\U0001FAF2\U0001F3FC': {
        'en' : u':handshake_light_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF1\U0001F3FB\U0000200D\U0001FAF2\U0001F3FD': {
        'en' : u':handshake_light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F91D\U0001F3FE': {
        'en' : u':handshake_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001FAF1\U0001F3FE\U0000200D\U0001FAF2\U0001F3FF': {
        'en' : u':handshake_medium-dark_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF1\U0001F3FE\U0000200D\U0001FAF2\U0001F3FB': {
        'en' : u':handshake_medium-dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF1\U0001F3FE\U0000200D\U0001FAF2\U0001F3FC': {
        'en' : u':handshake_medium-dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF1\U0001F3FE\U0000200D\U0001FAF2\U0001F3FD': {
        'en' : u':handshake_medium-dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F91D\U0001F3FC': {
        'en' : u':handshake_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001FAF1\U0001F3FC\U0000200D\U0001FAF2\U0001F3FF': {
        'en' : u':handshake_medium-light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF1\U0001F3FC\U0000200D\U0001FAF2\U0001F3FB': {
        'en' : u':handshake_medium-light_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF1\U0001F3FC\U0000200D\U0001FAF2\U0001F3FE': {
        'en' : u':handshake_medium-light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF1\U0001F3FC\U0000200D\U0001FAF2\U0001F3FD': {
        'en' : u':handshake_medium-light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F91D\U0001F3FD': {
        'en' : u':handshake_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001FAF1\U0001F3FD\U0000200D\U0001FAF2\U0001F3FF': {
        'en' : u':handshake_medium_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF1\U0001F3FD\U0000200D\U0001FAF2\U0001F3FB': {
        'en' : u':handshake_medium_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF1\U0001F3FD\U0000200D\U0001FAF2\U0001F3FE': {
        'en' : u':handshake_medium_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF1\U0001F3FD\U0000200D\U0001FAF2\U0001F3FC': {
        'en' : u':handshake_medium_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F423': {
        'en' : u':hatching_chick:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3A7': {
        'en' : u':headphone:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001FAA6': {
        'en' : u':headstone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F9D1\U0000200D\U00002695\U0000FE0F': {
        'en' : u':health_worker:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0000200D\U00002695': {
        'en' : u':health_worker:',
        'status' : minimally_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002695\U0000FE0F': {
        'en' : u':health_worker_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002695': {
        'en' : u':health_worker_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002695\U0000FE0F': {
        'en' : u':health_worker_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002695': {
        'en' : u':health_worker_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002695\U0000FE0F': {
        'en' : u':health_worker_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002695': {
        'en' : u':health_worker_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002695\U0000FE0F': {
        'en' : u':health_worker_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002695': {
        'en' : u':health_worker_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002695\U0000FE0F': {
        'en' : u':health_worker_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002695': {
        'en' : u':health_worker_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12.1
    },
    u'\U0001F649': {
        'en' : u':hear-no-evil_monkey:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F49F': {
        'en' : u':heart_decoration:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00002763\U0000FE0F': {
        'en' : u':heart_exclamation:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U00002763': {
        'en' : u':heart_exclamation:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0001FAF6': {
        'en' : u':heart_hands:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF6\U0001F3FF': {
        'en' : u':heart_hands_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF6\U0001F3FB': {
        'en' : u':heart_hands_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF6\U0001F3FE': {
        'en' : u':heart_hands_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF6\U0001F3FC': {
        'en' : u':heart_hands_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF6\U0001F3FD': {
        'en' : u':heart_hands_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U00002764\U0000FE0F\U0000200D\U0001F525': {
        'en' : u':heart_on_fire:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U00002764\U0000200D\U0001F525': {
        'en' : u':heart_on_fire:',
        'status' : unqualified,
        'E' : 13.1
    },
    u'\U00002665\U0000FE0F': {
        'en' : u':heart_suit:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002665': {
        'en' : u':heart_suit:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F498': {
        'en' : u':heart_with_arrow:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F49D': {
        'en' : u':heart_with_ribbon:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4B2': {
        'en' : u':heavy_dollar_sign:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F7F0': {
        'en' : u':heavy_equals_sign:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F994': {
        'en' : u':hedgehog:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F681': {
        'en' : u':helicopter:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F33F': {
        'en' : u':herb:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F33A': {
        'en' : u':hibiscus:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F460': {
        'en' : u':high-heeled_shoe:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F684': {
        'en' : u':high-speed_train:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U000026A1': {
        'en' : u':high_voltage:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F97E': {
        'en' : u':hiking_boot:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F6D5': {
        'en' : u':hindu_temple:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F99B': {
        'en' : u':hippopotamus:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F573\U0000FE0F': {
        'en' : u':hole:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F573': {
        'en' : u':hole:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U00002B55': {
        'en' : u':hollow_red_circle:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F36F': {
        'en' : u':honey_pot:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F41D': {
        'en' : u':honeybee:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FA9D': {
        'en' : u':hook:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F6A5': {
        'en' : u':horizontal_traffic_light:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F40E': {
        'en' : u':horse:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F434': {
        'en' : u':horse_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3C7': {
        'en' : u':horse_racing:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3C7\U0001F3FF': {
        'en' : u':horse_racing_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3C7\U0001F3FB': {
        'en' : u':horse_racing_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3C7\U0001F3FE': {
        'en' : u':horse_racing_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3C7\U0001F3FC': {
        'en' : u':horse_racing_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3C7\U0001F3FD': {
        'en' : u':horse_racing_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3E5': {
        'en' : u':hospital:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00002615': {
        'en' : u':hot_beverage:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F32D': {
        'en' : u':hot_dog:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F975': {
        'en' : u':hot_face:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F336\U0000FE0F': {
        'en' : u':hot_pepper:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F336': {
        'en' : u':hot_pepper:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U00002668\U0000FE0F': {
        'en' : u':hot_springs:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002668': {
        'en' : u':hot_springs:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F3E8': {
        'en' : u':hotel:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0000231B': {
        'en' : u':hourglass_done:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000023F3': {
        'en' : u':hourglass_not_done:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F3E0': {
        'en' : u':house:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F3E1': {
        'en' : u':house_with_garden:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3D8\U0000FE0F': {
        'en' : u':houses:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3D8': {
        'en' : u':houses:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F4AF': {
        'en' : u':hundred_points:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F62F': {
        'en' : u':hushed_face:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6D6': {
        'en' : u':hut:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F9CA': {
        'en' : u':ice:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F368': {
        'en' : u':ice_cream:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3D2': {
        'en' : u':ice_hockey:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U000026F8\U0000FE0F': {
        'en' : u':ice_skate:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000026F8': {
        'en' : u':ice_skate:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001FAAA': {
        'en' : u':identification_card:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F4E5': {
        'en' : u':inbox_tray:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F4E8': {
        'en' : u':incoming_envelope:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FAF5': {
        'en' : u':index_pointing_at_the_viewer:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF5\U0001F3FF': {
        'en' : u':index_pointing_at_the_viewer_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF5\U0001F3FB': {
        'en' : u':index_pointing_at_the_viewer_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF5\U0001F3FE': {
        'en' : u':index_pointing_at_the_viewer_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF5\U0001F3FC': {
        'en' : u':index_pointing_at_the_viewer_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF5\U0001F3FD': {
        'en' : u':index_pointing_at_the_viewer_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0000261D\U0000FE0F': {
        'en' : u':index_pointing_up:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0000261D': {
        'en' : u':index_pointing_up:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0000261D\U0001F3FF': {
        'en' : u':index_pointing_up_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000261D\U0001F3FB': {
        'en' : u':index_pointing_up_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000261D\U0001F3FE': {
        'en' : u':index_pointing_up_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000261D\U0001F3FC': {
        'en' : u':index_pointing_up_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000261D\U0001F3FD': {
        'en' : u':index_pointing_up_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000267E\U0000FE0F': {
        'en' : u':infinity:',
        'status' : fully_qualified,
        'E' : 11,
        'variant': True,
    },
    u'\U0000267E': {
        'en' : u':infinity:',
        'status' : unqualified,
        'E' : 11,
        'variant': True,
    },
    u'\U00002139\U0000FE0F': {
        'en' : u':information:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002139': {
        'en' : u':information:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F524': {
        'en' : u':input_latin_letters:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F521': {
        'en' : u':input_latin_lowercase:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F520': {
        'en' : u':input_latin_uppercase:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F522': {
        'en' : u':input_numbers:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F523': {
        'en' : u':input_symbols:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F383': {
        'en' : u':jack-o-lantern:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FAD9': {
        'en' : u':jar:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F456': {
        'en' : u':jeans:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F0CF': {
        'en' : u':joker:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F579\U0000FE0F': {
        'en' : u':joystick:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F579': {
        'en' : u':joystick:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F9D1\U0000200D\U00002696\U0000FE0F': {
        'en' : u':judge:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0000200D\U00002696': {
        'en' : u':judge:',
        'status' : minimally_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002696\U0000FE0F': {
        'en' : u':judge_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002696': {
        'en' : u':judge_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002696\U0000FE0F': {
        'en' : u':judge_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002696': {
        'en' : u':judge_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002696\U0000FE0F': {
        'en' : u':judge_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002696': {
        'en' : u':judge_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002696\U0000FE0F': {
        'en' : u':judge_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002696': {
        'en' : u':judge_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002696\U0000FE0F': {
        'en' : u':judge_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002696': {
        'en' : u':judge_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12.1
    },
    u'\U0001F54B': {
        'en' : u':kaaba:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F998': {
        'en' : u':kangaroo:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F511': {
        'en' : u':key:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00002328\U0000FE0F': {
        'en' : u':keyboard:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U00002328': {
        'en' : u':keyboard:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U00000023\U0000FE0F\U000020E3': {
        'en' : u':keycap_#:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00000023\U000020E3': {
        'en' : u':keycap_#:',
        'status' : unqualified,
        'E' : 0.6
    },
    u'\U0000002A\U0000FE0F\U000020E3': {
        'en' : u':keycap_*:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0000002A\U000020E3': {
        'en' : u':keycap_*:',
        'status' : unqualified,
        'E' : 2
    },
    u'\U00000030\U0000FE0F\U000020E3': {
        'en' : u':keycap_0:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00000030\U000020E3': {
        'en' : u':keycap_0:',
        'status' : unqualified,
        'E' : 0.6
    },
    u'\U00000031\U0000FE0F\U000020E3': {
        'en' : u':keycap_1:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00000031\U000020E3': {
        'en' : u':keycap_1:',
        'status' : unqualified,
        'E' : 0.6
    },
    u'\U0001F51F': {
        'en' : u':keycap_10:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00000032\U0000FE0F\U000020E3': {
        'en' : u':keycap_2:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00000032\U000020E3': {
        'en' : u':keycap_2:',
        'status' : unqualified,
        'E' : 0.6
    },
    u'\U00000033\U0000FE0F\U000020E3': {
        'en' : u':keycap_3:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00000033\U000020E3': {
        'en' : u':keycap_3:',
        'status' : unqualified,
        'E' : 0.6
    },
    u'\U00000034\U0000FE0F\U000020E3': {
        'en' : u':keycap_4:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00000034\U000020E3': {
        'en' : u':keycap_4:',
        'status' : unqualified,
        'E' : 0.6
    },
    u'\U00000035\U0000FE0F\U000020E3': {
        'en' : u':keycap_5:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00000035\U000020E3': {
        'en' : u':keycap_5:',
        'status' : unqualified,
        'E' : 0.6
    },
    u'\U00000036\U0000FE0F\U000020E3': {
        'en' : u':keycap_6:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00000036\U000020E3': {
        'en' : u':keycap_6:',
        'status' : unqualified,
        'E' : 0.6
    },
    u'\U00000037\U0000FE0F\U000020E3': {
        'en' : u':keycap_7:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00000037\U000020E3': {
        'en' : u':keycap_7:',
        'status' : unqualified,
        'E' : 0.6
    },
    u'\U00000038\U0000FE0F\U000020E3': {
        'en' : u':keycap_8:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00000038\U000020E3': {
        'en' : u':keycap_8:',
        'status' : unqualified,
        'E' : 0.6
    },
    u'\U00000039\U0000FE0F\U000020E3': {
        'en' : u':keycap_9:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00000039\U000020E3': {
        'en' : u':keycap_9:',
        'status' : unqualified,
        'E' : 0.6
    },
    u'\U0001F6F4': {
        'en' : u':kick_scooter:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F458': {
        'en' : u':kimono:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F48F': {
        'en' : u':kiss:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F48F\U0001F3FF': {
        'en' : u':kiss_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F48F\U0001F3FB': {
        'en' : u':kiss_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468': {
        'en' : u':kiss_man_man:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F468\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468': {
        'en' : u':kiss_man_man:',
        'status' : minimally_qualified,
        'E' : 2
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':kiss_man_man_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':kiss_man_man_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':kiss_man_man_dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':kiss_man_man_dark_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':kiss_man_man_dark_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':kiss_man_man_dark_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':kiss_man_man_dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':kiss_man_man_dark_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':kiss_man_man_dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':kiss_man_man_dark_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':kiss_man_man_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':kiss_man_man_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':kiss_man_man_light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':kiss_man_man_light_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':kiss_man_man_light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':kiss_man_man_light_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':kiss_man_man_light_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':kiss_man_man_light_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':kiss_man_man_light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':kiss_man_man_light_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':kiss_man_man_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':kiss_man_man_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':kiss_man_man_medium-dark_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':kiss_man_man_medium-dark_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':kiss_man_man_medium-dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':kiss_man_man_medium-dark_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':kiss_man_man_medium-dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':kiss_man_man_medium-dark_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':kiss_man_man_medium-dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':kiss_man_man_medium-dark_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':kiss_man_man_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':kiss_man_man_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':kiss_man_man_medium-light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':kiss_man_man_medium-light_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':kiss_man_man_medium-light_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':kiss_man_man_medium-light_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':kiss_man_man_medium-light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':kiss_man_man_medium-light_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':kiss_man_man_medium-light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':kiss_man_man_medium-light_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':kiss_man_man_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':kiss_man_man_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':kiss_man_man_medium_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':kiss_man_man_medium_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':kiss_man_man_medium_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':kiss_man_man_medium_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':kiss_man_man_medium_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':kiss_man_man_medium_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':kiss_man_man_medium_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':kiss_man_man_medium_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F48B': {
        'en' : u':kiss_mark:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F48F\U0001F3FE': {
        'en' : u':kiss_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F48F\U0001F3FC': {
        'en' : u':kiss_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F48F\U0001F3FD': {
        'en' : u':kiss_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FB': {
        'en' : u':kiss_person_person_dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FB': {
        'en' : u':kiss_person_person_dark_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FE': {
        'en' : u':kiss_person_person_dark_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FE': {
        'en' : u':kiss_person_person_dark_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FC': {
        'en' : u':kiss_person_person_dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FC': {
        'en' : u':kiss_person_person_dark_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FD': {
        'en' : u':kiss_person_person_dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FD': {
        'en' : u':kiss_person_person_dark_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FF': {
        'en' : u':kiss_person_person_light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FF': {
        'en' : u':kiss_person_person_light_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FE': {
        'en' : u':kiss_person_person_light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FE': {
        'en' : u':kiss_person_person_light_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FC': {
        'en' : u':kiss_person_person_light_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FC': {
        'en' : u':kiss_person_person_light_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FD': {
        'en' : u':kiss_person_person_light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FD': {
        'en' : u':kiss_person_person_light_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FF': {
        'en' : u':kiss_person_person_medium-dark_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FF': {
        'en' : u':kiss_person_person_medium-dark_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FB': {
        'en' : u':kiss_person_person_medium-dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FB': {
        'en' : u':kiss_person_person_medium-dark_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FC': {
        'en' : u':kiss_person_person_medium-dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FC': {
        'en' : u':kiss_person_person_medium-dark_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FD': {
        'en' : u':kiss_person_person_medium-dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FD': {
        'en' : u':kiss_person_person_medium-dark_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FF': {
        'en' : u':kiss_person_person_medium-light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FF': {
        'en' : u':kiss_person_person_medium-light_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FB': {
        'en' : u':kiss_person_person_medium-light_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FB': {
        'en' : u':kiss_person_person_medium-light_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FE': {
        'en' : u':kiss_person_person_medium-light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FE': {
        'en' : u':kiss_person_person_medium-light_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FD': {
        'en' : u':kiss_person_person_medium-light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FD': {
        'en' : u':kiss_person_person_medium-light_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FF': {
        'en' : u':kiss_person_person_medium_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FF': {
        'en' : u':kiss_person_person_medium_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FB': {
        'en' : u':kiss_person_person_medium_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FB': {
        'en' : u':kiss_person_person_medium_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FE': {
        'en' : u':kiss_person_person_medium_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FE': {
        'en' : u':kiss_person_person_medium_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FC': {
        'en' : u':kiss_person_person_medium_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F9D1\U0001F3FC': {
        'en' : u':kiss_person_person_medium_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468': {
        'en' : u':kiss_woman_man:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F469\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468': {
        'en' : u':kiss_woman_man:',
        'status' : minimally_qualified,
        'E' : 2
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':kiss_woman_man_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':kiss_woman_man_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':kiss_woman_man_dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':kiss_woman_man_dark_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':kiss_woman_man_dark_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':kiss_woman_man_dark_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':kiss_woman_man_dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':kiss_woman_man_dark_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':kiss_woman_man_dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':kiss_woman_man_dark_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':kiss_woman_man_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':kiss_woman_man_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':kiss_woman_man_light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':kiss_woman_man_light_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':kiss_woman_man_light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':kiss_woman_man_light_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':kiss_woman_man_light_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':kiss_woman_man_light_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':kiss_woman_man_light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':kiss_woman_man_light_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':kiss_woman_man_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':kiss_woman_man_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':kiss_woman_man_medium-dark_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':kiss_woman_man_medium-dark_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':kiss_woman_man_medium-dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':kiss_woman_man_medium-dark_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':kiss_woman_man_medium-dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':kiss_woman_man_medium-dark_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':kiss_woman_man_medium-dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':kiss_woman_man_medium-dark_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':kiss_woman_man_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':kiss_woman_man_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':kiss_woman_man_medium-light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':kiss_woman_man_medium-light_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':kiss_woman_man_medium-light_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':kiss_woman_man_medium-light_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':kiss_woman_man_medium-light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':kiss_woman_man_medium-light_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':kiss_woman_man_medium-light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':kiss_woman_man_medium-light_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':kiss_woman_man_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':kiss_woman_man_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':kiss_woman_man_medium_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':kiss_woman_man_medium_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':kiss_woman_man_medium_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':kiss_woman_man_medium_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':kiss_woman_man_medium_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':kiss_woman_man_medium_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':kiss_woman_man_medium_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':kiss_woman_man_medium_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469': {
        'en' : u':kiss_woman_woman:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F469\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469': {
        'en' : u':kiss_woman_woman:',
        'status' : minimally_qualified,
        'E' : 2
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':kiss_woman_woman_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':kiss_woman_woman_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':kiss_woman_woman_dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':kiss_woman_woman_dark_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':kiss_woman_woman_dark_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':kiss_woman_woman_dark_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':kiss_woman_woman_dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':kiss_woman_woman_dark_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':kiss_woman_woman_dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':kiss_woman_woman_dark_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':kiss_woman_woman_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':kiss_woman_woman_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':kiss_woman_woman_light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':kiss_woman_woman_light_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':kiss_woman_woman_light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':kiss_woman_woman_light_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':kiss_woman_woman_light_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':kiss_woman_woman_light_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':kiss_woman_woman_light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':kiss_woman_woman_light_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':kiss_woman_woman_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':kiss_woman_woman_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':kiss_woman_woman_medium-dark_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':kiss_woman_woman_medium-dark_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':kiss_woman_woman_medium-dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':kiss_woman_woman_medium-dark_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':kiss_woman_woman_medium-dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':kiss_woman_woman_medium-dark_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':kiss_woman_woman_medium-dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':kiss_woman_woman_medium-dark_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':kiss_woman_woman_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':kiss_woman_woman_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':kiss_woman_woman_medium-light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':kiss_woman_woman_medium-light_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':kiss_woman_woman_medium-light_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':kiss_woman_woman_medium-light_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':kiss_woman_woman_medium-light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':kiss_woman_woman_medium-light_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':kiss_woman_woman_medium-light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':kiss_woman_woman_medium-light_skin_tone_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':kiss_woman_woman_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':kiss_woman_woman_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':kiss_woman_woman_medium_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':kiss_woman_woman_medium_skin_tone_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':kiss_woman_woman_medium_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':kiss_woman_woman_medium_skin_tone_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':kiss_woman_woman_medium_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':kiss_woman_woman_medium_skin_tone_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000FE0F\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':kiss_woman_woman_medium_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':kiss_woman_woman_medium_skin_tone_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F63D': {
        'en' : u':kissing_cat:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F617': {
        'en' : u':kissing_face:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F61A': {
        'en' : u':kissing_face_with_closed_eyes:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F619': {
        'en' : u':kissing_face_with_smiling_eyes:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F52A': {
        'en' : u':kitchen_knife:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FA81': {
        'en' : u':kite:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F95D': {
        'en' : u':kiwi_fruit:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001FAA2': {
        'en' : u':knot:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F428': {
        'en' : u':koala:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F97C': {
        'en' : u':lab_coat:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F3F7\U0000FE0F': {
        'en' : u':label:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3F7': {
        'en' : u':label:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F94D': {
        'en' : u':lacrosse:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001FA9C': {
        'en' : u':ladder:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F41E': {
        'en' : u':lady_beetle:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4BB': {
        'en' : u':laptop:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F537': {
        'en' : u':large_blue_diamond:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F536': {
        'en' : u':large_orange_diamond:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F317': {
        'en' : u':last_quarter_moon:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F31C': {
        'en' : u':last_quarter_moon_face:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000023EE\U0000FE0F': {
        'en' : u':last_track_button:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000023EE': {
        'en' : u':last_track_button:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0000271D\U0000FE0F': {
        'en' : u':latin_cross:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0000271D': {
        'en' : u':latin_cross:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F343': {
        'en' : u':leaf_fluttering_in_wind:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F96C': {
        'en' : u':leafy_green:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F4D2': {
        'en' : u':ledger:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F91B': {
        'en' : u':left-facing_fist:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F91B\U0001F3FF': {
        'en' : u':left-facing_fist_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F91B\U0001F3FB': {
        'en' : u':left-facing_fist_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F91B\U0001F3FE': {
        'en' : u':left-facing_fist_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F91B\U0001F3FC': {
        'en' : u':left-facing_fist_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F91B\U0001F3FD': {
        'en' : u':left-facing_fist_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U00002194\U0000FE0F': {
        'en' : u':left-right_arrow:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002194': {
        'en' : u':left-right_arrow:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002B05\U0000FE0F': {
        'en' : u':left_arrow:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002B05': {
        'en' : u':left_arrow:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000021AA\U0000FE0F': {
        'en' : u':left_arrow_curving_right:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000021AA': {
        'en' : u':left_arrow_curving_right:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F6C5': {
        'en' : u':left_luggage:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F5E8\U0000FE0F': {
        'en' : u':left_speech_bubble:',
        'status' : fully_qualified,
        'E' : 2,
        'variant': True,
    },
    u'\U0001F5E8': {
        'en' : u':left_speech_bubble:',
        'status' : unqualified,
        'E' : 2,
        'variant': True,
    },
    u'\U0001FAF2': {
        'en' : u':leftwards_hand:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF2\U0001F3FF': {
        'en' : u':leftwards_hand_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF2\U0001F3FB': {
        'en' : u':leftwards_hand_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF2\U0001F3FE': {
        'en' : u':leftwards_hand_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF2\U0001F3FC': {
        'en' : u':leftwards_hand_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF2\U0001F3FD': {
        'en' : u':leftwards_hand_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F9B5': {
        'en' : u':leg:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B5\U0001F3FF': {
        'en' : u':leg_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B5\U0001F3FB': {
        'en' : u':leg_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B5\U0001F3FE': {
        'en' : u':leg_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B5\U0001F3FC': {
        'en' : u':leg_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B5\U0001F3FD': {
        'en' : u':leg_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F34B': {
        'en' : u':lemon:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F406': {
        'en' : u':leopard:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F39A\U0000FE0F': {
        'en' : u':level_slider:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F39A': {
        'en' : u':level_slider:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F4A1': {
        'en' : u':light_bulb:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F688': {
        'en' : u':light_rail:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3FB': {
        'en' : u':light_skin_tone:',
        'status' : component,
        'E' : 1
    },
    u'\U0001F517': {
        'en' : u':link:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F587\U0000FE0F': {
        'en' : u':linked_paperclips:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F587': {
        'en' : u':linked_paperclips:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F981': {
        'en' : u':lion:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F484': {
        'en' : u':lipstick:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F6AE': {
        'en' : u':litter_in_bin_sign:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F98E': {
        'en' : u':lizard:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F999': {
        'en' : u':llama:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F99E': {
        'en' : u':lobster:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F512': {
        'en' : u':locked:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F510': {
        'en' : u':locked_with_key:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F50F': {
        'en' : u':locked_with_pen:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F682': {
        'en' : u':locomotive:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F36D': {
        'en' : u':lollipop:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FA98': {
        'en' : u':long_drum:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F9F4': {
        'en' : u':lotion_bottle:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001FAB7': {
        'en' : u':lotus:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F62D': {
        'en' : u':loudly_crying_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4E2': {
        'en' : u':loudspeaker:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F91F': {
        'en' : u':love-you_gesture:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F91F\U0001F3FF': {
        'en' : u':love-you_gesture_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F91F\U0001F3FB': {
        'en' : u':love-you_gesture_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F91F\U0001F3FE': {
        'en' : u':love-you_gesture_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F91F\U0001F3FC': {
        'en' : u':love-you_gesture_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F91F\U0001F3FD': {
        'en' : u':love-you_gesture_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F3E9': {
        'en' : u':love_hotel:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F48C': {
        'en' : u':love_letter:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FAAB': {
        'en' : u':low_battery:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F9F3': {
        'en' : u':luggage:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001FAC1': {
        'en' : u':lungs:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F925': {
        'en' : u':lying_face:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F9D9': {
        'en' : u':mage:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FF': {
        'en' : u':mage_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FB': {
        'en' : u':mage_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FE': {
        'en' : u':mage_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FC': {
        'en' : u':mage_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FD': {
        'en' : u':mage_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001FA84': {
        'en' : u':magic_wand:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F9F2': {
        'en' : u':magnet:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F50D': {
        'en' : u':magnifying_glass_tilted_left:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F50E': {
        'en' : u':magnifying_glass_tilted_right:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F004': {
        'en' : u':mahjong_red_dragon:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002642\U0000FE0F': {
        'en' : u':male_sign:',
        'status' : fully_qualified,
        'E' : 4,
        'variant': True,
    },
    u'\U00002642': {
        'en' : u':male_sign:',
        'status' : unqualified,
        'E' : 4,
        'variant': True,
    },
    u'\U0001F9A3': {
        'en' : u':mammoth:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F468': {
        'en' : u':man:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F468\U0000200D\U0001F3A8': {
        'en' : u':man_artist:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F3A8': {
        'en' : u':man_artist_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F3A8': {
        'en' : u':man_artist_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F3A8': {
        'en' : u':man_artist_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F3A8': {
        'en' : u':man_artist_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F3A8': {
        'en' : u':man_artist_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U0001F680': {
        'en' : u':man_astronaut:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F680': {
        'en' : u':man_astronaut_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F680': {
        'en' : u':man_astronaut_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F680': {
        'en' : u':man_astronaut_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F680': {
        'en' : u':man_astronaut_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F680': {
        'en' : u':man_astronaut_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U0001F9B2': {
        'en' : u':man_bald:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9D4\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_beard:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D4\U0000200D\U00002642': {
        'en' : u':man_beard:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F6B4\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_biking:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0000200D\U00002642': {
        'en' : u':man_biking:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_biking_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_biking_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_biking_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_biking_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_biking_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_biking_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_biking_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_biking_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_biking_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_biking_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F471\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_blond_hair:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F471\U0000200D\U00002642': {
        'en' : u':man_blond_hair:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U000026F9\U0000FE0F\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_bouncing_ball:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U000026F9\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_bouncing_ball:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U000026F9\U0000FE0F\U0000200D\U00002642': {
        'en' : u':man_bouncing_ball:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U000026F9\U0000200D\U00002642': {
        'en' : u':man_bouncing_ball:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U000026F9\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_bouncing_ball_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U000026F9\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_bouncing_ball_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U000026F9\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_bouncing_ball_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U000026F9\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_bouncing_ball_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U000026F9\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_bouncing_ball_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U000026F9\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_bouncing_ball_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U000026F9\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_bouncing_ball_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U000026F9\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_bouncing_ball_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U000026F9\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_bouncing_ball_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U000026F9\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_bouncing_ball_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F647\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_bowing:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F647\U0000200D\U00002642': {
        'en' : u':man_bowing:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F647\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_bowing_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F647\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_bowing_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F647\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_bowing_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F647\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_bowing_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F647\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_bowing_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F647\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_bowing_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F647\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_bowing_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F647\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_bowing_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F647\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_bowing_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F647\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_bowing_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F938\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_cartwheeling:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F938\U0000200D\U00002642': {
        'en' : u':man_cartwheeling:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F938\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_cartwheeling_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F938\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_cartwheeling_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F938\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_cartwheeling_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F938\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_cartwheeling_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F938\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_cartwheeling_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F938\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_cartwheeling_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F938\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_cartwheeling_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F938\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_cartwheeling_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F938\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_cartwheeling_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F938\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_cartwheeling_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F9D7\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_climbing:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0000200D\U00002642': {
        'en' : u':man_climbing:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_climbing_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_climbing_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_climbing_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_climbing_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_climbing_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_climbing_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_climbing_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_climbing_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_climbing_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_climbing_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F477\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_construction_worker:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F477\U0000200D\U00002642': {
        'en' : u':man_construction_worker:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F477\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_construction_worker_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F477\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_construction_worker_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F477\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_construction_worker_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F477\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_construction_worker_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F477\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_construction_worker_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F477\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_construction_worker_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F477\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_construction_worker_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F477\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_construction_worker_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F477\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_construction_worker_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F477\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_construction_worker_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U0001F373': {
        'en' : u':man_cook:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F373': {
        'en' : u':man_cook_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F373': {
        'en' : u':man_cook_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F373': {
        'en' : u':man_cook_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F373': {
        'en' : u':man_cook_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F373': {
        'en' : u':man_cook_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U0001F9B1': {
        'en' : u':man_curly_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F57A': {
        'en' : u':man_dancing:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F57A\U0001F3FF': {
        'en' : u':man_dancing_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F57A\U0001F3FB': {
        'en' : u':man_dancing_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F57A\U0001F3FE': {
        'en' : u':man_dancing_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F57A\U0001F3FC': {
        'en' : u':man_dancing_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F57A\U0001F3FD': {
        'en' : u':man_dancing_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F468\U0001F3FF': {
        'en' : u':man_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F9B2': {
        'en' : u':man_dark_skin_tone_bald:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9D4\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_dark_skin_tone_beard:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D4\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_dark_skin_tone_beard:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F471\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_dark_skin_tone_blond_hair:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F471\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_dark_skin_tone_blond_hair:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F9B1': {
        'en' : u':man_dark_skin_tone_curly_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F9B0': {
        'en' : u':man_dark_skin_tone_red_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F9B3': {
        'en' : u':man_dark_skin_tone_white_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F575\U0000FE0F\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_detective:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F575\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_detective:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U0001F575\U0000FE0F\U0000200D\U00002642': {
        'en' : u':man_detective:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U0001F575\U0000200D\U00002642': {
        'en' : u':man_detective:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U0001F575\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_detective_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F575\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_detective_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F575\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_detective_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F575\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_detective_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F575\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_detective_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F575\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_detective_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F575\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_detective_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F575\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_detective_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F575\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_detective_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F575\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_detective_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F9DD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_elf:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0000200D\U00002642': {
        'en' : u':man_elf:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_elf_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_elf_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_elf_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_elf_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_elf_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_elf_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_elf_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_elf_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_elf_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_elf_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F926\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_facepalming:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F926\U0000200D\U00002642': {
        'en' : u':man_facepalming:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F926\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_facepalming_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F926\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_facepalming_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F926\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_facepalming_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F926\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_facepalming_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F926\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_facepalming_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F926\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_facepalming_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F926\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_facepalming_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F926\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_facepalming_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F926\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_facepalming_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F926\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_facepalming_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U0001F3ED': {
        'en' : u':man_factory_worker:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F3ED': {
        'en' : u':man_factory_worker_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F3ED': {
        'en' : u':man_factory_worker_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F3ED': {
        'en' : u':man_factory_worker_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F3ED': {
        'en' : u':man_factory_worker_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F3ED': {
        'en' : u':man_factory_worker_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F9DA\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_fairy:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0000200D\U00002642': {
        'en' : u':man_fairy:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_fairy_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_fairy_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_fairy_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_fairy_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_fairy_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_fairy_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_fairy_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_fairy_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_fairy_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_fairy_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F468\U0000200D\U0001F33E': {
        'en' : u':man_farmer:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F33E': {
        'en' : u':man_farmer_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F33E': {
        'en' : u':man_farmer_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F33E': {
        'en' : u':man_farmer_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F33E': {
        'en' : u':man_farmer_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F33E': {
        'en' : u':man_farmer_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U0001F37C': {
        'en' : u':man_feeding_baby:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F37C': {
        'en' : u':man_feeding_baby_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F37C': {
        'en' : u':man_feeding_baby_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F37C': {
        'en' : u':man_feeding_baby_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F37C': {
        'en' : u':man_feeding_baby_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F37C': {
        'en' : u':man_feeding_baby_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F468\U0000200D\U0001F692': {
        'en' : u':man_firefighter:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F692': {
        'en' : u':man_firefighter_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F692': {
        'en' : u':man_firefighter_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F692': {
        'en' : u':man_firefighter_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F692': {
        'en' : u':man_firefighter_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F692': {
        'en' : u':man_firefighter_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_frowning:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0000200D\U00002642': {
        'en' : u':man_frowning:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_frowning_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_frowning_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_frowning_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_frowning_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_frowning_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_frowning_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_frowning_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_frowning_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_frowning_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_frowning_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F9DE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_genie:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DE\U0000200D\U00002642': {
        'en' : u':man_genie:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F645\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_gesturing_NO:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F645\U0000200D\U00002642': {
        'en' : u':man_gesturing_NO:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F645\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_gesturing_NO_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F645\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_gesturing_NO_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F645\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_gesturing_NO_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F645\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_gesturing_NO_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F645\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_gesturing_NO_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F645\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_gesturing_NO_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F645\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_gesturing_NO_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F645\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_gesturing_NO_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F645\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_gesturing_NO_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F645\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_gesturing_NO_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F646\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_gesturing_OK:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F646\U0000200D\U00002642': {
        'en' : u':man_gesturing_OK:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F646\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_gesturing_OK_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F646\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_gesturing_OK_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F646\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_gesturing_OK_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F646\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_gesturing_OK_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F646\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_gesturing_OK_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F646\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_gesturing_OK_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F646\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_gesturing_OK_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F646\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_gesturing_OK_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F646\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_gesturing_OK_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F646\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_gesturing_OK_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F487\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_getting_haircut:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F487\U0000200D\U00002642': {
        'en' : u':man_getting_haircut:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F487\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_getting_haircut_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F487\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_getting_haircut_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F487\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_getting_haircut_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F487\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_getting_haircut_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F487\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_getting_haircut_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F487\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_getting_haircut_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F487\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_getting_haircut_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F487\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_getting_haircut_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F487\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_getting_haircut_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F487\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_getting_haircut_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F486\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_getting_massage:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F486\U0000200D\U00002642': {
        'en' : u':man_getting_massage:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F486\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_getting_massage_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F486\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_getting_massage_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F486\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_getting_massage_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F486\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_getting_massage_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F486\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_getting_massage_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F486\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_getting_massage_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F486\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_getting_massage_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F486\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_getting_massage_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F486\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_getting_massage_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F486\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_getting_massage_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0000FE0F\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_golfing:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_golfing:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U0001F3CC\U0000FE0F\U0000200D\U00002642': {
        'en' : u':man_golfing:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U0001F3CC\U0000200D\U00002642': {
        'en' : u':man_golfing:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_golfing_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_golfing_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_golfing_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_golfing_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_golfing_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_golfing_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_golfing_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_golfing_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_golfing_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_golfing_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F482\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_guard:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F482\U0000200D\U00002642': {
        'en' : u':man_guard:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F482\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_guard_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F482\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_guard_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F482\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_guard_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F482\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_guard_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F482\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_guard_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F482\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_guard_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F482\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_guard_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F482\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_guard_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F482\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_guard_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F482\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_guard_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U00002695\U0000FE0F': {
        'en' : u':man_health_worker:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U00002695': {
        'en' : u':man_health_worker:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002695\U0000FE0F': {
        'en' : u':man_health_worker_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002695': {
        'en' : u':man_health_worker_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002695\U0000FE0F': {
        'en' : u':man_health_worker_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002695': {
        'en' : u':man_health_worker_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002695\U0000FE0F': {
        'en' : u':man_health_worker_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002695': {
        'en' : u':man_health_worker_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002695\U0000FE0F': {
        'en' : u':man_health_worker_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002695': {
        'en' : u':man_health_worker_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002695\U0000FE0F': {
        'en' : u':man_health_worker_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002695': {
        'en' : u':man_health_worker_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F9D8\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_in_lotus_position:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0000200D\U00002642': {
        'en' : u':man_in_lotus_position:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_in_lotus_position_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_in_lotus_position_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_in_lotus_position_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_in_lotus_position_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_in_lotus_position_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_in_lotus_position_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_in_lotus_position_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_in_lotus_position_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_in_lotus_position_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_in_lotus_position_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F468\U0000200D\U0001F9BD': {
        'en' : u':man_in_manual_wheelchair:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F9BD': {
        'en' : u':man_in_manual_wheelchair_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F9BD': {
        'en' : u':man_in_manual_wheelchair_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F9BD': {
        'en' : u':man_in_manual_wheelchair_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F9BD': {
        'en' : u':man_in_manual_wheelchair_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F9BD': {
        'en' : u':man_in_manual_wheelchair_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0000200D\U0001F9BC': {
        'en' : u':man_in_motorized_wheelchair:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F9BC': {
        'en' : u':man_in_motorized_wheelchair_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F9BC': {
        'en' : u':man_in_motorized_wheelchair_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F9BC': {
        'en' : u':man_in_motorized_wheelchair_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F9BC': {
        'en' : u':man_in_motorized_wheelchair_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F9BC': {
        'en' : u':man_in_motorized_wheelchair_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9D6\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_in_steamy_room:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0000200D\U00002642': {
        'en' : u':man_in_steamy_room:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_in_steamy_room_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_in_steamy_room_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_in_steamy_room_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_in_steamy_room_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_in_steamy_room_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_in_steamy_room_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_in_steamy_room_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_in_steamy_room_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_in_steamy_room_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_in_steamy_room_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F935\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_in_tuxedo:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F935\U0000200D\U00002642': {
        'en' : u':man_in_tuxedo:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F935\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_in_tuxedo_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F935\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_in_tuxedo_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F935\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_in_tuxedo_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F935\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_in_tuxedo_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F935\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_in_tuxedo_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F935\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_in_tuxedo_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F935\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_in_tuxedo_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F935\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_in_tuxedo_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F935\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_in_tuxedo_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F935\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_in_tuxedo_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F468\U0000200D\U00002696\U0000FE0F': {
        'en' : u':man_judge:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U00002696': {
        'en' : u':man_judge:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002696\U0000FE0F': {
        'en' : u':man_judge_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002696': {
        'en' : u':man_judge_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002696\U0000FE0F': {
        'en' : u':man_judge_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002696': {
        'en' : u':man_judge_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002696\U0000FE0F': {
        'en' : u':man_judge_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002696': {
        'en' : u':man_judge_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002696\U0000FE0F': {
        'en' : u':man_judge_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002696': {
        'en' : u':man_judge_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002696\U0000FE0F': {
        'en' : u':man_judge_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002696': {
        'en' : u':man_judge_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F939\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_juggling:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F939\U0000200D\U00002642': {
        'en' : u':man_juggling:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F939\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_juggling_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F939\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_juggling_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F939\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_juggling_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F939\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_juggling_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F939\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_juggling_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F939\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_juggling_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F939\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_juggling_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F939\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_juggling_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F939\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_juggling_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F939\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_juggling_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F9CE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_kneeling:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0000200D\U00002642': {
        'en' : u':man_kneeling:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_kneeling_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_kneeling_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_kneeling_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_kneeling_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_kneeling_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_kneeling_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_kneeling_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_kneeling_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_kneeling_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_kneeling_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F3CB\U0000FE0F\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_lifting_weights:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_lifting_weights:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U0001F3CB\U0000FE0F\U0000200D\U00002642': {
        'en' : u':man_lifting_weights:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U0001F3CB\U0000200D\U00002642': {
        'en' : u':man_lifting_weights:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U0001F3CB\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_lifting_weights_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CB\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_lifting_weights_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CB\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_lifting_weights_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CB\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_lifting_weights_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CB\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_lifting_weights_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CB\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_lifting_weights_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CB\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_lifting_weights_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CB\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_lifting_weights_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CB\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_lifting_weights_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CB\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_lifting_weights_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FB': {
        'en' : u':man_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F9B2': {
        'en' : u':man_light_skin_tone_bald:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9D4\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_light_skin_tone_beard:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D4\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_light_skin_tone_beard:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F471\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_light_skin_tone_blond_hair:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F471\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_light_skin_tone_blond_hair:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F9B1': {
        'en' : u':man_light_skin_tone_curly_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F9B0': {
        'en' : u':man_light_skin_tone_red_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F9B3': {
        'en' : u':man_light_skin_tone_white_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9D9\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_mage:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0000200D\U00002642': {
        'en' : u':man_mage:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_mage_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_mage_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_mage_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_mage_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_mage_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_mage_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_mage_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_mage_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_mage_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_mage_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F468\U0000200D\U0001F527': {
        'en' : u':man_mechanic:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F527': {
        'en' : u':man_mechanic_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F527': {
        'en' : u':man_mechanic_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F527': {
        'en' : u':man_mechanic_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F527': {
        'en' : u':man_mechanic_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F527': {
        'en' : u':man_mechanic_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FE': {
        'en' : u':man_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F9B2': {
        'en' : u':man_medium-dark_skin_tone_bald:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9D4\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_medium-dark_skin_tone_beard:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D4\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_medium-dark_skin_tone_beard:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F471\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_medium-dark_skin_tone_blond_hair:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F471\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_medium-dark_skin_tone_blond_hair:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F9B1': {
        'en' : u':man_medium-dark_skin_tone_curly_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F9B0': {
        'en' : u':man_medium-dark_skin_tone_red_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F9B3': {
        'en' : u':man_medium-dark_skin_tone_white_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F468\U0001F3FC': {
        'en' : u':man_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F9B2': {
        'en' : u':man_medium-light_skin_tone_bald:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9D4\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_medium-light_skin_tone_beard:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D4\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_medium-light_skin_tone_beard:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F471\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_medium-light_skin_tone_blond_hair:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F471\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_medium-light_skin_tone_blond_hair:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F9B1': {
        'en' : u':man_medium-light_skin_tone_curly_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F9B0': {
        'en' : u':man_medium-light_skin_tone_red_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F9B3': {
        'en' : u':man_medium-light_skin_tone_white_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F468\U0001F3FD': {
        'en' : u':man_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F9B2': {
        'en' : u':man_medium_skin_tone_bald:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9D4\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_medium_skin_tone_beard:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D4\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_medium_skin_tone_beard:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F471\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_medium_skin_tone_blond_hair:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F471\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_medium_skin_tone_blond_hair:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F9B1': {
        'en' : u':man_medium_skin_tone_curly_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F9B0': {
        'en' : u':man_medium_skin_tone_red_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F9B3': {
        'en' : u':man_medium_skin_tone_white_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F6B5\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_mountain_biking:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0000200D\U00002642': {
        'en' : u':man_mountain_biking:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_mountain_biking_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_mountain_biking_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_mountain_biking_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_mountain_biking_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_mountain_biking_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_mountain_biking_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_mountain_biking_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_mountain_biking_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_mountain_biking_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_mountain_biking_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U0001F4BC': {
        'en' : u':man_office_worker:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F4BC': {
        'en' : u':man_office_worker_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F4BC': {
        'en' : u':man_office_worker_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F4BC': {
        'en' : u':man_office_worker_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F4BC': {
        'en' : u':man_office_worker_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F4BC': {
        'en' : u':man_office_worker_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U00002708\U0000FE0F': {
        'en' : u':man_pilot:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U00002708': {
        'en' : u':man_pilot:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002708\U0000FE0F': {
        'en' : u':man_pilot_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FF\U0000200D\U00002708': {
        'en' : u':man_pilot_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002708\U0000FE0F': {
        'en' : u':man_pilot_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FB\U0000200D\U00002708': {
        'en' : u':man_pilot_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002708\U0000FE0F': {
        'en' : u':man_pilot_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FE\U0000200D\U00002708': {
        'en' : u':man_pilot_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002708\U0000FE0F': {
        'en' : u':man_pilot_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FC\U0000200D\U00002708': {
        'en' : u':man_pilot_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002708\U0000FE0F': {
        'en' : u':man_pilot_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FD\U0000200D\U00002708': {
        'en' : u':man_pilot_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_playing_handball:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0000200D\U00002642': {
        'en' : u':man_playing_handball:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_playing_handball_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_playing_handball_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_playing_handball_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_playing_handball_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_playing_handball_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_playing_handball_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_playing_handball_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_playing_handball_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_playing_handball_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_playing_handball_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_playing_water_polo:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0000200D\U00002642': {
        'en' : u':man_playing_water_polo:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_playing_water_polo_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_playing_water_polo_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_playing_water_polo_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_playing_water_polo_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_playing_water_polo_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_playing_water_polo_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_playing_water_polo_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_playing_water_polo_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_playing_water_polo_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_playing_water_polo_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_police_officer:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0000200D\U00002642': {
        'en' : u':man_police_officer:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_police_officer_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_police_officer_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_police_officer_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_police_officer_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_police_officer_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_police_officer_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_police_officer_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_police_officer_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_police_officer_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_police_officer_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_pouting:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0000200D\U00002642': {
        'en' : u':man_pouting:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_pouting_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_pouting_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_pouting_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_pouting_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_pouting_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_pouting_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_pouting_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_pouting_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_pouting_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_pouting_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_raising_hand:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0000200D\U00002642': {
        'en' : u':man_raising_hand:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_raising_hand_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_raising_hand_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_raising_hand_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_raising_hand_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_raising_hand_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_raising_hand_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_raising_hand_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_raising_hand_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_raising_hand_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_raising_hand_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U0001F9B0': {
        'en' : u':man_red_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F6A3\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_rowing_boat:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0000200D\U00002642': {
        'en' : u':man_rowing_boat:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_rowing_boat_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_rowing_boat_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_rowing_boat_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_rowing_boat_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_rowing_boat_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_rowing_boat_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_rowing_boat_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_rowing_boat_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_rowing_boat_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_rowing_boat_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_running:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0000200D\U00002642': {
        'en' : u':man_running:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_running_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_running_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_running_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_running_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_running_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_running_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_running_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_running_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_running_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_running_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U0001F52C': {
        'en' : u':man_scientist:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F52C': {
        'en' : u':man_scientist_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F52C': {
        'en' : u':man_scientist_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F52C': {
        'en' : u':man_scientist_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F52C': {
        'en' : u':man_scientist_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F52C': {
        'en' : u':man_scientist_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F937\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_shrugging:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F937\U0000200D\U00002642': {
        'en' : u':man_shrugging:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F937\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_shrugging_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F937\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_shrugging_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F937\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_shrugging_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F937\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_shrugging_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F937\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_shrugging_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F937\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_shrugging_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F937\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_shrugging_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F937\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_shrugging_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F937\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_shrugging_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F937\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_shrugging_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U0001F3A4': {
        'en' : u':man_singer:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F3A4': {
        'en' : u':man_singer_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F3A4': {
        'en' : u':man_singer_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F3A4': {
        'en' : u':man_singer_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F3A4': {
        'en' : u':man_singer_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F3A4': {
        'en' : u':man_singer_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F9CD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_standing:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0000200D\U00002642': {
        'en' : u':man_standing:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_standing_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_standing_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_standing_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_standing_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_standing_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_standing_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_standing_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_standing_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_standing_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_standing_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F468\U0000200D\U0001F393': {
        'en' : u':man_student:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F393': {
        'en' : u':man_student_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F393': {
        'en' : u':man_student_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F393': {
        'en' : u':man_student_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F393': {
        'en' : u':man_student_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F393': {
        'en' : u':man_student_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F9B8\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_superhero:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0000200D\U00002642': {
        'en' : u':man_superhero:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_superhero_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_superhero_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_superhero_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_superhero_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_superhero_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_superhero_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_superhero_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_superhero_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_superhero_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_superhero_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_supervillain:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0000200D\U00002642': {
        'en' : u':man_supervillain:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_supervillain_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_supervillain_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_supervillain_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_supervillain_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_supervillain_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_supervillain_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_supervillain_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_supervillain_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_supervillain_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_supervillain_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F3C4\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_surfing:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0000200D\U00002642': {
        'en' : u':man_surfing:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_surfing_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_surfing_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_surfing_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_surfing_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_surfing_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_surfing_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_surfing_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_surfing_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_surfing_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_surfing_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_swimming:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0000200D\U00002642': {
        'en' : u':man_swimming:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_swimming_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_swimming_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_swimming_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_swimming_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_swimming_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_swimming_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_swimming_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_swimming_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_swimming_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_swimming_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U0001F3EB': {
        'en' : u':man_teacher:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F3EB': {
        'en' : u':man_teacher_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F3EB': {
        'en' : u':man_teacher_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F3EB': {
        'en' : u':man_teacher_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F3EB': {
        'en' : u':man_teacher_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F3EB': {
        'en' : u':man_teacher_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U0001F4BB': {
        'en' : u':man_technologist:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F4BB': {
        'en' : u':man_technologist_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F4BB': {
        'en' : u':man_technologist_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F4BB': {
        'en' : u':man_technologist_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F4BB': {
        'en' : u':man_technologist_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F4BB': {
        'en' : u':man_technologist_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F481\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_tipping_hand:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F481\U0000200D\U00002642': {
        'en' : u':man_tipping_hand:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F481\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_tipping_hand_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F481\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_tipping_hand_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F481\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_tipping_hand_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F481\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_tipping_hand_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F481\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_tipping_hand_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F481\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_tipping_hand_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F481\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_tipping_hand_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F481\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_tipping_hand_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F481\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_tipping_hand_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F481\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_tipping_hand_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F9DB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_vampire:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0000200D\U00002642': {
        'en' : u':man_vampire:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_vampire_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_vampire_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_vampire_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_vampire_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_vampire_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_vampire_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_vampire_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_vampire_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_vampire_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_vampire_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F6B6\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_walking:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0000200D\U00002642': {
        'en' : u':man_walking:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_walking_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_walking_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_walking_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_walking_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_walking_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_walking_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_walking_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_walking_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_walking_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_walking_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F473\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_wearing_turban:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F473\U0000200D\U00002642': {
        'en' : u':man_wearing_turban:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F473\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_wearing_turban_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F473\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_wearing_turban_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F473\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_wearing_turban_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F473\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_wearing_turban_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F473\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_wearing_turban_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F473\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_wearing_turban_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F473\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_wearing_turban_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F473\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_wearing_turban_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F473\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_wearing_turban_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F473\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_wearing_turban_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F468\U0000200D\U0001F9B3': {
        'en' : u':man_white_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F470\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_with_veil:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F470\U0000200D\U00002642': {
        'en' : u':man_with_veil:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F470\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_with_veil_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F470\U0001F3FF\U0000200D\U00002642': {
        'en' : u':man_with_veil_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F470\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_with_veil_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F470\U0001F3FB\U0000200D\U00002642': {
        'en' : u':man_with_veil_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F470\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_with_veil_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F470\U0001F3FE\U0000200D\U00002642': {
        'en' : u':man_with_veil_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F470\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_with_veil_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F470\U0001F3FC\U0000200D\U00002642': {
        'en' : u':man_with_veil_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F470\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_with_veil_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F470\U0001F3FD\U0000200D\U00002642': {
        'en' : u':man_with_veil_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F468\U0000200D\U0001F9AF': {
        'en' : u':man_with_white_cane:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F9AF': {
        'en' : u':man_with_white_cane_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F9AF': {
        'en' : u':man_with_white_cane_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F9AF': {
        'en' : u':man_with_white_cane_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F9AF': {
        'en' : u':man_with_white_cane_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F9AF': {
        'en' : u':man_with_white_cane_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9DF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':man_zombie:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DF\U0000200D\U00002642': {
        'en' : u':man_zombie:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F96D': {
        'en' : u':mango:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F570\U0000FE0F': {
        'en' : u':mantelpiece_clock:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F570': {
        'en' : u':mantelpiece_clock:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F9BD': {
        'en' : u':manual_wheelchair:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F45E': {
        'en' : u':man’s_shoe:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F5FE': {
        'en' : u':map_of_Japan:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F341': {
        'en' : u':maple_leaf:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F94B': {
        'en' : u':martial_arts_uniform:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F9C9': {
        'en' : u':mate:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F356': {
        'en' : u':meat_on_bone:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9D1\U0000200D\U0001F527': {
        'en' : u':mechanic:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F527': {
        'en' : u':mechanic_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F527': {
        'en' : u':mechanic_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F527': {
        'en' : u':mechanic_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F527': {
        'en' : u':mechanic_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F527': {
        'en' : u':mechanic_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9BE': {
        'en' : u':mechanical_arm:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9BF': {
        'en' : u':mechanical_leg:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U00002695\U0000FE0F': {
        'en' : u':medical_symbol:',
        'status' : fully_qualified,
        'E' : 4,
        'variant': True,
    },
    u'\U00002695': {
        'en' : u':medical_symbol:',
        'status' : unqualified,
        'E' : 4,
        'variant': True,
    },
    u'\U0001F3FE': {
        'en' : u':medium-dark_skin_tone:',
        'status' : component,
        'E' : 1
    },
    u'\U0001F3FC': {
        'en' : u':medium-light_skin_tone:',
        'status' : component,
        'E' : 1
    },
    u'\U0001F3FD': {
        'en' : u':medium_skin_tone:',
        'status' : component,
        'E' : 1
    },
    u'\U0001F4E3': {
        'en' : u':megaphone:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F348': {
        'en' : u':melon:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FAE0': {
        'en' : u':melting_face:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F4DD': {
        'en' : u':memo:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F46C': {
        'en' : u':men_holding_hands:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F46C\U0001F3FF': {
        'en' : u':men_holding_hands_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':men_holding_hands_dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':men_holding_hands_dark_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':men_holding_hands_dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':men_holding_hands_dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F46C\U0001F3FB': {
        'en' : u':men_holding_hands_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':men_holding_hands_light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':men_holding_hands_light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':men_holding_hands_light_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F468\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':men_holding_hands_light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F46C\U0001F3FE': {
        'en' : u':men_holding_hands_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':men_holding_hands_medium-dark_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':men_holding_hands_medium-dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':men_holding_hands_medium-dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':men_holding_hands_medium-dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F46C\U0001F3FC': {
        'en' : u':men_holding_hands_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':men_holding_hands_medium-light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':men_holding_hands_medium-light_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':men_holding_hands_medium-light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F468\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':men_holding_hands_medium-light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F46C\U0001F3FD': {
        'en' : u':men_holding_hands_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':men_holding_hands_medium_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':men_holding_hands_medium_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':men_holding_hands_medium_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F468\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':men_holding_hands_medium_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F46F\U0000200D\U00002642\U0000FE0F': {
        'en' : u':men_with_bunny_ears:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F46F\U0000200D\U00002642': {
        'en' : u':men_with_bunny_ears:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93C\U0000200D\U00002642\U0000FE0F': {
        'en' : u':men_wrestling:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93C\U0000200D\U00002642': {
        'en' : u':men_wrestling:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U00002764\U0000FE0F\U0000200D\U0001FA79': {
        'en' : u':mending_heart:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U00002764\U0000200D\U0001FA79': {
        'en' : u':mending_heart:',
        'status' : unqualified,
        'E' : 13.1
    },
    u'\U0001F54E': {
        'en' : u':menorah:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6B9': {
        'en' : u':men’s_room:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F9DC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':mermaid:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0000200D\U00002640': {
        'en' : u':mermaid:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':mermaid_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FF\U0000200D\U00002640': {
        'en' : u':mermaid_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':mermaid_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FB\U0000200D\U00002640': {
        'en' : u':mermaid_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':mermaid_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FE\U0000200D\U00002640': {
        'en' : u':mermaid_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':mermaid_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FC\U0000200D\U00002640': {
        'en' : u':mermaid_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':mermaid_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FD\U0000200D\U00002640': {
        'en' : u':mermaid_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':merman:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0000200D\U00002642': {
        'en' : u':merman:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FF\U0000200D\U00002642\U0000FE0F': {
        'en' : u':merman_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FF\U0000200D\U00002642': {
        'en' : u':merman_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FB\U0000200D\U00002642\U0000FE0F': {
        'en' : u':merman_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FB\U0000200D\U00002642': {
        'en' : u':merman_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FE\U0000200D\U00002642\U0000FE0F': {
        'en' : u':merman_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FE\U0000200D\U00002642': {
        'en' : u':merman_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FC\U0000200D\U00002642\U0000FE0F': {
        'en' : u':merman_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FC\U0000200D\U00002642': {
        'en' : u':merman_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FD\U0000200D\U00002642\U0000FE0F': {
        'en' : u':merman_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FD\U0000200D\U00002642': {
        'en' : u':merman_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DC': {
        'en' : u':merperson:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FF': {
        'en' : u':merperson_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FB': {
        'en' : u':merperson_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FE': {
        'en' : u':merperson_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FC': {
        'en' : u':merperson_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DC\U0001F3FD': {
        'en' : u':merperson_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F687': {
        'en' : u':metro:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F9A0': {
        'en' : u':microbe:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F3A4': {
        'en' : u':microphone:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F52C': {
        'en' : u':microscope:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F595': {
        'en' : u':middle_finger:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F595\U0001F3FF': {
        'en' : u':middle_finger_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F595\U0001F3FB': {
        'en' : u':middle_finger_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F595\U0001F3FE': {
        'en' : u':middle_finger_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F595\U0001F3FC': {
        'en' : u':middle_finger_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F595\U0001F3FD': {
        'en' : u':middle_finger_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001FA96': {
        'en' : u':military_helmet:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F396\U0000FE0F': {
        'en' : u':military_medal:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F396': {
        'en' : u':military_medal:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F30C': {
        'en' : u':milky_way:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F690': {
        'en' : u':minibus:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U00002796': {
        'en' : u':minus:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FA9E': {
        'en' : u':mirror:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001FAA9': {
        'en' : u':mirror_ball:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F5FF': {
        'en' : u':moai:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4F1': {
        'en' : u':mobile_phone:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4F4': {
        'en' : u':mobile_phone_off:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4F2': {
        'en' : u':mobile_phone_with_arrow:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F911': {
        'en' : u':money-mouth_face:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F4B0': {
        'en' : u':money_bag:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F4B8': {
        'en' : u':money_with_wings:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F412': {
        'en' : u':monkey:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F435': {
        'en' : u':monkey_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F69D': {
        'en' : u':monorail:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F96E': {
        'en' : u':moon_cake:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F391': {
        'en' : u':moon_viewing_ceremony:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F54C': {
        'en' : u':mosque:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F99F': {
        'en' : u':mosquito:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F6E5\U0000FE0F': {
        'en' : u':motor_boat:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6E5': {
        'en' : u':motor_boat:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6F5': {
        'en' : u':motor_scooter:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F3CD\U0000FE0F': {
        'en' : u':motorcycle:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3CD': {
        'en' : u':motorcycle:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F9BC': {
        'en' : u':motorized_wheelchair:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F6E3\U0000FE0F': {
        'en' : u':motorway:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6E3': {
        'en' : u':motorway:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5FB': {
        'en' : u':mount_fuji:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U000026F0\U0000FE0F': {
        'en' : u':mountain:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000026F0': {
        'en' : u':mountain:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6A0': {
        'en' : u':mountain_cableway:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F69E': {
        'en' : u':mountain_railway:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F401': {
        'en' : u':mouse:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F42D': {
        'en' : u':mouse_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FAA4': {
        'en' : u':mouse_trap:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F444': {
        'en' : u':mouth:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3A5': {
        'en' : u':movie_camera:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00002716\U0000FE0F': {
        'en' : u':multiply:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002716': {
        'en' : u':multiply:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F344': {
        'en' : u':mushroom:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3B9': {
        'en' : u':musical_keyboard:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3B5': {
        'en' : u':musical_note:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3B6': {
        'en' : u':musical_notes:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3BC': {
        'en' : u':musical_score:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F507': {
        'en' : u':muted_speaker:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F9D1\U0000200D\U0001F384': {
        'en' : u':mx_claus:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F384': {
        'en' : u':mx_claus_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F384': {
        'en' : u':mx_claus_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F384': {
        'en' : u':mx_claus_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F384': {
        'en' : u':mx_claus_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F384': {
        'en' : u':mx_claus_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F485': {
        'en' : u':nail_polish:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F485\U0001F3FF': {
        'en' : u':nail_polish_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F485\U0001F3FB': {
        'en' : u':nail_polish_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F485\U0001F3FE': {
        'en' : u':nail_polish_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F485\U0001F3FC': {
        'en' : u':nail_polish_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F485\U0001F3FD': {
        'en' : u':nail_polish_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F4DB': {
        'en' : u':name_badge:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3DE\U0000FE0F': {
        'en' : u':national_park:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3DE': {
        'en' : u':national_park:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F922': {
        'en' : u':nauseated_face:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F9FF': {
        'en' : u':nazar_amulet:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F454': {
        'en' : u':necktie:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F913': {
        'en' : u':nerd_face:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001FABA': {
        'en' : u':nest_with_eggs:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FA86': {
        'en' : u':nesting_dolls:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F610': {
        'en' : u':neutral_face:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F311': {
        'en' : u':new_moon:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F31A': {
        'en' : u':new_moon_face:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F4F0': {
        'en' : u':newspaper:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U000023ED\U0000FE0F': {
        'en' : u':next_track_button:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000023ED': {
        'en' : u':next_track_button:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F303': {
        'en' : u':night_with_stars:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F564': {
        'en' : u':nine-thirty:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F558': {
        'en' : u':nine_o’clock:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F977': {
        'en' : u':ninja:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F977\U0001F3FF': {
        'en' : u':ninja_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F977\U0001F3FB': {
        'en' : u':ninja_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F977\U0001F3FE': {
        'en' : u':ninja_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F977\U0001F3FC': {
        'en' : u':ninja_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F977\U0001F3FD': {
        'en' : u':ninja_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F6B3': {
        'en' : u':no_bicycles:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U000026D4': {
        'en' : u':no_entry:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F6AF': {
        'en' : u':no_littering:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F4F5': {
        'en' : u':no_mobile_phones:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F51E': {
        'en' : u':no_one_under_eighteen:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F6B7': {
        'en' : u':no_pedestrians:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6AD': {
        'en' : u':no_smoking:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F6B1': {
        'en' : u':non-potable_water:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F443': {
        'en' : u':nose:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F443\U0001F3FF': {
        'en' : u':nose_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F443\U0001F3FB': {
        'en' : u':nose_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F443\U0001F3FE': {
        'en' : u':nose_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F443\U0001F3FC': {
        'en' : u':nose_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F443\U0001F3FD': {
        'en' : u':nose_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F4D3': {
        'en' : u':notebook:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4D4': {
        'en' : u':notebook_with_decorative_cover:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F529': {
        'en' : u':nut_and_bolt:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F419': {
        'en' : u':octopus:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F362': {
        'en' : u':oden:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3E2': {
        'en' : u':office_building:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9D1\U0000200D\U0001F4BC': {
        'en' : u':office_worker:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F4BC': {
        'en' : u':office_worker_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F4BC': {
        'en' : u':office_worker_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F4BC': {
        'en' : u':office_worker_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F4BC': {
        'en' : u':office_worker_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F4BC': {
        'en' : u':office_worker_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F479': {
        'en' : u':ogre:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F6E2\U0000FE0F': {
        'en' : u':oil_drum:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6E2': {
        'en' : u':oil_drum:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5DD\U0000FE0F': {
        'en' : u':old_key:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5DD': {
        'en' : u':old_key:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F474': {
        'en' : u':old_man:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F474\U0001F3FF': {
        'en' : u':old_man_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F474\U0001F3FB': {
        'en' : u':old_man_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F474\U0001F3FE': {
        'en' : u':old_man_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F474\U0001F3FC': {
        'en' : u':old_man_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F474\U0001F3FD': {
        'en' : u':old_man_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F475': {
        'en' : u':old_woman:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F475\U0001F3FF': {
        'en' : u':old_woman_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F475\U0001F3FB': {
        'en' : u':old_woman_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F475\U0001F3FE': {
        'en' : u':old_woman_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F475\U0001F3FC': {
        'en' : u':old_woman_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F475\U0001F3FD': {
        'en' : u':old_woman_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F9D3': {
        'en' : u':older_person:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D3\U0001F3FF': {
        'en' : u':older_person_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D3\U0001F3FB': {
        'en' : u':older_person_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D3\U0001F3FE': {
        'en' : u':older_person_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D3\U0001F3FC': {
        'en' : u':older_person_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D3\U0001F3FD': {
        'en' : u':older_person_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001FAD2': {
        'en' : u':olive:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F549\U0000FE0F': {
        'en' : u':om:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F549': {
        'en' : u':om:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F698': {
        'en' : u':oncoming_automobile:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F68D': {
        'en' : u':oncoming_bus:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F44A': {
        'en' : u':oncoming_fist:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F44A\U0001F3FF': {
        'en' : u':oncoming_fist_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44A\U0001F3FB': {
        'en' : u':oncoming_fist_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44A\U0001F3FE': {
        'en' : u':oncoming_fist_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44A\U0001F3FC': {
        'en' : u':oncoming_fist_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44A\U0001F3FD': {
        'en' : u':oncoming_fist_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F694': {
        'en' : u':oncoming_police_car:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F696': {
        'en' : u':oncoming_taxi:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001FA71': {
        'en' : u':one-piece_swimsuit:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F55C': {
        'en' : u':one-thirty:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F550': {
        'en' : u':one_o’clock:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F9C5': {
        'en' : u':onion:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F4D6': {
        'en' : u':open_book:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4C2': {
        'en' : u':open_file_folder:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F450': {
        'en' : u':open_hands:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F450\U0001F3FF': {
        'en' : u':open_hands_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F450\U0001F3FB': {
        'en' : u':open_hands_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F450\U0001F3FE': {
        'en' : u':open_hands_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F450\U0001F3FC': {
        'en' : u':open_hands_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F450\U0001F3FD': {
        'en' : u':open_hands_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F4ED': {
        'en' : u':open_mailbox_with_lowered_flag:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F4EC': {
        'en' : u':open_mailbox_with_raised_flag:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F4BF': {
        'en' : u':optical_disk:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F4D9': {
        'en' : u':orange_book:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F7E0': {
        'en' : u':orange_circle:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9E1': {
        'en' : u':orange_heart:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F7E7': {
        'en' : u':orange_square:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9A7': {
        'en' : u':orangutan:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U00002626\U0000FE0F': {
        'en' : u':orthodox_cross:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U00002626': {
        'en' : u':orthodox_cross:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0001F9A6': {
        'en' : u':otter:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F4E4': {
        'en' : u':outbox_tray:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F989': {
        'en' : u':owl:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F402': {
        'en' : u':ox:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F9AA': {
        'en' : u':oyster:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F4E6': {
        'en' : u':package:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F4C4': {
        'en' : u':page_facing_up:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4C3': {
        'en' : u':page_with_curl:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4DF': {
        'en' : u':pager:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F58C\U0000FE0F': {
        'en' : u':paintbrush:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F58C': {
        'en' : u':paintbrush:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001FAF3': {
        'en' : u':palm_down_hand:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF3\U0001F3FF': {
        'en' : u':palm_down_hand_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF3\U0001F3FB': {
        'en' : u':palm_down_hand_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF3\U0001F3FE': {
        'en' : u':palm_down_hand_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF3\U0001F3FC': {
        'en' : u':palm_down_hand_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF3\U0001F3FD': {
        'en' : u':palm_down_hand_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F334': {
        'en' : u':palm_tree:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FAF4': {
        'en' : u':palm_up_hand:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF4\U0001F3FF': {
        'en' : u':palm_up_hand_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF4\U0001F3FB': {
        'en' : u':palm_up_hand_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF4\U0001F3FE': {
        'en' : u':palm_up_hand_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF4\U0001F3FC': {
        'en' : u':palm_up_hand_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF4\U0001F3FD': {
        'en' : u':palm_up_hand_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F932': {
        'en' : u':palms_up_together:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F932\U0001F3FF': {
        'en' : u':palms_up_together_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F932\U0001F3FB': {
        'en' : u':palms_up_together_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F932\U0001F3FE': {
        'en' : u':palms_up_together_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F932\U0001F3FC': {
        'en' : u':palms_up_together_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F932\U0001F3FD': {
        'en' : u':palms_up_together_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F95E': {
        'en' : u':pancakes:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F43C': {
        'en' : u':panda:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4CE': {
        'en' : u':paperclip:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FA82': {
        'en' : u':parachute:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F99C': {
        'en' : u':parrot:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0000303D\U0000FE0F': {
        'en' : u':part_alternation_mark:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0000303D': {
        'en' : u':part_alternation_mark:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F389': {
        'en' : u':party_popper:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F973': {
        'en' : u':partying_face:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F6F3\U0000FE0F': {
        'en' : u':passenger_ship:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6F3': {
        'en' : u':passenger_ship:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6C2': {
        'en' : u':passport_control:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U000023F8\U0000FE0F': {
        'en' : u':pause_button:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000023F8': {
        'en' : u':pause_button:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F43E': {
        'en' : u':paw_prints:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0000262E\U0000FE0F': {
        'en' : u':peace_symbol:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0000262E': {
        'en' : u':peace_symbol:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0001F351': {
        'en' : u':peach:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F99A': {
        'en' : u':peacock:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F95C': {
        'en' : u':peanuts:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F350': {
        'en' : u':pear:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F58A\U0000FE0F': {
        'en' : u':pen:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F58A': {
        'en' : u':pen:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0000270F\U0000FE0F': {
        'en' : u':pencil:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0000270F': {
        'en' : u':pencil:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F427': {
        'en' : u':penguin:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F614': {
        'en' : u':pensive_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9D1\U0000200D\U0001F91D\U0000200D\U0001F9D1': {
        'en' : u':people_holding_hands:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FF': {
        'en' : u':people_holding_hands_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FB': {
        'en' : u':people_holding_hands_dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FE': {
        'en' : u':people_holding_hands_dark_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FC': {
        'en' : u':people_holding_hands_dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FD': {
        'en' : u':people_holding_hands_dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FB': {
        'en' : u':people_holding_hands_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FF': {
        'en' : u':people_holding_hands_light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FE': {
        'en' : u':people_holding_hands_light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FC': {
        'en' : u':people_holding_hands_light_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FD': {
        'en' : u':people_holding_hands_light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FE': {
        'en' : u':people_holding_hands_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FF': {
        'en' : u':people_holding_hands_medium-dark_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FB': {
        'en' : u':people_holding_hands_medium-dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FC': {
        'en' : u':people_holding_hands_medium-dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FD': {
        'en' : u':people_holding_hands_medium-dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FC': {
        'en' : u':people_holding_hands_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FF': {
        'en' : u':people_holding_hands_medium-light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FB': {
        'en' : u':people_holding_hands_medium-light_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FE': {
        'en' : u':people_holding_hands_medium-light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FD': {
        'en' : u':people_holding_hands_medium-light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FD': {
        'en' : u':people_holding_hands_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FF': {
        'en' : u':people_holding_hands_medium_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FB': {
        'en' : u':people_holding_hands_medium_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FE': {
        'en' : u':people_holding_hands_medium_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FC': {
        'en' : u':people_holding_hands_medium_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001FAC2': {
        'en' : u':people_hugging:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F46F': {
        'en' : u':people_with_bunny_ears:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F93C': {
        'en' : u':people_wrestling:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F3AD': {
        'en' : u':performing_arts:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F623': {
        'en' : u':persevering_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9D1': {
        'en' : u':person:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D1\U0000200D\U0001F9B2': {
        'en' : u':person_bald:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D4': {
        'en' : u':person_beard:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F6B4': {
        'en' : u':person_biking:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6B4\U0001F3FF': {
        'en' : u':person_biking_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6B4\U0001F3FB': {
        'en' : u':person_biking_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6B4\U0001F3FE': {
        'en' : u':person_biking_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6B4\U0001F3FC': {
        'en' : u':person_biking_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6B4\U0001F3FD': {
        'en' : u':person_biking_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F471': {
        'en' : u':person_blond_hair:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U000026F9\U0000FE0F': {
        'en' : u':person_bouncing_ball:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000026F9': {
        'en' : u':person_bouncing_ball:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000026F9\U0001F3FF': {
        'en' : u':person_bouncing_ball_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U000026F9\U0001F3FB': {
        'en' : u':person_bouncing_ball_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U000026F9\U0001F3FE': {
        'en' : u':person_bouncing_ball_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U000026F9\U0001F3FC': {
        'en' : u':person_bouncing_ball_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U000026F9\U0001F3FD': {
        'en' : u':person_bouncing_ball_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F647': {
        'en' : u':person_bowing:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F647\U0001F3FF': {
        'en' : u':person_bowing_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F647\U0001F3FB': {
        'en' : u':person_bowing_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F647\U0001F3FE': {
        'en' : u':person_bowing_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F647\U0001F3FC': {
        'en' : u':person_bowing_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F647\U0001F3FD': {
        'en' : u':person_bowing_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F938': {
        'en' : u':person_cartwheeling:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F938\U0001F3FF': {
        'en' : u':person_cartwheeling_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F938\U0001F3FB': {
        'en' : u':person_cartwheeling_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F938\U0001F3FE': {
        'en' : u':person_cartwheeling_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F938\U0001F3FC': {
        'en' : u':person_cartwheeling_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F938\U0001F3FD': {
        'en' : u':person_cartwheeling_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F9D7': {
        'en' : u':person_climbing:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FF': {
        'en' : u':person_climbing_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FB': {
        'en' : u':person_climbing_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FE': {
        'en' : u':person_climbing_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FC': {
        'en' : u':person_climbing_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FD': {
        'en' : u':person_climbing_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D1\U0000200D\U0001F9B1': {
        'en' : u':person_curly_hair:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF': {
        'en' : u':person_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F9B2': {
        'en' : u':person_dark_skin_tone_bald:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D4\U0001F3FF': {
        'en' : u':person_dark_skin_tone_beard:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F471\U0001F3FF': {
        'en' : u':person_dark_skin_tone_blond_hair:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F9B1': {
        'en' : u':person_dark_skin_tone_curly_hair:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F9B0': {
        'en' : u':person_dark_skin_tone_red_hair:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F9B3': {
        'en' : u':person_dark_skin_tone_white_hair:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F926': {
        'en' : u':person_facepalming:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F926\U0001F3FF': {
        'en' : u':person_facepalming_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F926\U0001F3FB': {
        'en' : u':person_facepalming_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F926\U0001F3FE': {
        'en' : u':person_facepalming_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F926\U0001F3FC': {
        'en' : u':person_facepalming_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F926\U0001F3FD': {
        'en' : u':person_facepalming_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F9D1\U0000200D\U0001F37C': {
        'en' : u':person_feeding_baby:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F37C': {
        'en' : u':person_feeding_baby_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F37C': {
        'en' : u':person_feeding_baby_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F37C': {
        'en' : u':person_feeding_baby_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F37C': {
        'en' : u':person_feeding_baby_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F37C': {
        'en' : u':person_feeding_baby_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F93A': {
        'en' : u':person_fencing:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F64D': {
        'en' : u':person_frowning:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F64D\U0001F3FF': {
        'en' : u':person_frowning_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64D\U0001F3FB': {
        'en' : u':person_frowning_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64D\U0001F3FE': {
        'en' : u':person_frowning_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64D\U0001F3FC': {
        'en' : u':person_frowning_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64D\U0001F3FD': {
        'en' : u':person_frowning_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F645': {
        'en' : u':person_gesturing_NO:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F645\U0001F3FF': {
        'en' : u':person_gesturing_NO_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F645\U0001F3FB': {
        'en' : u':person_gesturing_NO_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F645\U0001F3FE': {
        'en' : u':person_gesturing_NO_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F645\U0001F3FC': {
        'en' : u':person_gesturing_NO_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F645\U0001F3FD': {
        'en' : u':person_gesturing_NO_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F646': {
        'en' : u':person_gesturing_OK:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F646\U0001F3FF': {
        'en' : u':person_gesturing_OK_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F646\U0001F3FB': {
        'en' : u':person_gesturing_OK_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F646\U0001F3FE': {
        'en' : u':person_gesturing_OK_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F646\U0001F3FC': {
        'en' : u':person_gesturing_OK_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F646\U0001F3FD': {
        'en' : u':person_gesturing_OK_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F487': {
        'en' : u':person_getting_haircut:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F487\U0001F3FF': {
        'en' : u':person_getting_haircut_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F487\U0001F3FB': {
        'en' : u':person_getting_haircut_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F487\U0001F3FE': {
        'en' : u':person_getting_haircut_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F487\U0001F3FC': {
        'en' : u':person_getting_haircut_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F487\U0001F3FD': {
        'en' : u':person_getting_haircut_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F486': {
        'en' : u':person_getting_massage:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F486\U0001F3FF': {
        'en' : u':person_getting_massage_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F486\U0001F3FB': {
        'en' : u':person_getting_massage_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F486\U0001F3FE': {
        'en' : u':person_getting_massage_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F486\U0001F3FC': {
        'en' : u':person_getting_massage_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F486\U0001F3FD': {
        'en' : u':person_getting_massage_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3CC\U0000FE0F': {
        'en' : u':person_golfing:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3CC': {
        'en' : u':person_golfing:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3CC\U0001F3FF': {
        'en' : u':person_golfing_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FB': {
        'en' : u':person_golfing_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FE': {
        'en' : u':person_golfing_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FC': {
        'en' : u':person_golfing_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FD': {
        'en' : u':person_golfing_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6CC': {
        'en' : u':person_in_bed:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6CC\U0001F3FF': {
        'en' : u':person_in_bed_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6CC\U0001F3FB': {
        'en' : u':person_in_bed_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6CC\U0001F3FE': {
        'en' : u':person_in_bed_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6CC\U0001F3FC': {
        'en' : u':person_in_bed_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6CC\U0001F3FD': {
        'en' : u':person_in_bed_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F9D8': {
        'en' : u':person_in_lotus_position:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FF': {
        'en' : u':person_in_lotus_position_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FB': {
        'en' : u':person_in_lotus_position_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FE': {
        'en' : u':person_in_lotus_position_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FC': {
        'en' : u':person_in_lotus_position_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FD': {
        'en' : u':person_in_lotus_position_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D1\U0000200D\U0001F9BD': {
        'en' : u':person_in_manual_wheelchair:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F9BD': {
        'en' : u':person_in_manual_wheelchair_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F9BD': {
        'en' : u':person_in_manual_wheelchair_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F9BD': {
        'en' : u':person_in_manual_wheelchair_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F9BD': {
        'en' : u':person_in_manual_wheelchair_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F9BD': {
        'en' : u':person_in_manual_wheelchair_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0000200D\U0001F9BC': {
        'en' : u':person_in_motorized_wheelchair:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F9BC': {
        'en' : u':person_in_motorized_wheelchair_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F9BC': {
        'en' : u':person_in_motorized_wheelchair_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F9BC': {
        'en' : u':person_in_motorized_wheelchair_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F9BC': {
        'en' : u':person_in_motorized_wheelchair_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F9BC': {
        'en' : u':person_in_motorized_wheelchair_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D6': {
        'en' : u':person_in_steamy_room:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FF': {
        'en' : u':person_in_steamy_room_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FB': {
        'en' : u':person_in_steamy_room_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FE': {
        'en' : u':person_in_steamy_room_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FC': {
        'en' : u':person_in_steamy_room_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FD': {
        'en' : u':person_in_steamy_room_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F574\U0000FE0F': {
        'en' : u':person_in_suit_levitating:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F574': {
        'en' : u':person_in_suit_levitating:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F574\U0001F3FF': {
        'en' : u':person_in_suit_levitating_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F574\U0001F3FB': {
        'en' : u':person_in_suit_levitating_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F574\U0001F3FE': {
        'en' : u':person_in_suit_levitating_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F574\U0001F3FC': {
        'en' : u':person_in_suit_levitating_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F574\U0001F3FD': {
        'en' : u':person_in_suit_levitating_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F935': {
        'en' : u':person_in_tuxedo:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F935\U0001F3FF': {
        'en' : u':person_in_tuxedo_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F935\U0001F3FB': {
        'en' : u':person_in_tuxedo_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F935\U0001F3FE': {
        'en' : u':person_in_tuxedo_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F935\U0001F3FC': {
        'en' : u':person_in_tuxedo_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F935\U0001F3FD': {
        'en' : u':person_in_tuxedo_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F939': {
        'en' : u':person_juggling:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F939\U0001F3FF': {
        'en' : u':person_juggling_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F939\U0001F3FB': {
        'en' : u':person_juggling_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F939\U0001F3FE': {
        'en' : u':person_juggling_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F939\U0001F3FC': {
        'en' : u':person_juggling_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F939\U0001F3FD': {
        'en' : u':person_juggling_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F9CE': {
        'en' : u':person_kneeling:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FF': {
        'en' : u':person_kneeling_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FB': {
        'en' : u':person_kneeling_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FE': {
        'en' : u':person_kneeling_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FC': {
        'en' : u':person_kneeling_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FD': {
        'en' : u':person_kneeling_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F3CB\U0000FE0F': {
        'en' : u':person_lifting_weights:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3CB': {
        'en' : u':person_lifting_weights:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3CB\U0001F3FF': {
        'en' : u':person_lifting_weights_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F3CB\U0001F3FB': {
        'en' : u':person_lifting_weights_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F3CB\U0001F3FE': {
        'en' : u':person_lifting_weights_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F3CB\U0001F3FC': {
        'en' : u':person_lifting_weights_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F3CB\U0001F3FD': {
        'en' : u':person_lifting_weights_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 2
    },
    u'\U0001F9D1\U0001F3FB': {
        'en' : u':person_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F9B2': {
        'en' : u':person_light_skin_tone_bald:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D4\U0001F3FB': {
        'en' : u':person_light_skin_tone_beard:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F471\U0001F3FB': {
        'en' : u':person_light_skin_tone_blond_hair:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F9B1': {
        'en' : u':person_light_skin_tone_curly_hair:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F9B0': {
        'en' : u':person_light_skin_tone_red_hair:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F9B3': {
        'en' : u':person_light_skin_tone_white_hair:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE': {
        'en' : u':person_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F9B2': {
        'en' : u':person_medium-dark_skin_tone_bald:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D4\U0001F3FE': {
        'en' : u':person_medium-dark_skin_tone_beard:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F471\U0001F3FE': {
        'en' : u':person_medium-dark_skin_tone_blond_hair:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F9B1': {
        'en' : u':person_medium-dark_skin_tone_curly_hair:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F9B0': {
        'en' : u':person_medium-dark_skin_tone_red_hair:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F9B3': {
        'en' : u':person_medium-dark_skin_tone_white_hair:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC': {
        'en' : u':person_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F9B2': {
        'en' : u':person_medium-light_skin_tone_bald:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D4\U0001F3FC': {
        'en' : u':person_medium-light_skin_tone_beard:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F471\U0001F3FC': {
        'en' : u':person_medium-light_skin_tone_blond_hair:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F9B1': {
        'en' : u':person_medium-light_skin_tone_curly_hair:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F9B0': {
        'en' : u':person_medium-light_skin_tone_red_hair:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F9B3': {
        'en' : u':person_medium-light_skin_tone_white_hair:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD': {
        'en' : u':person_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F9B2': {
        'en' : u':person_medium_skin_tone_bald:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D4\U0001F3FD': {
        'en' : u':person_medium_skin_tone_beard:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F471\U0001F3FD': {
        'en' : u':person_medium_skin_tone_blond_hair:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F9B1': {
        'en' : u':person_medium_skin_tone_curly_hair:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F9B0': {
        'en' : u':person_medium_skin_tone_red_hair:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F9B3': {
        'en' : u':person_medium_skin_tone_white_hair:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F6B5': {
        'en' : u':person_mountain_biking:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6B5\U0001F3FF': {
        'en' : u':person_mountain_biking_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6B5\U0001F3FB': {
        'en' : u':person_mountain_biking_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6B5\U0001F3FE': {
        'en' : u':person_mountain_biking_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6B5\U0001F3FC': {
        'en' : u':person_mountain_biking_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6B5\U0001F3FD': {
        'en' : u':person_mountain_biking_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F93E': {
        'en' : u':person_playing_handball:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F93E\U0001F3FF': {
        'en' : u':person_playing_handball_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F93E\U0001F3FB': {
        'en' : u':person_playing_handball_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F93E\U0001F3FE': {
        'en' : u':person_playing_handball_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F93E\U0001F3FC': {
        'en' : u':person_playing_handball_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F93E\U0001F3FD': {
        'en' : u':person_playing_handball_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F93D': {
        'en' : u':person_playing_water_polo:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F93D\U0001F3FF': {
        'en' : u':person_playing_water_polo_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F93D\U0001F3FB': {
        'en' : u':person_playing_water_polo_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F93D\U0001F3FE': {
        'en' : u':person_playing_water_polo_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F93D\U0001F3FC': {
        'en' : u':person_playing_water_polo_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F93D\U0001F3FD': {
        'en' : u':person_playing_water_polo_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F64E': {
        'en' : u':person_pouting:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F64E\U0001F3FF': {
        'en' : u':person_pouting_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64E\U0001F3FB': {
        'en' : u':person_pouting_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64E\U0001F3FE': {
        'en' : u':person_pouting_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64E\U0001F3FC': {
        'en' : u':person_pouting_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64E\U0001F3FD': {
        'en' : u':person_pouting_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64B': {
        'en' : u':person_raising_hand:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F64B\U0001F3FF': {
        'en' : u':person_raising_hand_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64B\U0001F3FB': {
        'en' : u':person_raising_hand_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64B\U0001F3FE': {
        'en' : u':person_raising_hand_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64B\U0001F3FC': {
        'en' : u':person_raising_hand_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64B\U0001F3FD': {
        'en' : u':person_raising_hand_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F9D1\U0000200D\U0001F9B0': {
        'en' : u':person_red_hair:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F6A3': {
        'en' : u':person_rowing_boat:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6A3\U0001F3FF': {
        'en' : u':person_rowing_boat_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6A3\U0001F3FB': {
        'en' : u':person_rowing_boat_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6A3\U0001F3FE': {
        'en' : u':person_rowing_boat_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6A3\U0001F3FC': {
        'en' : u':person_rowing_boat_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6A3\U0001F3FD': {
        'en' : u':person_rowing_boat_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3C3': {
        'en' : u':person_running:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3C3\U0001F3FF': {
        'en' : u':person_running_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3C3\U0001F3FB': {
        'en' : u':person_running_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3C3\U0001F3FE': {
        'en' : u':person_running_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3C3\U0001F3FC': {
        'en' : u':person_running_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3C3\U0001F3FD': {
        'en' : u':person_running_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F937': {
        'en' : u':person_shrugging:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F937\U0001F3FF': {
        'en' : u':person_shrugging_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F937\U0001F3FB': {
        'en' : u':person_shrugging_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F937\U0001F3FE': {
        'en' : u':person_shrugging_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F937\U0001F3FC': {
        'en' : u':person_shrugging_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F937\U0001F3FD': {
        'en' : u':person_shrugging_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F9CD': {
        'en' : u':person_standing:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FF': {
        'en' : u':person_standing_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FB': {
        'en' : u':person_standing_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FE': {
        'en' : u':person_standing_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FC': {
        'en' : u':person_standing_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FD': {
        'en' : u':person_standing_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F3C4': {
        'en' : u':person_surfing:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F3C4\U0001F3FF': {
        'en' : u':person_surfing_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3C4\U0001F3FB': {
        'en' : u':person_surfing_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3C4\U0001F3FE': {
        'en' : u':person_surfing_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3C4\U0001F3FC': {
        'en' : u':person_surfing_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3C4\U0001F3FD': {
        'en' : u':person_surfing_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3CA': {
        'en' : u':person_swimming:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F3CA\U0001F3FF': {
        'en' : u':person_swimming_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3CA\U0001F3FB': {
        'en' : u':person_swimming_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3CA\U0001F3FE': {
        'en' : u':person_swimming_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3CA\U0001F3FC': {
        'en' : u':person_swimming_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3CA\U0001F3FD': {
        'en' : u':person_swimming_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6C0': {
        'en' : u':person_taking_bath:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F6C0\U0001F3FF': {
        'en' : u':person_taking_bath_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6C0\U0001F3FB': {
        'en' : u':person_taking_bath_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6C0\U0001F3FE': {
        'en' : u':person_taking_bath_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6C0\U0001F3FC': {
        'en' : u':person_taking_bath_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6C0\U0001F3FD': {
        'en' : u':person_taking_bath_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F481': {
        'en' : u':person_tipping_hand:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F481\U0001F3FF': {
        'en' : u':person_tipping_hand_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F481\U0001F3FB': {
        'en' : u':person_tipping_hand_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F481\U0001F3FE': {
        'en' : u':person_tipping_hand_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F481\U0001F3FC': {
        'en' : u':person_tipping_hand_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F481\U0001F3FD': {
        'en' : u':person_tipping_hand_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6B6': {
        'en' : u':person_walking:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F6B6\U0001F3FF': {
        'en' : u':person_walking_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6B6\U0001F3FB': {
        'en' : u':person_walking_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6B6\U0001F3FE': {
        'en' : u':person_walking_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6B6\U0001F3FC': {
        'en' : u':person_walking_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6B6\U0001F3FD': {
        'en' : u':person_walking_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F473': {
        'en' : u':person_wearing_turban:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F473\U0001F3FF': {
        'en' : u':person_wearing_turban_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F473\U0001F3FB': {
        'en' : u':person_wearing_turban_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F473\U0001F3FE': {
        'en' : u':person_wearing_turban_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F473\U0001F3FC': {
        'en' : u':person_wearing_turban_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F473\U0001F3FD': {
        'en' : u':person_wearing_turban_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F9D1\U0000200D\U0001F9B3': {
        'en' : u':person_white_hair:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001FAC5': {
        'en' : u':person_with_crown:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAC5\U0001F3FF': {
        'en' : u':person_with_crown_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAC5\U0001F3FB': {
        'en' : u':person_with_crown_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAC5\U0001F3FE': {
        'en' : u':person_with_crown_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAC5\U0001F3FC': {
        'en' : u':person_with_crown_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAC5\U0001F3FD': {
        'en' : u':person_with_crown_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F472': {
        'en' : u':person_with_skullcap:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F472\U0001F3FF': {
        'en' : u':person_with_skullcap_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F472\U0001F3FB': {
        'en' : u':person_with_skullcap_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F472\U0001F3FE': {
        'en' : u':person_with_skullcap_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F472\U0001F3FC': {
        'en' : u':person_with_skullcap_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F472\U0001F3FD': {
        'en' : u':person_with_skullcap_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F470': {
        'en' : u':person_with_veil:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F470\U0001F3FF': {
        'en' : u':person_with_veil_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F470\U0001F3FB': {
        'en' : u':person_with_veil_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F470\U0001F3FE': {
        'en' : u':person_with_veil_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F470\U0001F3FC': {
        'en' : u':person_with_veil_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F470\U0001F3FD': {
        'en' : u':person_with_veil_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F9D1\U0000200D\U0001F9AF': {
        'en' : u':person_with_white_cane:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F9AF': {
        'en' : u':person_with_white_cane_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F9AF': {
        'en' : u':person_with_white_cane_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F9AF': {
        'en' : u':person_with_white_cane_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F9AF': {
        'en' : u':person_with_white_cane_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F9AF': {
        'en' : u':person_with_white_cane_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9EB': {
        'en' : u':petri_dish:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U000026CF\U0000FE0F': {
        'en' : u':pick:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000026CF': {
        'en' : u':pick:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6FB': {
        'en' : u':pickup_truck:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F967': {
        'en' : u':pie:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F416': {
        'en' : u':pig:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F437': {
        'en' : u':pig_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F43D': {
        'en' : u':pig_nose:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4A9': {
        'en' : u':pile_of_poo:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F48A': {
        'en' : u':pill:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9D1\U0000200D\U00002708\U0000FE0F': {
        'en' : u':pilot:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0000200D\U00002708': {
        'en' : u':pilot:',
        'status' : minimally_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002708\U0000FE0F': {
        'en' : u':pilot_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U00002708': {
        'en' : u':pilot_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002708\U0000FE0F': {
        'en' : u':pilot_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U00002708': {
        'en' : u':pilot_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002708\U0000FE0F': {
        'en' : u':pilot_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U00002708': {
        'en' : u':pilot_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002708\U0000FE0F': {
        'en' : u':pilot_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U00002708': {
        'en' : u':pilot_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002708\U0000FE0F': {
        'en' : u':pilot_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U00002708': {
        'en' : u':pilot_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12.1
    },
    u'\U0001F90C': {
        'en' : u':pinched_fingers:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F90C\U0001F3FF': {
        'en' : u':pinched_fingers_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F90C\U0001F3FB': {
        'en' : u':pinched_fingers_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F90C\U0001F3FE': {
        'en' : u':pinched_fingers_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F90C\U0001F3FC': {
        'en' : u':pinched_fingers_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F90C\U0001F3FD': {
        'en' : u':pinched_fingers_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F90F': {
        'en' : u':pinching_hand:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F90F\U0001F3FF': {
        'en' : u':pinching_hand_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F90F\U0001F3FB': {
        'en' : u':pinching_hand_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F90F\U0001F3FE': {
        'en' : u':pinching_hand_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F90F\U0001F3FC': {
        'en' : u':pinching_hand_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F90F\U0001F3FD': {
        'en' : u':pinching_hand_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F38D': {
        'en' : u':pine_decoration:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F34D': {
        'en' : u':pineapple:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3D3': {
        'en' : u':ping_pong:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3F4\U0000200D\U00002620\U0000FE0F': {
        'en' : u':pirate_flag:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F3F4\U0000200D\U00002620': {
        'en' : u':pirate_flag:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F355': {
        'en' : u':pizza:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FA85': {
        'en' : u':piñata:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001FAA7': {
        'en' : u':placard:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F6D0': {
        'en' : u':place_of_worship:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U000025B6\U0000FE0F': {
        'en' : u':play_button:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000025B6': {
        'en' : u':play_button:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000023EF\U0000FE0F': {
        'en' : u':play_or_pause_button:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U000023EF': {
        'en' : u':play_or_pause_button:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0001F6DD': {
        'en' : u':playground_slide:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F97A': {
        'en' : u':pleading_face:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001FAA0': {
        'en' : u':plunger:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U00002795': {
        'en' : u':plus:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F43B\U0000200D\U00002744\U0000FE0F': {
        'en' : u':polar_bear:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F43B\U0000200D\U00002744': {
        'en' : u':polar_bear:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F693': {
        'en' : u':police_car:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F6A8': {
        'en' : u':police_car_light:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F46E': {
        'en' : u':police_officer:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F46E\U0001F3FF': {
        'en' : u':police_officer_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F46E\U0001F3FB': {
        'en' : u':police_officer_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F46E\U0001F3FE': {
        'en' : u':police_officer_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F46E\U0001F3FC': {
        'en' : u':police_officer_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F46E\U0001F3FD': {
        'en' : u':police_officer_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F429': {
        'en' : u':poodle:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3B1': {
        'en' : u':pool_8_ball:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F37F': {
        'en' : u':popcorn:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3E4': {
        'en' : u':post_office:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F4EF': {
        'en' : u':postal_horn:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F4EE': {
        'en' : u':postbox:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F372': {
        'en' : u':pot_of_food:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F6B0': {
        'en' : u':potable_water:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F954': {
        'en' : u':potato:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001FAB4': {
        'en' : u':potted_plant:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F357': {
        'en' : u':poultry_leg:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4B7': {
        'en' : u':pound_banknote:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001FAD7': {
        'en' : u':pouring_liquid:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F63E': {
        'en' : u':pouting_cat:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F621': {
        'en' : u':pouting_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4FF': {
        'en' : u':prayer_beads:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001FAC3': {
        'en' : u':pregnant_man:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAC3\U0001F3FF': {
        'en' : u':pregnant_man_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAC3\U0001F3FB': {
        'en' : u':pregnant_man_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAC3\U0001F3FE': {
        'en' : u':pregnant_man_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAC3\U0001F3FC': {
        'en' : u':pregnant_man_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAC3\U0001F3FD': {
        'en' : u':pregnant_man_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAC4': {
        'en' : u':pregnant_person:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAC4\U0001F3FF': {
        'en' : u':pregnant_person_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAC4\U0001F3FB': {
        'en' : u':pregnant_person_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAC4\U0001F3FE': {
        'en' : u':pregnant_person_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAC4\U0001F3FC': {
        'en' : u':pregnant_person_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAC4\U0001F3FD': {
        'en' : u':pregnant_person_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F930': {
        'en' : u':pregnant_woman:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F930\U0001F3FF': {
        'en' : u':pregnant_woman_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F930\U0001F3FB': {
        'en' : u':pregnant_woman_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F930\U0001F3FE': {
        'en' : u':pregnant_woman_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F930\U0001F3FC': {
        'en' : u':pregnant_woman_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F930\U0001F3FD': {
        'en' : u':pregnant_woman_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F968': {
        'en' : u':pretzel:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F934': {
        'en' : u':prince:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F934\U0001F3FF': {
        'en' : u':prince_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F934\U0001F3FB': {
        'en' : u':prince_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F934\U0001F3FE': {
        'en' : u':prince_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F934\U0001F3FC': {
        'en' : u':prince_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F934\U0001F3FD': {
        'en' : u':prince_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F478': {
        'en' : u':princess:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F478\U0001F3FF': {
        'en' : u':princess_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F478\U0001F3FB': {
        'en' : u':princess_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F478\U0001F3FE': {
        'en' : u':princess_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F478\U0001F3FC': {
        'en' : u':princess_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F478\U0001F3FD': {
        'en' : u':princess_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F5A8\U0000FE0F': {
        'en' : u':printer:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5A8': {
        'en' : u':printer:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6AB': {
        'en' : u':prohibited:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F7E3': {
        'en' : u':purple_circle:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F49C': {
        'en' : u':purple_heart:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F7EA': {
        'en' : u':purple_square:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F45B': {
        'en' : u':purse:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4CC': {
        'en' : u':pushpin:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9E9': {
        'en' : u':puzzle_piece:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F407': {
        'en' : u':rabbit:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F430': {
        'en' : u':rabbit_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F99D': {
        'en' : u':raccoon:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F3CE\U0000FE0F': {
        'en' : u':racing_car:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3CE': {
        'en' : u':racing_car:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F4FB': {
        'en' : u':radio:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F518': {
        'en' : u':radio_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00002622\U0000FE0F': {
        'en' : u':radioactive:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U00002622': {
        'en' : u':radioactive:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0001F683': {
        'en' : u':railway_car:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F6E4\U0000FE0F': {
        'en' : u':railway_track:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6E4': {
        'en' : u':railway_track:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F308': {
        'en' : u':rainbow:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3F3\U0000FE0F\U0000200D\U0001F308': {
        'en' : u':rainbow_flag:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3F3\U0000200D\U0001F308': {
        'en' : u':rainbow_flag:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U0001F91A': {
        'en' : u':raised_back_of_hand:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F91A\U0001F3FF': {
        'en' : u':raised_back_of_hand_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F91A\U0001F3FB': {
        'en' : u':raised_back_of_hand_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F91A\U0001F3FE': {
        'en' : u':raised_back_of_hand_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F91A\U0001F3FC': {
        'en' : u':raised_back_of_hand_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F91A\U0001F3FD': {
        'en' : u':raised_back_of_hand_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0000270A': {
        'en' : u':raised_fist:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0000270A\U0001F3FF': {
        'en' : u':raised_fist_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000270A\U0001F3FB': {
        'en' : u':raised_fist_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000270A\U0001F3FE': {
        'en' : u':raised_fist_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000270A\U0001F3FC': {
        'en' : u':raised_fist_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000270A\U0001F3FD': {
        'en' : u':raised_fist_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000270B': {
        'en' : u':raised_hand:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0000270B\U0001F3FF': {
        'en' : u':raised_hand_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000270B\U0001F3FB': {
        'en' : u':raised_hand_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000270B\U0001F3FE': {
        'en' : u':raised_hand_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000270B\U0001F3FC': {
        'en' : u':raised_hand_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000270B\U0001F3FD': {
        'en' : u':raised_hand_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64C': {
        'en' : u':raising_hands:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F64C\U0001F3FF': {
        'en' : u':raising_hands_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64C\U0001F3FB': {
        'en' : u':raising_hands_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64C\U0001F3FE': {
        'en' : u':raising_hands_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64C\U0001F3FC': {
        'en' : u':raising_hands_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F64C\U0001F3FD': {
        'en' : u':raising_hands_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F40F': {
        'en' : u':ram:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F400': {
        'en' : u':rat:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001FA92': {
        'en' : u':razor:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9FE': {
        'en' : u':receipt:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U000023FA\U0000FE0F': {
        'en' : u':record_button:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000023FA': {
        'en' : u':record_button:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0000267B\U0000FE0F': {
        'en' : u':recycling_symbol:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0000267B': {
        'en' : u':recycling_symbol:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F34E': {
        'en' : u':red_apple:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F534': {
        'en' : u':red_circle:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9E7': {
        'en' : u':red_envelope:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U00002757': {
        'en' : u':red_exclamation_mark:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F9B0': {
        'en' : u':red_hair:',
        'status' : component,
        'E' : 11
    },
    u'\U00002764\U0000FE0F': {
        'en' : u':red_heart:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002764': {
        'en' : u':red_heart:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F3EE': {
        'en' : u':red_paper_lantern:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00002753': {
        'en' : u':red_question_mark:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F7E5': {
        'en' : u':red_square:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F53B': {
        'en' : u':red_triangle_pointed_down:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F53A': {
        'en' : u':red_triangle_pointed_up:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U000000AE\U0000FE0F': {
        'en' : u':registered:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000000AE': {
        'en' : u':registered:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F60C': {
        'en' : u':relieved_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F397\U0000FE0F': {
        'en' : u':reminder_ribbon:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F397': {
        'en' : u':reminder_ribbon:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F501': {
        'en' : u':repeat_button:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F502': {
        'en' : u':repeat_single_button:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U000026D1\U0000FE0F': {
        'en' : u':rescue_worker’s_helmet:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000026D1': {
        'en' : u':rescue_worker’s_helmet:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6BB': {
        'en' : u':restroom:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U000025C0\U0000FE0F': {
        'en' : u':reverse_button:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000025C0': {
        'en' : u':reverse_button:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F49E': {
        'en' : u':revolving_hearts:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F98F': {
        'en' : u':rhinoceros:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F380': {
        'en' : u':ribbon:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F359': {
        'en' : u':rice_ball:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F358': {
        'en' : u':rice_cracker:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F91C': {
        'en' : u':right-facing_fist:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F91C\U0001F3FF': {
        'en' : u':right-facing_fist_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F91C\U0001F3FB': {
        'en' : u':right-facing_fist_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F91C\U0001F3FE': {
        'en' : u':right-facing_fist_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F91C\U0001F3FC': {
        'en' : u':right-facing_fist_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F91C\U0001F3FD': {
        'en' : u':right-facing_fist_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F5EF\U0000FE0F': {
        'en' : u':right_anger_bubble:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5EF': {
        'en' : u':right_anger_bubble:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000027A1\U0000FE0F': {
        'en' : u':right_arrow:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000027A1': {
        'en' : u':right_arrow:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002935\U0000FE0F': {
        'en' : u':right_arrow_curving_down:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002935': {
        'en' : u':right_arrow_curving_down:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000021A9\U0000FE0F': {
        'en' : u':right_arrow_curving_left:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000021A9': {
        'en' : u':right_arrow_curving_left:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002934\U0000FE0F': {
        'en' : u':right_arrow_curving_up:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002934': {
        'en' : u':right_arrow_curving_up:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001FAF1': {
        'en' : u':rightwards_hand:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF1\U0001F3FF': {
        'en' : u':rightwards_hand_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF1\U0001F3FB': {
        'en' : u':rightwards_hand_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF1\U0001F3FE': {
        'en' : u':rightwards_hand_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF1\U0001F3FC': {
        'en' : u':rightwards_hand_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FAF1\U0001F3FD': {
        'en' : u':rightwards_hand_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F48D': {
        'en' : u':ring:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F6DF': {
        'en' : u':ring_buoy:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001FA90': {
        'en' : u':ringed_planet:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F360': {
        'en' : u':roasted_sweet_potato:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F916': {
        'en' : u':robot:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001FAA8': {
        'en' : u':rock:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F680': {
        'en' : u':rocket:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9FB': {
        'en' : u':roll_of_paper:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F5DE\U0000FE0F': {
        'en' : u':rolled-up_newspaper:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5DE': {
        'en' : u':rolled-up_newspaper:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3A2': {
        'en' : u':roller_coaster:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F6FC': {
        'en' : u':roller_skate:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F923': {
        'en' : u':rolling_on_the_floor_laughing:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F413': {
        'en' : u':rooster:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F339': {
        'en' : u':rose:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3F5\U0000FE0F': {
        'en' : u':rosette:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3F5': {
        'en' : u':rosette:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F4CD': {
        'en' : u':round_pushpin:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3C9': {
        'en' : u':rugby_football:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3BD': {
        'en' : u':running_shirt:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F45F': {
        'en' : u':running_shoe:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F625': {
        'en' : u':sad_but_relieved_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9F7': {
        'en' : u':safety_pin:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9BA': {
        'en' : u':safety_vest:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U000026F5': {
        'en' : u':sailboat:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F376': {
        'en' : u':sake:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9C2': {
        'en' : u':salt:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001FAE1': {
        'en' : u':saluting_face:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F96A': {
        'en' : u':sandwich:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F97B': {
        'en' : u':sari:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F6F0\U0000FE0F': {
        'en' : u':satellite:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6F0': {
        'en' : u':satellite:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F4E1': {
        'en' : u':satellite_antenna:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F995': {
        'en' : u':sauropod:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F3B7': {
        'en' : u':saxophone:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9E3': {
        'en' : u':scarf:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F3EB': {
        'en' : u':school:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9D1\U0000200D\U0001F52C': {
        'en' : u':scientist:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F52C': {
        'en' : u':scientist_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F52C': {
        'en' : u':scientist_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F52C': {
        'en' : u':scientist_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F52C': {
        'en' : u':scientist_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F52C': {
        'en' : u':scientist_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U00002702\U0000FE0F': {
        'en' : u':scissors:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002702': {
        'en' : u':scissors:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F982': {
        'en' : u':scorpion:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001FA9B': {
        'en' : u':screwdriver:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F4DC': {
        'en' : u':scroll:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9AD': {
        'en' : u':seal:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F4BA': {
        'en' : u':seat:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F648': {
        'en' : u':see-no-evil_monkey:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F331': {
        'en' : u':seedling:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F933': {
        'en' : u':selfie:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F933\U0001F3FF': {
        'en' : u':selfie_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F933\U0001F3FB': {
        'en' : u':selfie_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F933\U0001F3FE': {
        'en' : u':selfie_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F933\U0001F3FC': {
        'en' : u':selfie_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F933\U0001F3FD': {
        'en' : u':selfie_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F415\U0000200D\U0001F9BA': {
        'en' : u':service_dog:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F562': {
        'en' : u':seven-thirty:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F556': {
        'en' : u':seven_o’clock:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001FAA1': {
        'en' : u':sewing_needle:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F958': {
        'en' : u':shallow_pan_of_food:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U00002618\U0000FE0F': {
        'en' : u':shamrock:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U00002618': {
        'en' : u':shamrock:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0001F988': {
        'en' : u':shark:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F367': {
        'en' : u':shaved_ice:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F33E': {
        'en' : u':sheaf_of_rice:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F6E1\U0000FE0F': {
        'en' : u':shield:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6E1': {
        'en' : u':shield:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000026E9\U0000FE0F': {
        'en' : u':shinto_shrine:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000026E9': {
        'en' : u':shinto_shrine:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6A2': {
        'en' : u':ship:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F320': {
        'en' : u':shooting_star:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F6CD\U0000FE0F': {
        'en' : u':shopping_bags:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6CD': {
        'en' : u':shopping_bags:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6D2': {
        'en' : u':shopping_cart:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F370': {
        'en' : u':shortcake:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FA73': {
        'en' : u':shorts:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F6BF': {
        'en' : u':shower:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F990': {
        'en' : u':shrimp:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F500': {
        'en' : u':shuffle_tracks_button:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F92B': {
        'en' : u':shushing_face:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F918': {
        'en' : u':sign_of_the_horns:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F918\U0001F3FF': {
        'en' : u':sign_of_the_horns_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F918\U0001F3FB': {
        'en' : u':sign_of_the_horns_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F918\U0001F3FE': {
        'en' : u':sign_of_the_horns_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F918\U0001F3FC': {
        'en' : u':sign_of_the_horns_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F918\U0001F3FD': {
        'en' : u':sign_of_the_horns_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F9D1\U0000200D\U0001F3A4': {
        'en' : u':singer:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F3A4': {
        'en' : u':singer_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F3A4': {
        'en' : u':singer_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F3A4': {
        'en' : u':singer_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F3A4': {
        'en' : u':singer_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F3A4': {
        'en' : u':singer_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F561': {
        'en' : u':six-thirty:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F555': {
        'en' : u':six_o’clock:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F6F9': {
        'en' : u':skateboard:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U000026F7\U0000FE0F': {
        'en' : u':skier:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000026F7': {
        'en' : u':skier:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3BF': {
        'en' : u':skis:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F480': {
        'en' : u':skull:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00002620\U0000FE0F': {
        'en' : u':skull_and_crossbones:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U00002620': {
        'en' : u':skull_and_crossbones:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0001F9A8': {
        'en' : u':skunk:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F6F7': {
        'en' : u':sled:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F634': {
        'en' : u':sleeping_face:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F62A': {
        'en' : u':sleepy_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F641': {
        'en' : u':slightly_frowning_face:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F642': {
        'en' : u':slightly_smiling_face:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3B0': {
        'en' : u':slot_machine:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9A5': {
        'en' : u':sloth:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F6E9\U0000FE0F': {
        'en' : u':small_airplane:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6E9': {
        'en' : u':small_airplane:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F539': {
        'en' : u':small_blue_diamond:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F538': {
        'en' : u':small_orange_diamond:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F63B': {
        'en' : u':smiling_cat_with_heart-eyes:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0000263A\U0000FE0F': {
        'en' : u':smiling_face:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0000263A': {
        'en' : u':smiling_face:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F607': {
        'en' : u':smiling_face_with_halo:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F60D': {
        'en' : u':smiling_face_with_heart-eyes:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F970': {
        'en' : u':smiling_face_with_hearts:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F608': {
        'en' : u':smiling_face_with_horns:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F917': {
        'en' : u':smiling_face_with_open_hands:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F60A': {
        'en' : u':smiling_face_with_smiling_eyes:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F60E': {
        'en' : u':smiling_face_with_sunglasses:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F972': {
        'en' : u':smiling_face_with_tear:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F60F': {
        'en' : u':smirking_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F40C': {
        'en' : u':snail:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F40D': {
        'en' : u':snake:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F927': {
        'en' : u':sneezing_face:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F3D4\U0000FE0F': {
        'en' : u':snow-capped_mountain:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3D4': {
        'en' : u':snow-capped_mountain:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3C2': {
        'en' : u':snowboarder:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F3C2\U0001F3FF': {
        'en' : u':snowboarder_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3C2\U0001F3FB': {
        'en' : u':snowboarder_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3C2\U0001F3FE': {
        'en' : u':snowboarder_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3C2\U0001F3FC': {
        'en' : u':snowboarder_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3C2\U0001F3FD': {
        'en' : u':snowboarder_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U00002744\U0000FE0F': {
        'en' : u':snowflake:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002744': {
        'en' : u':snowflake:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002603\U0000FE0F': {
        'en' : u':snowman:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U00002603': {
        'en' : u':snowman:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000026C4': {
        'en' : u':snowman_without_snow:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F9FC': {
        'en' : u':soap:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U000026BD': {
        'en' : u':soccer_ball:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F9E6': {
        'en' : u':socks:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F366': {
        'en' : u':soft_ice_cream:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F94E': {
        'en' : u':softball:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U00002660\U0000FE0F': {
        'en' : u':spade_suit:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002660': {
        'en' : u':spade_suit:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F35D': {
        'en' : u':spaghetti:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00002747\U0000FE0F': {
        'en' : u':sparkle:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002747': {
        'en' : u':sparkle:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F387': {
        'en' : u':sparkler:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U00002728': {
        'en' : u':sparkles:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F496': {
        'en' : u':sparkling_heart:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F64A': {
        'en' : u':speak-no-evil_monkey:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F50A': {
        'en' : u':speaker_high_volume:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F508': {
        'en' : u':speaker_low_volume:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F509': {
        'en' : u':speaker_medium_volume:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F5E3\U0000FE0F': {
        'en' : u':speaking_head:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5E3': {
        'en' : u':speaking_head:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F4AC': {
        'en' : u':speech_balloon:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F6A4': {
        'en' : u':speedboat:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F577\U0000FE0F': {
        'en' : u':spider:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F577': {
        'en' : u':spider:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F578\U0000FE0F': {
        'en' : u':spider_web:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F578': {
        'en' : u':spider_web:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5D3\U0000FE0F': {
        'en' : u':spiral_calendar:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5D3': {
        'en' : u':spiral_calendar:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5D2\U0000FE0F': {
        'en' : u':spiral_notepad:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5D2': {
        'en' : u':spiral_notepad:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F41A': {
        'en' : u':spiral_shell:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9FD': {
        'en' : u':sponge:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F944': {
        'en' : u':spoon:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F699': {
        'en' : u':sport_utility_vehicle:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3C5': {
        'en' : u':sports_medal:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F433': {
        'en' : u':spouting_whale:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F991': {
        'en' : u':squid:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F61D': {
        'en' : u':squinting_face_with_tongue:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3DF\U0000FE0F': {
        'en' : u':stadium:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3DF': {
        'en' : u':stadium:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U00002B50': {
        'en' : u':star:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F929': {
        'en' : u':star-struck:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0000262A\U0000FE0F': {
        'en' : u':star_and_crescent:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0000262A': {
        'en' : u':star_and_crescent:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U00002721\U0000FE0F': {
        'en' : u':star_of_David:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U00002721': {
        'en' : u':star_of_David:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F689': {
        'en' : u':station:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F35C': {
        'en' : u':steaming_bowl:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FA7A': {
        'en' : u':stethoscope:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U000023F9\U0000FE0F': {
        'en' : u':stop_button:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000023F9': {
        'en' : u':stop_button:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F6D1': {
        'en' : u':stop_sign:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U000023F1\U0000FE0F': {
        'en' : u':stopwatch:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U000023F1': {
        'en' : u':stopwatch:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0001F4CF': {
        'en' : u':straight_ruler:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F353': {
        'en' : u':strawberry:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9D1\U0000200D\U0001F393': {
        'en' : u':student:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F393': {
        'en' : u':student_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F393': {
        'en' : u':student_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F393': {
        'en' : u':student_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F393': {
        'en' : u':student_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F393': {
        'en' : u':student_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F399\U0000FE0F': {
        'en' : u':studio_microphone:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F399': {
        'en' : u':studio_microphone:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F959': {
        'en' : u':stuffed_flatbread:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U00002600\U0000FE0F': {
        'en' : u':sun:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002600': {
        'en' : u':sun:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000026C5': {
        'en' : u':sun_behind_cloud:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F325\U0000FE0F': {
        'en' : u':sun_behind_large_cloud:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F325': {
        'en' : u':sun_behind_large_cloud:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F326\U0000FE0F': {
        'en' : u':sun_behind_rain_cloud:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F326': {
        'en' : u':sun_behind_rain_cloud:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F324\U0000FE0F': {
        'en' : u':sun_behind_small_cloud:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F324': {
        'en' : u':sun_behind_small_cloud:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F31E': {
        'en' : u':sun_with_face:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F33B': {
        'en' : u':sunflower:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F576\U0000FE0F': {
        'en' : u':sunglasses:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F576': {
        'en' : u':sunglasses:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F305': {
        'en' : u':sunrise:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F304': {
        'en' : u':sunrise_over_mountains:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F307': {
        'en' : u':sunset:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9B8': {
        'en' : u':superhero:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FF': {
        'en' : u':superhero_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FB': {
        'en' : u':superhero_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FE': {
        'en' : u':superhero_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FC': {
        'en' : u':superhero_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FD': {
        'en' : u':superhero_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B9': {
        'en' : u':supervillain:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FF': {
        'en' : u':supervillain_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FB': {
        'en' : u':supervillain_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FE': {
        'en' : u':supervillain_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FC': {
        'en' : u':supervillain_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FD': {
        'en' : u':supervillain_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F363': {
        'en' : u':sushi:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F69F': {
        'en' : u':suspension_railway:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F9A2': {
        'en' : u':swan:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F4A6': {
        'en' : u':sweat_droplets:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F54D': {
        'en' : u':synagogue:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F489': {
        'en' : u':syringe:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F455': {
        'en' : u':t-shirt:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F32E': {
        'en' : u':taco:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F961': {
        'en' : u':takeout_box:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001FAD4': {
        'en' : u':tamale:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F38B': {
        'en' : u':tanabata_tree:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F34A': {
        'en' : u':tangerine:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F695': {
        'en' : u':taxi:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9D1\U0000200D\U0001F3EB': {
        'en' : u':teacher:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F3EB': {
        'en' : u':teacher_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F3EB': {
        'en' : u':teacher_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F3EB': {
        'en' : u':teacher_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F3EB': {
        'en' : u':teacher_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F3EB': {
        'en' : u':teacher_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F375': {
        'en' : u':teacup_without_handle:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001FAD6': {
        'en' : u':teapot:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F4C6': {
        'en' : u':tear-off_calendar:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9D1\U0000200D\U0001F4BB': {
        'en' : u':technologist:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F4BB': {
        'en' : u':technologist_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F4BB': {
        'en' : u':technologist_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F4BB': {
        'en' : u':technologist_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F4BB': {
        'en' : u':technologist_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F4BB': {
        'en' : u':technologist_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F9F8': {
        'en' : u':teddy_bear:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0000260E\U0000FE0F': {
        'en' : u':telephone:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0000260E': {
        'en' : u':telephone:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F4DE': {
        'en' : u':telephone_receiver:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F52D': {
        'en' : u':telescope:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F4FA': {
        'en' : u':television:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F565': {
        'en' : u':ten-thirty:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F559': {
        'en' : u':ten_o’clock:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F3BE': {
        'en' : u':tennis:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U000026FA': {
        'en' : u':tent:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F9EA': {
        'en' : u':test_tube:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F321\U0000FE0F': {
        'en' : u':thermometer:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F321': {
        'en' : u':thermometer:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F914': {
        'en' : u':thinking_face:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001FA74': {
        'en' : u':thong_sandal:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F4AD': {
        'en' : u':thought_balloon:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F9F5': {
        'en' : u':thread:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F55E': {
        'en' : u':three-thirty:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F552': {
        'en' : u':three_o’clock:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F44E': {
        'en' : u':thumbs_down:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F44E\U0001F3FF': {
        'en' : u':thumbs_down_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44E\U0001F3FB': {
        'en' : u':thumbs_down_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44E\U0001F3FE': {
        'en' : u':thumbs_down_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44E\U0001F3FC': {
        'en' : u':thumbs_down_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44E\U0001F3FD': {
        'en' : u':thumbs_down_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44D': {
        'en' : u':thumbs_up:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F44D\U0001F3FF': {
        'en' : u':thumbs_up_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44D\U0001F3FB': {
        'en' : u':thumbs_up_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44D\U0001F3FE': {
        'en' : u':thumbs_up_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44D\U0001F3FC': {
        'en' : u':thumbs_up_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44D\U0001F3FD': {
        'en' : u':thumbs_up_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3AB': {
        'en' : u':ticket:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F405': {
        'en' : u':tiger:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F42F': {
        'en' : u':tiger_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U000023F2\U0000FE0F': {
        'en' : u':timer_clock:',
        'status' : fully_qualified,
        'E' : 1,
        'variant': True,
    },
    u'\U000023F2': {
        'en' : u':timer_clock:',
        'status' : unqualified,
        'E' : 1,
        'variant': True,
    },
    u'\U0001F62B': {
        'en' : u':tired_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F6BD': {
        'en' : u':toilet:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F345': {
        'en' : u':tomato:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F445': {
        'en' : u':tongue:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9F0': {
        'en' : u':toolbox:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B7': {
        'en' : u':tooth:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001FAA5': {
        'en' : u':toothbrush:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F3A9': {
        'en' : u':top_hat:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F32A\U0000FE0F': {
        'en' : u':tornado:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F32A': {
        'en' : u':tornado:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5B2\U0000FE0F': {
        'en' : u':trackball:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5B2': {
        'en' : u':trackball:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F69C': {
        'en' : u':tractor:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U00002122\U0000FE0F': {
        'en' : u':trade_mark:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002122': {
        'en' : u':trade_mark:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F686': {
        'en' : u':train:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F68A': {
        'en' : u':tram:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F68B': {
        'en' : u':tram_car:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3F3\U0000FE0F\U0000200D\U000026A7\U0000FE0F': {
        'en' : u':transgender_flag:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F3F3\U0000200D\U000026A7\U0000FE0F': {
        'en' : u':transgender_flag:',
        'status' : unqualified,
        'E' : 13
    },
    u'\U0001F3F3\U0000FE0F\U0000200D\U000026A7': {
        'en' : u':transgender_flag:',
        'status' : unqualified,
        'E' : 13
    },
    u'\U0001F3F3\U0000200D\U000026A7': {
        'en' : u':transgender_flag:',
        'status' : unqualified,
        'E' : 13
    },
    u'\U000026A7\U0000FE0F': {
        'en' : u':transgender_symbol:',
        'status' : fully_qualified,
        'E' : 13,
        'variant': True,
    },
    u'\U000026A7': {
        'en' : u':transgender_symbol:',
        'status' : unqualified,
        'E' : 13,
        'variant': True,
    },
    u'\U0001F6A9': {
        'en' : u':triangular_flag:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F4D0': {
        'en' : u':triangular_ruler:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F531': {
        'en' : u':trident_emblem:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9CC': {
        'en' : u':troll:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F68E': {
        'en' : u':trolleybus:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F3C6': {
        'en' : u':trophy:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F379': {
        'en' : u':tropical_drink:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F420': {
        'en' : u':tropical_fish:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3BA': {
        'en' : u':trumpet:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F337': {
        'en' : u':tulip:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F943': {
        'en' : u':tumbler_glass:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F983': {
        'en' : u':turkey:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F422': {
        'en' : u':turtle:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F567': {
        'en' : u':twelve-thirty:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F55B': {
        'en' : u':twelve_o’clock:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F42B': {
        'en' : u':two-hump_camel:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F55D': {
        'en' : u':two-thirty:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F495': {
        'en' : u':two_hearts:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F551': {
        'en' : u':two_o’clock:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002602\U0000FE0F': {
        'en' : u':umbrella:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U00002602': {
        'en' : u':umbrella:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000026F1\U0000FE0F': {
        'en' : u':umbrella_on_ground:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U000026F1': {
        'en' : u':umbrella_on_ground:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U00002614': {
        'en' : u':umbrella_with_rain_drops:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F612': {
        'en' : u':unamused_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F984': {
        'en' : u':unicorn:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F513': {
        'en' : u':unlocked:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002195\U0000FE0F': {
        'en' : u':up-down_arrow:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002195': {
        'en' : u':up-down_arrow:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002196\U0000FE0F': {
        'en' : u':up-left_arrow:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002196': {
        'en' : u':up-left_arrow:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002197\U0000FE0F': {
        'en' : u':up-right_arrow:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002197': {
        'en' : u':up-right_arrow:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002B06\U0000FE0F': {
        'en' : u':up_arrow:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002B06': {
        'en' : u':up_arrow:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F643': {
        'en' : u':upside-down_face:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F53C': {
        'en' : u':upwards_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9DB': {
        'en' : u':vampire:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FF': {
        'en' : u':vampire_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FB': {
        'en' : u':vampire_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FE': {
        'en' : u':vampire_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FC': {
        'en' : u':vampire_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FD': {
        'en' : u':vampire_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F6A6': {
        'en' : u':vertical_traffic_light:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F4F3': {
        'en' : u':vibration_mode:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0000270C\U0000FE0F': {
        'en' : u':victory_hand:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0000270C': {
        'en' : u':victory_hand:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0000270C\U0001F3FF': {
        'en' : u':victory_hand_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000270C\U0001F3FB': {
        'en' : u':victory_hand_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000270C\U0001F3FE': {
        'en' : u':victory_hand_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000270C\U0001F3FC': {
        'en' : u':victory_hand_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000270C\U0001F3FD': {
        'en' : u':victory_hand_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F4F9': {
        'en' : u':video_camera:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F3AE': {
        'en' : u':video_game:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F4FC': {
        'en' : u':videocassette:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3BB': {
        'en' : u':violin:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F30B': {
        'en' : u':volcano:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3D0': {
        'en' : u':volleyball:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F596': {
        'en' : u':vulcan_salute:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F596\U0001F3FF': {
        'en' : u':vulcan_salute_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F596\U0001F3FB': {
        'en' : u':vulcan_salute_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F596\U0001F3FE': {
        'en' : u':vulcan_salute_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F596\U0001F3FC': {
        'en' : u':vulcan_salute_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F596\U0001F3FD': {
        'en' : u':vulcan_salute_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F9C7': {
        'en' : u':waffle:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F318': {
        'en' : u':waning_crescent_moon:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F316': {
        'en' : u':waning_gibbous_moon:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U000026A0\U0000FE0F': {
        'en' : u':warning:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000026A0': {
        'en' : u':warning:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F5D1\U0000FE0F': {
        'en' : u':wastebasket:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5D1': {
        'en' : u':wastebasket:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0000231A': {
        'en' : u':watch:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F403': {
        'en' : u':water_buffalo:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6BE': {
        'en' : u':water_closet:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F52B': {
        'en' : u':water_pistol:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F30A': {
        'en' : u':water_wave:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F349': {
        'en' : u':watermelon:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F44B': {
        'en' : u':waving_hand:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F44B\U0001F3FF': {
        'en' : u':waving_hand_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44B\U0001F3FB': {
        'en' : u':waving_hand_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44B\U0001F3FE': {
        'en' : u':waving_hand_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44B\U0001F3FC': {
        'en' : u':waving_hand_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F44B\U0001F3FD': {
        'en' : u':waving_hand_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U00003030\U0000FE0F': {
        'en' : u':wavy_dash:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00003030': {
        'en' : u':wavy_dash:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F312': {
        'en' : u':waxing_crescent_moon:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F314': {
        'en' : u':waxing_gibbous_moon:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F640': {
        'en' : u':weary_cat:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F629': {
        'en' : u':weary_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F492': {
        'en' : u':wedding:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F40B': {
        'en' : u':whale:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F6DE': {
        'en' : u':wheel:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U00002638\U0000FE0F': {
        'en' : u':wheel_of_dharma:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U00002638': {
        'en' : u':wheel_of_dharma:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0000267F': {
        'en' : u':wheelchair_symbol:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F9AF': {
        'en' : u':white_cane:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U000026AA': {
        'en' : u':white_circle:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002755': {
        'en' : u':white_exclamation_mark:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F3F3\U0000FE0F': {
        'en' : u':white_flag:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F3F3': {
        'en' : u':white_flag:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F4AE': {
        'en' : u':white_flower:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F9B3': {
        'en' : u':white_hair:',
        'status' : component,
        'E' : 11
    },
    u'\U0001F90D': {
        'en' : u':white_heart:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U00002B1C': {
        'en' : u':white_large_square:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000025FD': {
        'en' : u':white_medium-small_square:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000025FB\U0000FE0F': {
        'en' : u':white_medium_square:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000025FB': {
        'en' : u':white_medium_square:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U00002754': {
        'en' : u':white_question_mark:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U000025AB\U0000FE0F': {
        'en' : u':white_small_square:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U000025AB': {
        'en' : u':white_small_square:',
        'status' : unqualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001F533': {
        'en' : u':white_square_button:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F940': {
        'en' : u':wilted_flower:',
        'status' : fully_qualified,
        'E' : 3
    },
    u'\U0001F390': {
        'en' : u':wind_chime:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F32C\U0000FE0F': {
        'en' : u':wind_face:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F32C': {
        'en' : u':wind_face:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001FA9F': {
        'en' : u':window:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F377': {
        'en' : u':wine_glass:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F609': {
        'en' : u':winking_face:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F61C': {
        'en' : u':winking_face_with_tongue:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F43A': {
        'en' : u':wolf:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F469': {
        'en' : u':woman:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F46B': {
        'en' : u':woman_and_man_holding_hands:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F46B\U0001F3FF': {
        'en' : u':woman_and_man_holding_hands_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':woman_and_man_holding_hands_dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':woman_and_man_holding_hands_dark_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':woman_and_man_holding_hands_dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':woman_and_man_holding_hands_dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F46B\U0001F3FB': {
        'en' : u':woman_and_man_holding_hands_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':woman_and_man_holding_hands_light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':woman_and_man_holding_hands_light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':woman_and_man_holding_hands_light_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':woman_and_man_holding_hands_light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F46B\U0001F3FE': {
        'en' : u':woman_and_man_holding_hands_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':woman_and_man_holding_hands_medium-dark_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':woman_and_man_holding_hands_medium-dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':woman_and_man_holding_hands_medium-dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':woman_and_man_holding_hands_medium-dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F46B\U0001F3FC': {
        'en' : u':woman_and_man_holding_hands_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':woman_and_man_holding_hands_medium-light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':woman_and_man_holding_hands_medium-light_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':woman_and_man_holding_hands_medium-light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FD': {
        'en' : u':woman_and_man_holding_hands_medium-light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F46B\U0001F3FD': {
        'en' : u':woman_and_man_holding_hands_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FF': {
        'en' : u':woman_and_man_holding_hands_medium_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FB': {
        'en' : u':woman_and_man_holding_hands_medium_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FE': {
        'en' : u':woman_and_man_holding_hands_medium_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FC': {
        'en' : u':woman_and_man_holding_hands_medium_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0000200D\U0001F3A8': {
        'en' : u':woman_artist:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F3A8': {
        'en' : u':woman_artist_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F3A8': {
        'en' : u':woman_artist_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F3A8': {
        'en' : u':woman_artist_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F3A8': {
        'en' : u':woman_artist_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F3A8': {
        'en' : u':woman_artist_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U0001F680': {
        'en' : u':woman_astronaut:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F680': {
        'en' : u':woman_astronaut_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F680': {
        'en' : u':woman_astronaut_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F680': {
        'en' : u':woman_astronaut_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F680': {
        'en' : u':woman_astronaut_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F680': {
        'en' : u':woman_astronaut_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U0001F9B2': {
        'en' : u':woman_bald:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9D4\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_beard:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D4\U0000200D\U00002640': {
        'en' : u':woman_beard:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F6B4\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_biking:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0000200D\U00002640': {
        'en' : u':woman_biking:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_biking_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_biking_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_biking_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_biking_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_biking_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_biking_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_biking_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_biking_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_biking_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B4\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_biking_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F471\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_blond_hair:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F471\U0000200D\U00002640': {
        'en' : u':woman_blond_hair:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U000026F9\U0000FE0F\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_bouncing_ball:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U000026F9\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_bouncing_ball:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U000026F9\U0000FE0F\U0000200D\U00002640': {
        'en' : u':woman_bouncing_ball:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U000026F9\U0000200D\U00002640': {
        'en' : u':woman_bouncing_ball:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U000026F9\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_bouncing_ball_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U000026F9\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_bouncing_ball_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U000026F9\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_bouncing_ball_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U000026F9\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_bouncing_ball_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U000026F9\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_bouncing_ball_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U000026F9\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_bouncing_ball_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U000026F9\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_bouncing_ball_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U000026F9\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_bouncing_ball_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U000026F9\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_bouncing_ball_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U000026F9\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_bouncing_ball_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F647\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_bowing:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F647\U0000200D\U00002640': {
        'en' : u':woman_bowing:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F647\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_bowing_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F647\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_bowing_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F647\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_bowing_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F647\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_bowing_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F647\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_bowing_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F647\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_bowing_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F647\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_bowing_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F647\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_bowing_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F647\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_bowing_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F647\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_bowing_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F938\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_cartwheeling:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F938\U0000200D\U00002640': {
        'en' : u':woman_cartwheeling:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F938\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_cartwheeling_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F938\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_cartwheeling_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F938\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_cartwheeling_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F938\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_cartwheeling_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F938\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_cartwheeling_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F938\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_cartwheeling_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F938\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_cartwheeling_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F938\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_cartwheeling_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F938\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_cartwheeling_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F938\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_cartwheeling_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F9D7\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_climbing:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0000200D\U00002640': {
        'en' : u':woman_climbing:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_climbing_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_climbing_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_climbing_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_climbing_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_climbing_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_climbing_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_climbing_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_climbing_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_climbing_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D7\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_climbing_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F477\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_construction_worker:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F477\U0000200D\U00002640': {
        'en' : u':woman_construction_worker:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F477\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_construction_worker_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F477\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_construction_worker_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F477\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_construction_worker_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F477\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_construction_worker_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F477\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_construction_worker_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F477\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_construction_worker_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F477\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_construction_worker_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F477\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_construction_worker_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F477\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_construction_worker_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F477\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_construction_worker_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U0001F373': {
        'en' : u':woman_cook:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F373': {
        'en' : u':woman_cook_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F373': {
        'en' : u':woman_cook_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F373': {
        'en' : u':woman_cook_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F373': {
        'en' : u':woman_cook_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F373': {
        'en' : u':woman_cook_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U0001F9B1': {
        'en' : u':woman_curly_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F483': {
        'en' : u':woman_dancing:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F483\U0001F3FF': {
        'en' : u':woman_dancing_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F483\U0001F3FB': {
        'en' : u':woman_dancing_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F483\U0001F3FE': {
        'en' : u':woman_dancing_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F483\U0001F3FC': {
        'en' : u':woman_dancing_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F483\U0001F3FD': {
        'en' : u':woman_dancing_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F469\U0001F3FF': {
        'en' : u':woman_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F9B2': {
        'en' : u':woman_dark_skin_tone_bald:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9D4\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_dark_skin_tone_beard:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D4\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_dark_skin_tone_beard:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F471\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_dark_skin_tone_blond_hair:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F471\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_dark_skin_tone_blond_hair:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F9B1': {
        'en' : u':woman_dark_skin_tone_curly_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F9B0': {
        'en' : u':woman_dark_skin_tone_red_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F9B3': {
        'en' : u':woman_dark_skin_tone_white_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F575\U0000FE0F\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_detective:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F575\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_detective:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U0001F575\U0000FE0F\U0000200D\U00002640': {
        'en' : u':woman_detective:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U0001F575\U0000200D\U00002640': {
        'en' : u':woman_detective:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U0001F575\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_detective_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F575\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_detective_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F575\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_detective_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F575\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_detective_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F575\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_detective_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F575\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_detective_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F575\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_detective_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F575\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_detective_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F575\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_detective_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F575\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_detective_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F9DD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_elf:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0000200D\U00002640': {
        'en' : u':woman_elf:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_elf_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_elf_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_elf_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_elf_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_elf_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_elf_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_elf_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_elf_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_elf_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DD\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_elf_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F926\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_facepalming:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F926\U0000200D\U00002640': {
        'en' : u':woman_facepalming:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F926\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_facepalming_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F926\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_facepalming_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F926\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_facepalming_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F926\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_facepalming_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F926\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_facepalming_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F926\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_facepalming_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F926\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_facepalming_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F926\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_facepalming_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F926\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_facepalming_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F926\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_facepalming_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U0001F3ED': {
        'en' : u':woman_factory_worker:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F3ED': {
        'en' : u':woman_factory_worker_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F3ED': {
        'en' : u':woman_factory_worker_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F3ED': {
        'en' : u':woman_factory_worker_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F3ED': {
        'en' : u':woman_factory_worker_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F3ED': {
        'en' : u':woman_factory_worker_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F9DA\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_fairy:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0000200D\U00002640': {
        'en' : u':woman_fairy:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_fairy_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_fairy_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_fairy_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_fairy_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_fairy_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_fairy_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_fairy_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_fairy_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_fairy_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DA\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_fairy_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F469\U0000200D\U0001F33E': {
        'en' : u':woman_farmer:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F33E': {
        'en' : u':woman_farmer_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F33E': {
        'en' : u':woman_farmer_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F33E': {
        'en' : u':woman_farmer_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F33E': {
        'en' : u':woman_farmer_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F33E': {
        'en' : u':woman_farmer_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U0001F37C': {
        'en' : u':woman_feeding_baby:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F37C': {
        'en' : u':woman_feeding_baby_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F37C': {
        'en' : u':woman_feeding_baby_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F37C': {
        'en' : u':woman_feeding_baby_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F37C': {
        'en' : u':woman_feeding_baby_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F37C': {
        'en' : u':woman_feeding_baby_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F469\U0000200D\U0001F692': {
        'en' : u':woman_firefighter:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F692': {
        'en' : u':woman_firefighter_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F692': {
        'en' : u':woman_firefighter_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F692': {
        'en' : u':woman_firefighter_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F692': {
        'en' : u':woman_firefighter_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F692': {
        'en' : u':woman_firefighter_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_frowning:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0000200D\U00002640': {
        'en' : u':woman_frowning:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_frowning_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_frowning_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_frowning_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_frowning_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_frowning_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_frowning_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_frowning_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_frowning_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_frowning_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64D\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_frowning_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F9DE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_genie:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DE\U0000200D\U00002640': {
        'en' : u':woman_genie:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F645\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_gesturing_NO:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F645\U0000200D\U00002640': {
        'en' : u':woman_gesturing_NO:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F645\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_gesturing_NO_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F645\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_gesturing_NO_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F645\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_gesturing_NO_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F645\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_gesturing_NO_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F645\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_gesturing_NO_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F645\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_gesturing_NO_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F645\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_gesturing_NO_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F645\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_gesturing_NO_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F645\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_gesturing_NO_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F645\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_gesturing_NO_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F646\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_gesturing_OK:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F646\U0000200D\U00002640': {
        'en' : u':woman_gesturing_OK:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F646\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_gesturing_OK_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F646\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_gesturing_OK_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F646\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_gesturing_OK_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F646\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_gesturing_OK_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F646\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_gesturing_OK_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F646\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_gesturing_OK_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F646\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_gesturing_OK_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F646\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_gesturing_OK_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F646\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_gesturing_OK_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F646\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_gesturing_OK_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F487\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_getting_haircut:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F487\U0000200D\U00002640': {
        'en' : u':woman_getting_haircut:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F487\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_getting_haircut_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F487\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_getting_haircut_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F487\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_getting_haircut_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F487\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_getting_haircut_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F487\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_getting_haircut_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F487\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_getting_haircut_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F487\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_getting_haircut_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F487\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_getting_haircut_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F487\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_getting_haircut_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F487\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_getting_haircut_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F486\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_getting_massage:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F486\U0000200D\U00002640': {
        'en' : u':woman_getting_massage:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F486\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_getting_massage_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F486\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_getting_massage_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F486\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_getting_massage_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F486\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_getting_massage_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F486\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_getting_massage_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F486\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_getting_massage_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F486\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_getting_massage_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F486\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_getting_massage_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F486\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_getting_massage_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F486\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_getting_massage_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0000FE0F\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_golfing:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_golfing:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U0001F3CC\U0000FE0F\U0000200D\U00002640': {
        'en' : u':woman_golfing:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U0001F3CC\U0000200D\U00002640': {
        'en' : u':woman_golfing:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_golfing_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_golfing_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_golfing_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_golfing_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_golfing_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_golfing_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_golfing_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_golfing_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_golfing_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CC\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_golfing_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F482\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_guard:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F482\U0000200D\U00002640': {
        'en' : u':woman_guard:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F482\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_guard_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F482\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_guard_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F482\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_guard_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F482\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_guard_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F482\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_guard_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F482\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_guard_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F482\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_guard_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F482\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_guard_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F482\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_guard_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F482\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_guard_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U00002695\U0000FE0F': {
        'en' : u':woman_health_worker:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U00002695': {
        'en' : u':woman_health_worker:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002695\U0000FE0F': {
        'en' : u':woman_health_worker_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002695': {
        'en' : u':woman_health_worker_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002695\U0000FE0F': {
        'en' : u':woman_health_worker_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002695': {
        'en' : u':woman_health_worker_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002695\U0000FE0F': {
        'en' : u':woman_health_worker_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002695': {
        'en' : u':woman_health_worker_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002695\U0000FE0F': {
        'en' : u':woman_health_worker_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002695': {
        'en' : u':woman_health_worker_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002695\U0000FE0F': {
        'en' : u':woman_health_worker_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002695': {
        'en' : u':woman_health_worker_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F9D8\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_in_lotus_position:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0000200D\U00002640': {
        'en' : u':woman_in_lotus_position:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_in_lotus_position_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_in_lotus_position_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_in_lotus_position_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_in_lotus_position_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_in_lotus_position_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_in_lotus_position_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_in_lotus_position_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_in_lotus_position_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_in_lotus_position_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D8\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_in_lotus_position_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F469\U0000200D\U0001F9BD': {
        'en' : u':woman_in_manual_wheelchair:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F9BD': {
        'en' : u':woman_in_manual_wheelchair_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F9BD': {
        'en' : u':woman_in_manual_wheelchair_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F9BD': {
        'en' : u':woman_in_manual_wheelchair_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F9BD': {
        'en' : u':woman_in_manual_wheelchair_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F9BD': {
        'en' : u':woman_in_manual_wheelchair_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0000200D\U0001F9BC': {
        'en' : u':woman_in_motorized_wheelchair:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F9BC': {
        'en' : u':woman_in_motorized_wheelchair_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F9BC': {
        'en' : u':woman_in_motorized_wheelchair_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F9BC': {
        'en' : u':woman_in_motorized_wheelchair_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F9BC': {
        'en' : u':woman_in_motorized_wheelchair_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F9BC': {
        'en' : u':woman_in_motorized_wheelchair_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9D6\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_in_steamy_room:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0000200D\U00002640': {
        'en' : u':woman_in_steamy_room:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_in_steamy_room_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_in_steamy_room_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_in_steamy_room_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_in_steamy_room_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_in_steamy_room_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_in_steamy_room_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_in_steamy_room_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_in_steamy_room_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_in_steamy_room_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D6\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_in_steamy_room_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F935\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_in_tuxedo:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F935\U0000200D\U00002640': {
        'en' : u':woman_in_tuxedo:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F935\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_in_tuxedo_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F935\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_in_tuxedo_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F935\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_in_tuxedo_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F935\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_in_tuxedo_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F935\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_in_tuxedo_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F935\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_in_tuxedo_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F935\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_in_tuxedo_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F935\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_in_tuxedo_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F935\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_in_tuxedo_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F935\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_in_tuxedo_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F469\U0000200D\U00002696\U0000FE0F': {
        'en' : u':woman_judge:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U00002696': {
        'en' : u':woman_judge:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002696\U0000FE0F': {
        'en' : u':woman_judge_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002696': {
        'en' : u':woman_judge_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002696\U0000FE0F': {
        'en' : u':woman_judge_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002696': {
        'en' : u':woman_judge_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002696\U0000FE0F': {
        'en' : u':woman_judge_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002696': {
        'en' : u':woman_judge_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002696\U0000FE0F': {
        'en' : u':woman_judge_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002696': {
        'en' : u':woman_judge_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002696\U0000FE0F': {
        'en' : u':woman_judge_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002696': {
        'en' : u':woman_judge_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F939\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_juggling:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F939\U0000200D\U00002640': {
        'en' : u':woman_juggling:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F939\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_juggling_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F939\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_juggling_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F939\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_juggling_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F939\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_juggling_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F939\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_juggling_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F939\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_juggling_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F939\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_juggling_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F939\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_juggling_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F939\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_juggling_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F939\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_juggling_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F9CE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_kneeling:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0000200D\U00002640': {
        'en' : u':woman_kneeling:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_kneeling_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_kneeling_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_kneeling_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_kneeling_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_kneeling_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_kneeling_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_kneeling_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_kneeling_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_kneeling_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CE\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_kneeling_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F3CB\U0000FE0F\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_lifting_weights:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_lifting_weights:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U0001F3CB\U0000FE0F\U0000200D\U00002640': {
        'en' : u':woman_lifting_weights:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U0001F3CB\U0000200D\U00002640': {
        'en' : u':woman_lifting_weights:',
        'status' : unqualified,
        'E' : 4
    },
    u'\U0001F3CB\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_lifting_weights_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CB\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_lifting_weights_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CB\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_lifting_weights_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CB\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_lifting_weights_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CB\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_lifting_weights_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CB\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_lifting_weights_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CB\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_lifting_weights_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CB\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_lifting_weights_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CB\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_lifting_weights_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CB\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_lifting_weights_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FB': {
        'en' : u':woman_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F9B2': {
        'en' : u':woman_light_skin_tone_bald:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9D4\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_light_skin_tone_beard:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D4\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_light_skin_tone_beard:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F471\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_light_skin_tone_blond_hair:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F471\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_light_skin_tone_blond_hair:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F9B1': {
        'en' : u':woman_light_skin_tone_curly_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F9B0': {
        'en' : u':woman_light_skin_tone_red_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F9B3': {
        'en' : u':woman_light_skin_tone_white_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9D9\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_mage:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0000200D\U00002640': {
        'en' : u':woman_mage:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_mage_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_mage_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_mage_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_mage_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_mage_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_mage_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_mage_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_mage_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_mage_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D9\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_mage_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F469\U0000200D\U0001F527': {
        'en' : u':woman_mechanic:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F527': {
        'en' : u':woman_mechanic_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F527': {
        'en' : u':woman_mechanic_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F527': {
        'en' : u':woman_mechanic_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F527': {
        'en' : u':woman_mechanic_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F527': {
        'en' : u':woman_mechanic_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FE': {
        'en' : u':woman_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F9B2': {
        'en' : u':woman_medium-dark_skin_tone_bald:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9D4\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_medium-dark_skin_tone_beard:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D4\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_medium-dark_skin_tone_beard:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F471\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_medium-dark_skin_tone_blond_hair:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F471\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_medium-dark_skin_tone_blond_hair:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F9B1': {
        'en' : u':woman_medium-dark_skin_tone_curly_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F9B0': {
        'en' : u':woman_medium-dark_skin_tone_red_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F9B3': {
        'en' : u':woman_medium-dark_skin_tone_white_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F469\U0001F3FC': {
        'en' : u':woman_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F9B2': {
        'en' : u':woman_medium-light_skin_tone_bald:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9D4\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_medium-light_skin_tone_beard:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D4\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_medium-light_skin_tone_beard:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F471\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_medium-light_skin_tone_blond_hair:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F471\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_medium-light_skin_tone_blond_hair:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F9B1': {
        'en' : u':woman_medium-light_skin_tone_curly_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F9B0': {
        'en' : u':woman_medium-light_skin_tone_red_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F9B3': {
        'en' : u':woman_medium-light_skin_tone_white_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F469\U0001F3FD': {
        'en' : u':woman_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F9B2': {
        'en' : u':woman_medium_skin_tone_bald:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9D4\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_medium_skin_tone_beard:',
        'status' : fully_qualified,
        'E' : 13.1
    },
    u'\U0001F9D4\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_medium_skin_tone_beard:',
        'status' : minimally_qualified,
        'E' : 13.1
    },
    u'\U0001F471\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_medium_skin_tone_blond_hair:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F471\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_medium_skin_tone_blond_hair:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F9B1': {
        'en' : u':woman_medium_skin_tone_curly_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F9B0': {
        'en' : u':woman_medium_skin_tone_red_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F9B3': {
        'en' : u':woman_medium_skin_tone_white_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F6B5\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_mountain_biking:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0000200D\U00002640': {
        'en' : u':woman_mountain_biking:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_mountain_biking_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_mountain_biking_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_mountain_biking_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_mountain_biking_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_mountain_biking_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_mountain_biking_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_mountain_biking_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_mountain_biking_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_mountain_biking_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B5\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_mountain_biking_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U0001F4BC': {
        'en' : u':woman_office_worker:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F4BC': {
        'en' : u':woman_office_worker_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F4BC': {
        'en' : u':woman_office_worker_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F4BC': {
        'en' : u':woman_office_worker_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F4BC': {
        'en' : u':woman_office_worker_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F4BC': {
        'en' : u':woman_office_worker_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U00002708\U0000FE0F': {
        'en' : u':woman_pilot:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U00002708': {
        'en' : u':woman_pilot:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002708\U0000FE0F': {
        'en' : u':woman_pilot_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FF\U0000200D\U00002708': {
        'en' : u':woman_pilot_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002708\U0000FE0F': {
        'en' : u':woman_pilot_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FB\U0000200D\U00002708': {
        'en' : u':woman_pilot_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002708\U0000FE0F': {
        'en' : u':woman_pilot_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FE\U0000200D\U00002708': {
        'en' : u':woman_pilot_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002708\U0000FE0F': {
        'en' : u':woman_pilot_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FC\U0000200D\U00002708': {
        'en' : u':woman_pilot_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002708\U0000FE0F': {
        'en' : u':woman_pilot_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FD\U0000200D\U00002708': {
        'en' : u':woman_pilot_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_playing_handball:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0000200D\U00002640': {
        'en' : u':woman_playing_handball:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_playing_handball_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_playing_handball_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_playing_handball_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_playing_handball_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_playing_handball_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_playing_handball_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_playing_handball_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_playing_handball_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_playing_handball_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93E\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_playing_handball_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_playing_water_polo:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0000200D\U00002640': {
        'en' : u':woman_playing_water_polo:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_playing_water_polo_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_playing_water_polo_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_playing_water_polo_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_playing_water_polo_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_playing_water_polo_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_playing_water_polo_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_playing_water_polo_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_playing_water_polo_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_playing_water_polo_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93D\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_playing_water_polo_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_police_officer:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0000200D\U00002640': {
        'en' : u':woman_police_officer:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_police_officer_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_police_officer_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_police_officer_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_police_officer_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_police_officer_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_police_officer_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_police_officer_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_police_officer_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_police_officer_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F46E\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_police_officer_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_pouting:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0000200D\U00002640': {
        'en' : u':woman_pouting:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_pouting_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_pouting_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_pouting_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_pouting_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_pouting_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_pouting_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_pouting_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_pouting_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_pouting_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64E\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_pouting_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_raising_hand:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0000200D\U00002640': {
        'en' : u':woman_raising_hand:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_raising_hand_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_raising_hand_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_raising_hand_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_raising_hand_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_raising_hand_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_raising_hand_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_raising_hand_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_raising_hand_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_raising_hand_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F64B\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_raising_hand_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U0001F9B0': {
        'en' : u':woman_red_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F6A3\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_rowing_boat:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0000200D\U00002640': {
        'en' : u':woman_rowing_boat:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_rowing_boat_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_rowing_boat_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_rowing_boat_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_rowing_boat_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_rowing_boat_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_rowing_boat_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_rowing_boat_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_rowing_boat_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_rowing_boat_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6A3\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_rowing_boat_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_running:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0000200D\U00002640': {
        'en' : u':woman_running:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_running_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_running_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_running_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_running_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_running_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_running_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_running_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_running_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_running_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C3\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_running_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U0001F52C': {
        'en' : u':woman_scientist:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F52C': {
        'en' : u':woman_scientist_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F52C': {
        'en' : u':woman_scientist_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F52C': {
        'en' : u':woman_scientist_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F52C': {
        'en' : u':woman_scientist_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F52C': {
        'en' : u':woman_scientist_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F937\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_shrugging:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F937\U0000200D\U00002640': {
        'en' : u':woman_shrugging:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F937\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_shrugging_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F937\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_shrugging_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F937\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_shrugging_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F937\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_shrugging_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F937\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_shrugging_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F937\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_shrugging_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F937\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_shrugging_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F937\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_shrugging_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F937\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_shrugging_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F937\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_shrugging_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U0001F3A4': {
        'en' : u':woman_singer:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F3A4': {
        'en' : u':woman_singer_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F3A4': {
        'en' : u':woman_singer_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F3A4': {
        'en' : u':woman_singer_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F3A4': {
        'en' : u':woman_singer_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F3A4': {
        'en' : u':woman_singer_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F9CD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_standing:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0000200D\U00002640': {
        'en' : u':woman_standing:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_standing_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_standing_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_standing_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_standing_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_standing_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_standing_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_standing_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_standing_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_standing_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9CD\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_standing_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 12
    },
    u'\U0001F469\U0000200D\U0001F393': {
        'en' : u':woman_student:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F393': {
        'en' : u':woman_student_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F393': {
        'en' : u':woman_student_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F393': {
        'en' : u':woman_student_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F393': {
        'en' : u':woman_student_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F393': {
        'en' : u':woman_student_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F9B8\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_superhero:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0000200D\U00002640': {
        'en' : u':woman_superhero:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_superhero_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_superhero_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_superhero_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_superhero_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_superhero_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_superhero_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_superhero_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_superhero_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_superhero_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B8\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_superhero_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_supervillain:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0000200D\U00002640': {
        'en' : u':woman_supervillain:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_supervillain_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_supervillain_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_supervillain_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_supervillain_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_supervillain_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_supervillain_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_supervillain_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_supervillain_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_supervillain_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9B9\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_supervillain_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 11
    },
    u'\U0001F3C4\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_surfing:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0000200D\U00002640': {
        'en' : u':woman_surfing:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_surfing_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_surfing_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_surfing_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_surfing_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_surfing_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_surfing_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_surfing_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_surfing_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_surfing_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3C4\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_surfing_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_swimming:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0000200D\U00002640': {
        'en' : u':woman_swimming:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_swimming_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_swimming_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_swimming_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_swimming_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_swimming_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_swimming_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_swimming_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_swimming_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_swimming_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F3CA\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_swimming_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U0001F3EB': {
        'en' : u':woman_teacher:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F3EB': {
        'en' : u':woman_teacher_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F3EB': {
        'en' : u':woman_teacher_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F3EB': {
        'en' : u':woman_teacher_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F3EB': {
        'en' : u':woman_teacher_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F3EB': {
        'en' : u':woman_teacher_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U0001F4BB': {
        'en' : u':woman_technologist:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F4BB': {
        'en' : u':woman_technologist_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F4BB': {
        'en' : u':woman_technologist_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F4BB': {
        'en' : u':woman_technologist_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F4BB': {
        'en' : u':woman_technologist_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F4BB': {
        'en' : u':woman_technologist_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F481\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_tipping_hand:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F481\U0000200D\U00002640': {
        'en' : u':woman_tipping_hand:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F481\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_tipping_hand_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F481\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_tipping_hand_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F481\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_tipping_hand_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F481\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_tipping_hand_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F481\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_tipping_hand_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F481\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_tipping_hand_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F481\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_tipping_hand_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F481\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_tipping_hand_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F481\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_tipping_hand_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F481\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_tipping_hand_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F9DB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_vampire:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0000200D\U00002640': {
        'en' : u':woman_vampire:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_vampire_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_vampire_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_vampire_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_vampire_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_vampire_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_vampire_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_vampire_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_vampire_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_vampire_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DB\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_vampire_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F6B6\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_walking:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0000200D\U00002640': {
        'en' : u':woman_walking:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_walking_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_walking_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_walking_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_walking_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_walking_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_walking_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_walking_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_walking_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_walking_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F6B6\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_walking_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F473\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_wearing_turban:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F473\U0000200D\U00002640': {
        'en' : u':woman_wearing_turban:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F473\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_wearing_turban_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F473\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_wearing_turban_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F473\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_wearing_turban_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F473\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_wearing_turban_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F473\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_wearing_turban_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F473\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_wearing_turban_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F473\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_wearing_turban_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F473\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_wearing_turban_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F473\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_wearing_turban_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F473\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_wearing_turban_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F469\U0000200D\U0001F9B3': {
        'en' : u':woman_white_hair:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F9D5': {
        'en' : u':woman_with_headscarf:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D5\U0001F3FF': {
        'en' : u':woman_with_headscarf_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D5\U0001F3FB': {
        'en' : u':woman_with_headscarf_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D5\U0001F3FE': {
        'en' : u':woman_with_headscarf_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D5\U0001F3FC': {
        'en' : u':woman_with_headscarf_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9D5\U0001F3FD': {
        'en' : u':woman_with_headscarf_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F470\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_with_veil:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F470\U0000200D\U00002640': {
        'en' : u':woman_with_veil:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F470\U0001F3FF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_with_veil_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F470\U0001F3FF\U0000200D\U00002640': {
        'en' : u':woman_with_veil_dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F470\U0001F3FB\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_with_veil_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F470\U0001F3FB\U0000200D\U00002640': {
        'en' : u':woman_with_veil_light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F470\U0001F3FE\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_with_veil_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F470\U0001F3FE\U0000200D\U00002640': {
        'en' : u':woman_with_veil_medium-dark_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F470\U0001F3FC\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_with_veil_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F470\U0001F3FC\U0000200D\U00002640': {
        'en' : u':woman_with_veil_medium-light_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F470\U0001F3FD\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_with_veil_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F470\U0001F3FD\U0000200D\U00002640': {
        'en' : u':woman_with_veil_medium_skin_tone:',
        'status' : minimally_qualified,
        'E' : 13
    },
    u'\U0001F469\U0000200D\U0001F9AF': {
        'en' : u':woman_with_white_cane:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F9AF': {
        'en' : u':woman_with_white_cane_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F9AF': {
        'en' : u':woman_with_white_cane_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F9AF': {
        'en' : u':woman_with_white_cane_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F9AF': {
        'en' : u':woman_with_white_cane_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F9AF': {
        'en' : u':woman_with_white_cane_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F9DF\U0000200D\U00002640\U0000FE0F': {
        'en' : u':woman_zombie:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F9DF\U0000200D\U00002640': {
        'en' : u':woman_zombie:',
        'status' : minimally_qualified,
        'E' : 5
    },
    u'\U0001F462': {
        'en' : u':woman’s_boot:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F45A': {
        'en' : u':woman’s_clothes:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F452': {
        'en' : u':woman’s_hat:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F461': {
        'en' : u':woman’s_sandal:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F46D': {
        'en' : u':women_holding_hands:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F46D\U0001F3FF': {
        'en' : u':women_holding_hands_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':women_holding_hands_dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':women_holding_hands_dark_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':women_holding_hands_dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':women_holding_hands_dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F46D\U0001F3FB': {
        'en' : u':women_holding_hands_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':women_holding_hands_light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':women_holding_hands_light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':women_holding_hands_light_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F469\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':women_holding_hands_light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F46D\U0001F3FE': {
        'en' : u':women_holding_hands_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':women_holding_hands_medium-dark_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':women_holding_hands_medium-dark_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':women_holding_hands_medium-dark_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':women_holding_hands_medium-dark_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F46D\U0001F3FC': {
        'en' : u':women_holding_hands_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':women_holding_hands_medium-light_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':women_holding_hands_medium-light_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':women_holding_hands_medium-light_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F469\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FD': {
        'en' : u':women_holding_hands_medium-light_skin_tone_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F46D\U0001F3FD': {
        'en' : u':women_holding_hands_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FF': {
        'en' : u':women_holding_hands_medium_skin_tone_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FB': {
        'en' : u':women_holding_hands_medium_skin_tone_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FE': {
        'en' : u':women_holding_hands_medium_skin_tone_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 12.1
    },
    u'\U0001F469\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FC': {
        'en' : u':women_holding_hands_medium_skin_tone_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F46F\U0000200D\U00002640\U0000FE0F': {
        'en' : u':women_with_bunny_ears:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F46F\U0000200D\U00002640': {
        'en' : u':women_with_bunny_ears:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F93C\U0000200D\U00002640\U0000FE0F': {
        'en' : u':women_wrestling:',
        'status' : fully_qualified,
        'E' : 4
    },
    u'\U0001F93C\U0000200D\U00002640': {
        'en' : u':women_wrestling:',
        'status' : minimally_qualified,
        'E' : 4
    },
    u'\U0001F6BA': {
        'en' : u':women’s_room:',
        'status' : fully_qualified,
        'E' : 0.6,
        'variant': True,
    },
    u'\U0001FAB5': {
        'en' : u':wood:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F974': {
        'en' : u':woozy_face:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F5FA\U0000FE0F': {
        'en' : u':world_map:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001F5FA': {
        'en' : u':world_map:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001FAB1': {
        'en' : u':worm:',
        'status' : fully_qualified,
        'E' : 13
    },
    u'\U0001F61F': {
        'en' : u':worried_face:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F381': {
        'en' : u':wrapped_gift:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F527': {
        'en' : u':wrench:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0000270D\U0000FE0F': {
        'en' : u':writing_hand:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0000270D': {
        'en' : u':writing_hand:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0000270D\U0001F3FF': {
        'en' : u':writing_hand_dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000270D\U0001F3FB': {
        'en' : u':writing_hand_light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000270D\U0001F3FE': {
        'en' : u':writing_hand_medium-dark_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000270D\U0001F3FC': {
        'en' : u':writing_hand_medium-light_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0000270D\U0001F3FD': {
        'en' : u':writing_hand_medium_skin_tone:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001FA7B': {
        'en' : u':x-ray:',
        'status' : fully_qualified,
        'E' : 14
    },
    u'\U0001F9F6': {
        'en' : u':yarn:',
        'status' : fully_qualified,
        'E' : 11
    },
    u'\U0001F971': {
        'en' : u':yawning_face:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F7E1': {
        'en' : u':yellow_circle:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F49B': {
        'en' : u':yellow_heart:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F7E8': {
        'en' : u':yellow_square:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F4B4': {
        'en' : u':yen_banknote:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0000262F\U0000FE0F': {
        'en' : u':yin_yang:',
        'status' : fully_qualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0000262F': {
        'en' : u':yin_yang:',
        'status' : unqualified,
        'E' : 0.7,
        'variant': True,
    },
    u'\U0001FA80': {
        'en' : u':yo-yo:',
        'status' : fully_qualified,
        'E' : 12
    },
    u'\U0001F92A': {
        'en' : u':zany_face:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F993': {
        'en' : u':zebra:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F910': {
        'en' : u':zipper-mouth_face:',
        'status' : fully_qualified,
        'E' : 1
    },
    u'\U0001F9DF': {
        'en' : u':zombie:',
        'status' : fully_qualified,
        'E' : 5
    },
    u'\U0001F4A4': {
        'en' : u':zzz:',
        'status' : fully_qualified,
        'E' : 0.6
    },
    u'\U0001F1E6\U0001F1FD': {
        'en' : u':Åland_Islands:',
        'status' : fully_qualified,
        'E' : 2
    },
}
