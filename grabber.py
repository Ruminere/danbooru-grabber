#!/usr/bin/python
#coding:utf-8
import os # path manipulation
import urllib.request as urllib
import requests

status = 'not done yet'

# directory where all images will be downloaded
image_folder = './images/'

# generate tag argument to be used in url and folder creation
def generate_tag_argv(tagList):
	tag_argv = ''
	for tag in tagList:
		tag_argv = tag_argv + tag + '+'
	tag_argv = tag_argv[:-1]
	return tag_argv

# request json, get urls of pictures and download them
def grabber(tag_argv, page_num):
	r = requests.get('https://danbooru.donmai.us/posts.json?tags='+tag_argv+'&page='+str(page_num))
	streams = r.json()
	# check if all pages have been visited
	if len(streams) == 0:
		global status
		status = 'done'
	else:
		# check if directory already exists
		tag_folder = image_folder+tag_argv
		if not os.path.exists(tag_folder):
			print("Making new tag folder at: %s" % tag_folder)
			os.mkdir(tag_folder)

		url = []
		for post in streams:
			if 'file_url' in post:
				url.append(post['file_url'])
		
		num_images = len(url)
		counter = 0;
		# download
		for address in url:
			urllib.urlretrieve(address,image_folder+tag_argv+'/'+address.split('/')[-1])
			counter = counter + 1
			print("Finished image " + str(counter) + "/" + str(num_images))

# inputs
page_num = int(input('Enter the number of pages you want to download. To download all, simply enter a super large number:'))
taginput = input('Enter tags,separated by space:')
# page_num = 100
# taginput = "tansho" 

# create images directory if not already created
if not os.path.exists(image_folder):
	print("Making new image folder at: %s" % image_folder)
	os.mkdir(image_folder)

# download
n = 1
while n <= page_num and status == 'not done yet':
  tagList = taginput.split(' ')
  tag_argv = generate_tag_argv(tagList)
  grabber(tag_argv,n)
  n = n + 1
print('Download successful!')