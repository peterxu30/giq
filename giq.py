from urllib import request
import sys

URL = "http://128.32.37.201:8079/api/query"

def help():
	return 'Commands:\nhelp: get list of commands.\nexit: exit the program\nurl: see the current target url\nchange <new_url>: change the target url'

def post_query(query):
	req = request.Request(URL, query.encode())
	resp = request.urlopen(req)
	return resp

def get_url():
	return URL

def change_url(url):
	URL = url

functions = {
	"help": help,
	"query": post_query,
	"exit": sys.exit,
	"change": change_url,
	"url": get_url
}

def interactive_loop():
	print('Type "help" for help.')
	while True:
		try:
			line = input("> ")
			tokens = line.split(" ")
			command = tokens[0]
			if command == "help":
				out = help()
			elif command == "change":
				out = change_url(tokens[1])
			elif command == "exit":
				sys.exit()
			elif command == "url":
				out = get_url()
			else:
				out = functions["query"](line)
			print(out)
		except KeyboardInterrupt:
			raise
		except:
			print("malformed input")

interactive_loop()
