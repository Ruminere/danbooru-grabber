#!/usr/bin/python
#coding:utf-8
import os # path manipulation
import urllib.request as urllib
import requests
import sys

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
		global end_reached
		end_reached = True
		print("No images on this page.")
	else:
		url = []
		for post in streams:
			if 'file_url' in post:
				url.append(post['file_url'])
		
		# setup progress bar
		num_images = len(url)
		counter = 0
		progress_bar(counter, num_images, num_images)

		# download and update progress bar
		for address in url:
			urllib.urlretrieve(address,image_folder+tag_argv+'/'+address.split('/')[-1])
			counter = counter + 1
			progress_bar(counter, num_images, num_images)

def progress_bar(current, total, bar_length):
    bar = "■" * current + "▢" * (bar_length - current)
    print("Progress: %s %d/%d" % (bar, current, total), end="\r")
		

# ==========

end_reached = False

# create images directory if not already created
if not os.path.exists(image_folder):
	print("Making new image folder at: %s" % image_folder)
	print("This folder will be used to store all images. You may change this by editing variable \"image_folder\" inside grabber.py.\n")
	os.mkdir(image_folder)

# create tag directory if not already created
tag_input = input('Enter tags, separated by one space (for tags with more than one word, add an underscore): ')
if (len(tag_input) == 0):
	print("No tag provided. Try again.")
	sys.exit()
tag_list = tag_input.split(' ')
if len(tag_list) > 2:
	print("Too many tags provided. Maximum of 2. Try again.")
	sys.exit()
tag_argv = generate_tag_argv(tag_list)
tag_folder = image_folder+tag_argv
if not os.path.exists(tag_folder):
	print("Making new tag folder at: %s \n" % tag_folder)
	os.mkdir(tag_folder)

# number of pages
page_num = input('Enter the number of pages you want to download (to download all, simply enter a super large number): ')
if (len(page_num) == 0):
	print("No number provided. Try again.")
	sys.exit()
else:
	page_num = int(page_num)

# download
n = 1
while n <= page_num and not end_reached:
  print("\nNow downloading page %d." % n)
  grabber(tag_argv,n)
  n = n + 1

print('\nDownload successful!')