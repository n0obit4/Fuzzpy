#!/usr/bin/env python3
###########################
#     Author              #
#   BY: n0obit4           #
#   11/July/2020          #
###########################

import requests,sys
from time import sleep
from colorama import Fore

def fuzz(url,file):
	header = {'User-agent': 'Mozilla/5.0'}

	with open(file) as dicc:
		file = dicc.readlines()

	print(Fore.YELLOW +"\nSearching..."+ Fore.RESET)
	for words in file:
		search = str(url+words)
		request = requests.get("{}".format(search.strip()), headers=header)
		status_code = request.status_code
		hide_code = 404
		if request.status_code != hide_code:
			print(f"Found: /{words.strip()} "+ Fore.YELLOW + " (Status: {})".format(status_code) + Fore.RESET)
		else:
			pass
	print(Fore.GREEN +"End!")

if __name__ == "__main__":
	url = sys.argv[1]
	file = sys.argv[2]
	fuzz(url,file)

