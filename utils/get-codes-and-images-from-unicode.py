#!/usr/bin/python
# coding: utf-8

#Use this to update the images and 
#Save emoji images with Apple rendering
#and create unicode_codes.txt for emoji project

import os
import urllib2
import base64
from lxml import etree

def get_html(url):
    response = urllib2.urlopen(url)
    return response.read()
    
def save_image(img_data):
    img_to_write = base64.b64decode(img_data.replace("data:image/png;base64,", ""))
    fh1 = open("images_code/%s.png" % code.replace(" ", "_"), "wb")
    fh2 = open("images_name/%s.png" % name.replace(" ", "_"), "wb")
    fh1.write(img_to_write)
    fh2.write(img_to_write)
    fh1.close()
    fh2.close()

if __name__ == "__main__":
    emoji_list_html = get_html("http://unicode.org/emoji/charts/emoji-list.html")

    tree = etree.HTML(emoji_list_html)
    rows = tree.xpath('/html/body/div[@class="main"]/table/tr')

    if not os.path.exists("images_code"):
        os.makedirs("images_code")
    if not os.path.exists("images_name"):
        os.makedirs("images_name")

    fd = open("unicode_codes.txt", "w") #copy this to unicode_codes.py

    for tr in rows:
        if tr.xpath('td[@class="code"]'):

            name = tr.xpath('td[@class="name"][1]//text()')[0]
            keywords = tr.xpath('td[@class="name"][2]//text()')[0]
            img_data = tr.xpath('td[@class="andr"]/a/img/@src')[0]
            code = tr.xpath('td[@class="code"]//text()')[0]
            _code = []
            for c in code.split(' '):
                if len(c) is 6:
                    _code.append(c.replace('+', '0000'))
                else:
                    _code.append(c.replace('+', '000'))
            code = ' '.join(_code).replace('U', '\\U')

            name = name.replace(' ', '_') \
                        .replace(':', '') \
                        .replace(',', '') \
                        .replace('“'.decode('utf-8'), '') \
                        .replace('”'.decode('utf-8'), '') \
                        .strip()
            
            #fd.write("%s\t%s\t%s\t%s.png\n" % (code, name.encode("utf8"), keywords.encode("utf8"), code.replace(" ", "_")))
            fd.write("\tu':%s:': u'%s',\n" % (name.encode("utf8"), code.replace(" ", "")))

            save_image(img_data)
            save_image(img_data)
            
    fd.close()

