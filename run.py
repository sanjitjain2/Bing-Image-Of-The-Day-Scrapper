#! /usr/bin/python2

#run.py - Download Bing Wallpaper Of The Day and sets it as desktop wallpaper

import requests,os,re,urllib2,time

url = 'https://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=2&mkt=en-US'

#Download the xml page
raw_xml = urllib2.urlopen(url).read()

#Extract Image URL and Image details from xml

#URL and Details pattern
image_url_detail_pattern = '<url>(.*?)</url>.+<copyright>(.*?)</copyright>'

#search for the pattern
(image_URL,image_detail) = re.search(image_url_detail_pattern, raw_xml).groups(1)

#Complete the URL
bing_URL = 'http://www.bing.com' + image_URL

#Download the image
res = requests.get(bing_URL)
res.raise_for_status()

#Name of the image
filename = bing_URL.split('/')[-1]

#Save the image
imageFile = open(os.path.join('',os.path.basename(bing_URL)),'wb')
for chunk in res.iter_content(100000000000):
	imageFile.write(chunk)
imageFile.close()

# Get Absolute Path Of Image
path = os.path.join(os.path.realpath('.'),filename)

# Command For Changing Wallpaper
cmd = 'gsettings set org.gnome.desktop.background picture-uri "file:///{}"'.format(path)
os.system(cmd)
