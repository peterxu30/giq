from urllib import request
import sys

URL = "http://128.32.37.201:8079/api/query"

query_bindings = {}

def help(_):
	return 'Commands:\nhelp: get list of commands.\nexit: exit the program\nbind: bind a query to a shortcut\nsee <shortcut>: see the query bound to the given shortcut\nlist: list all query bindings\nurl: see the current target url\nchange <new_url>: change the target url'

def exit(_):
	sys.exit()

def post_query(input):
	query = input[0]
	if query in query_bindings:
		query = query_bindings[query]
	req = request.Request(URL, query.encode())
	resp = request.urlopen(req)
	return resp

def get_url(_):
	return URL

def change_url(input):
	global URL
	URL = input[0]

def bind(input):
	query_bindings[input[0]] = input[1]

def get_binding(input):
	return query_bindings[input[0]]

def get_all_bindings(input):
	all_bindings = ""
	length = len(query_bindings)
	for k in query_bindings:
		v = query_bindings[k]
		all_bindings += k
		all_bindings += ": "
		all_bindings += v

		if (length > 1):
			all_bindings += "\n"
		length -= 1
	return all_bindings

functions = {
	"help": help,
	"exit": exit,
	"change": change_url,
	"url": get_url,
	"bind": bind,
	"see": get_binding,
	"list": get_all_bindings,
	"query": post_query
}

def interactive_loop():
	print('Type "help" for help.')
	while True:
		try:
			line = input("> ")
			tokens = line.split(" ")
			command = tokens.pop(0)
			if command in functions:
				out = functions[command](tokens)
			else:
				out = functions["query"](line)

			if out != None:
				print(out + "\n")
		except KeyboardInterrupt:
			raise
		except SystemExit:
			raise
		except:
			print("malformed input")

interactive_loop()
