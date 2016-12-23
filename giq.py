import requests
import sys

URL = "http://128.32.37.201:8079/api/query"

query_bindings = {}

def help(_):
	return 'Commands:\nhelp: get list of commands.\nexit: exit the program\nbind: bind a query to a shortcut\nsee <shortcut>: see the query bound to the given shortcut\nlist: list all query bindings\nurl: see the current target url\nswitch <new_url>: change the target url'

def exit(_):
	sys.exit()

def post_query(input):
	query = input[0]
	if query in query_bindings:
		query = query_bindings[query]
	req = requests.post(URL, data=query.encode())
	return req.json()

def get_url(_):
	return URL

def switch_url(input):
	global URL
	URL = input[0]

def bind(input):
	query_bindings[input[0]] = input[1]

def get_binding(input):
	return query_bindings[input[0]]

def get_all_bindings(input):
	all_bindings = ""
	length = len(query_bindings)
	if length == 0:
		return "no bindings"
		
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
	"switch": switch_url,
	"url": get_url,
	"bind": bind,
	"see": get_binding,
	"list": get_all_bindings,
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
				out = post_query(line)

			if out != None:
				print(out)
				print("")
		except KeyboardInterrupt:
			raise
		except SystemExit:
			raise
		except Exception as e:
			print(e)

interactive_loop()
