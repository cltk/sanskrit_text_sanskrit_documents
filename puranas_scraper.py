import urllib
import urllib.request
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

def write_text(lines,target):

	lines=lines.split("#")
	no_sentences=0
	for l in range(len(lines)):
				line=lines[l]
				line=line.strip()

				if line!="":
					target.write(line)
					target.write("\n")
					no_sentences+=1
	return no_sentences

def get_html(url_link):
	with urllib.request.urlopen(url_link) as url:
		return url.read()
		


def get_links_books():
	links=["http://sanskritdocuments.org/doc_purana/garuDapurANa.html?lang=sa",
	       "http://sanskritdocuments.org/doc_purana/brahmapur.html?lang=sa",
	       "http://sanskritdocuments.org/doc_purana/bhagpur.html?lang=sa",
	       "http://sanskritdocuments.org/doc_purana/brahpur.html?lang=sa",
	       "http://sanskritdocuments.org/doc_purana/bhiishhmastuti.html?lang=sa",
	       "http://sanskritdocuments.org/doc_purana/skandapur.html?lang=sa"]
	directory="Puranas/"
	make_dir(directory)
	url=links[5]
	
	html=get_html(url)
	soup = BeautifulSoup(html)
	lines = soup.find('pre').text
	lines= lines.replace('<hr>', '#')
	target= open(directory+"skandapur.txt", 'w')
	print (write_text(lines,target))
if __name__ == "__main__":
	get_links_books()