from requests import Session
from bs4 import BeautifulSoup as bs
import re
import sys
import json


services = ['facebook', 'youtube', 'twitter', 'instagram', 'blogger', 'googleplus', 'twitch', 'reddit', 'ebay', 'wordpress', 'pinterest', 'yelp', 'slack', 'github', 'basecamp', 'tumblr', 'flickr', 'pandora', 'producthunt', 'steam', 'myspace', 'foursquare', 'okcupid', 'vimeo', 'ustream', 'etsy', 'soundcloud', 'bitbucket', 'meetup', 'cashme', 'dailymotion', 'aboutme', 'disqus', 'medium', 'behance', 'photobucket', 'bitly', 'cafemom', 'coderwall', 'fanpop', 'deviantart', 'goodreads', 'instructables', 'keybase', 'kongregate', 'livejournal', 'stumbleupon', 'angellist', 'lastfm', 'slideshare', 'tripit', 'fotolog', 'vine', 'paypal', 'dribbble', 'imgur', 'tracky', 'flipboard', 'vk', 'kik', 'codecademy', 'roblox', 'gravatar', 'trip', 'pastebin', 'coinbase', 'blipfm', 'wikipedia', 'ello', 'streamme', 'ifttt', 'webcredit', 'codementor', 'soupio', 'fiverr', 'trakt', 'hackernews', 'five00px', 'spotify', 'pof', 'houzz', 'contently', 'buzzfeed', 'tripadvisor', 'hubpages', 'scribd', 'venmo', 'canva', 'creativemarket', 'bandcamp', 'wikia', 'reverbnation', 'wattpad', 'designspiration', 'colourlovers', 'eyeem', 'kanoworld', 'askfm', 'smashcast', 'badoo', 'newgrounds', 'younow', 'patreon', 'mixcloud', 'gumroad', 'quora']


def usage():
	print("usage")


args = sys.argv
args.remove(sys.argv[0])

index = 0

if len(args) < 1:
	print("[!] ERROR: at least one argument is requiered (-u or --username)")
	usage()
	exit()

for arg in args:
	index = index + 1
	if arg == "-u" or arg == "--username":
		username = args[index]



s = Session()
r = s.get("https://namechk.com")
soup  = bs(r.text, "html.parser")

tmp_res = soup.find("input", attrs = {"name": "authenticity_token"})
authenticity_token = tmp_res['value']

p = s.post(url = "https://namechk.com", data = {"authenticity_token": authenticity_token, 'q': username})
j = json.loads(p.text)
token = j.get('valid')

chk_url = "https://namechk.com/services/check"
fat = "xwSgxU58x1nAwVbP6+mYSFLsa8zkcl2q6NcKwc8uFm+TvFbN8LaOzmLOBDKza0ShvREINUhbwwljVe30LbKcQw=="

for service in services:
	data = {"token": token, "service": service, 'fat': fat}
	chk_req = s.post(chk_url, data = data)
	try:
		jj = json.loads(chk_req.text)
		status = jj.get("status")
		if status == "available":
			print(f"[+] {service}: available")
		elif status == "failed":
			print(f'''[-] {service}: failed, failed reason: {jj.get("failed_reason")}''')
		else:
			print(f"[-] {service}: {status}")
	except:
		print(f"[-] {service}: Unknown Error")

