import os.path
import pickle
import pprint
import requests
import sys

URL = "http://128.32.37.201:8079/api/query"
BINDINGS_FILE = ".bindings.p"

query_bindings = {}

def startup():
	global query_bindings
	if os.path.isfile(BINDINGS_FILE):
		query_bindings = pickle.load(open(BINDINGS_FILE, "rb"))

def help(_):
	return 'Commands:\nhelp: get list of commands.\nexit: exit the program\nbind <shortcut> <query>: bind a query to a shortcut\nunbind <shortcut>: unbind a shortcut from a query\nsee <shortcut>: see the query bound to the given shortcut\nlist: list all query bindings\nclear: unbind all query bindings\nurl: see the current target url\nswitch <new_url>: change the target url'

def exit(_):
	sys.exit()

def save_bindings():
	pickle.dump(query_bindings, open(BINDINGS_FILE, "wb"))

def post_query(input):
	query = input[0]
	if query in query_bindings:
		query = query_bindings[query]
	req = requests.post(URL, data=query.encode())
	return pprint.pformat(req.json())

def get_url(_):
	return URL

def switch_url(input):
	global URL
	URL = input[0]

def bind(input):
	query_bindings[input[0]] = input[1]

def unbind(input):
	del query_bindings[input[0]]

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

def clear(input):
	query_bindings.clear()

functions = {
	"help": help,
	"exit": exit,
	"switch": switch_url,
	"url": get_url,
	"bind": bind,
	"unbind": unbind,
	"see": get_binding,
	"list": get_all_bindings,
	"clear": clear
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
			save_bindings()
			raise
		except SystemExit:
			save_bindings()
			raise
		except Exception as e:
			print(e)

startup()
interactive_loop()
