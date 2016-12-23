# giq
Giles Interactive Query

An interactive way to query the Giles2 interface.

##Features
giq allows you to submit queries to any Giles interface and prints the repsonses. It is nothing more than a glorified POST request maker. Allows binding of query strings to shortcuts for easy access.

##Install
1. Clone the repo.
2. Install the Requests HTTP library for Python.
3. Run `python3 qig.py`

##Commands
```
help: get list of commands.
exit: exit the program
bind: bind a query to a shortcut
see <shortcut>: see the query bound to the given shortcut\nlist: list all query bindings
url: see the current target url
switch <new_url>: change the target url
```