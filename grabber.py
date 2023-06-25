#!/usr/bin/python
#coding:utf-8
import os # path manipulation
import urllib.request as urllib
import requests

status = 'not done yet'

# directory where all images will be downloaded
danbooru_folder = './images/'

# generate tag argument to be used in url and folder creation
def generate_tag_argv(tagList):
	tag_argv = ''
	for tag in tagList:
		tag_argv = tag_argv + tag + '+'
	tag_argv = tag_argv[:-1]
	print("[0.2] tag string: %s" % tag_argv);
	return tag_argv

# request json, get urls of pictures and download them
def grabber(tag_argv, page_num):
	r = requests.get('https://danbooru.donmai.us/posts.json?tags='+tag_argv+'&page='+str(page_num))
	streams = r.json()
	# check if all pages have been visited
	print("[1] preparing to grab...")
	if len(streams) == 0:
		print("[2.1] All pictures have been downloaded!")
		global status
		status = 'done'
	else:
		# check if directory already exists
		print("[2.2] checking for directory...")
		if not os.path.exists(danbooru_folder+tag_argv):
			print("[2.2.1] creating directory...")
			os.mkdir(danbooru_folder+tag_argv)

		url = []
		for post in streams:
			if 'file_url' in post:
				url.append(post['file_url'])
		target = ['https://danbooru.donmai.us'+x for x in url]

		# download
		for address in target:
			urllib.urlretrieve(address,danbooru_folder+tag_argv+'/'+address.split('/')[-1])

# inputs
# page_num = int(input('Enter the number of pages you want to download. To download all, simply enter a super large number:'))
# taginput = input('Enter tags,separated by space:')
page_num = 100
taginput = "tansho" 

# create images directory if not already created
image_folder = "./images/"
if not os.path.exists(image_folder):
		print("[0.1] creating image directory...")
		os.mkdir(image_folder)

# download
n = 1
while n <= page_num and status == 'not done yet':
  tagList = taginput.split(' ')
  tag_argv = generate_tag_argv(tagList)
  grabber(tag_argv,n)
  n = n + 1
print('Download successful!')