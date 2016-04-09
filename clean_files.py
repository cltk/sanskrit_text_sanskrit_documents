import re
import os 
import string
import regex
try:
	from bs4 import BeautifulSoup
except ImportError:
	from BeautifulSoup import BeautifulSoup

def make_dir(directory):
	if not os.path.exists(directory):
			os.makedirs(directory)	
'''
def clean_files():
	directory="Puranas/"
	path_="Puranas/bhagpur_cleaned.txt"
	target_= open(path_, 'w')

	with open(directory+"bhagpur.txt") as f:
		for line in f:
			if line.rstrip() !='':
				line=re.sub(r"[\u0966-\u096F]+", "", line)
				target_.write(line.strip()+"\n")

'''
'''
def clean_files():
	directory="Puranas/"
	path_="Puranas/brahmapur_cleaned.txt"
	target_= open(path_, 'w')

	with open(directory+"brahmapur.txt") as f:
		for line in f:
			if line.rstrip() !='':
				line=re.sub(r"[\u0966-\u096F]+", "", line)
				line=re.sub(r"[.][/]", "", line)
				line=re.sub(r"(\s)+[.]॥", "", line)
				target_.write(line.strip()+"\n")

'''

'''
def clean_files():
	directory="Puranas/"
	path_="Puranas/brahpur_cleaned.txt"
	target_= open(path_, 'w')

	with open(directory+"brahpur.txt") as f:
		for line in f:
			if line.rstrip() !='':
				line=re.sub(r"[\u0966-\u096F]+", "", line)
				line=re.sub(r"[.][/]", "", line)
				line=re.sub(r"(\s)+[.]।", "", line)
				target_.write(line.strip()+"\n")
'''
'''
def clean_files():
	directory="Puranas/"
	path_="Puranas/garuDapurANa_cleaned.txt"
	target_= open(path_, 'w')

	with open(directory+"garuDapurANa.txt") as f:
		for line in f:
			if line.rstrip() !='':
				line=re.sub(r"[\u0966-\u096F]+", "", line)
				line=re.sub(r"[.][/]", "", line)
				line=re.sub(r",. ॥", "", line)
				target_.write(line.strip()+"\n")
'''
'''
def clean_files():
	directory="Puranas/"
	path_="Puranas/bhiishhmastuti_cleaned.txt"
	target_= open(path_, 'w')

	with open(directory+"bhiishhmastuti.txt") as f:
		for line in f:
			if line.rstrip() !='':
				line=re.sub(r"[\u0966-\u096F]+", "", line)
				line=re.sub(r"[.][/]", "", line)
				line=re.sub(r"॥ ॥", "॥", line)
				target_.write(line.strip()+"\n")
'''
def clean_files():
	directory="Puranas/"
	path_="Puranas/skandapur_cleaned.txt"
	target_= open(path_, 'w')

	with open(directory+"skandapur.txt") as f:
		for line in f:
			if line.rstrip() !='':
				line=re.sub(r"[\u0966-\u096F]+", "", line)
				line=re.sub(r"[.][/]", "", line)
				line=re.sub(r"(SP)(\w)+(\s)+", "", line)
				target_.write(line.strip())

				target_.write("\n")


if __name__ == "__main__":
	clean_files()
