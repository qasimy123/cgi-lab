#!/usr/bin/env python3
import cgi
import cgitb
import json
import os

from templates import login_page
cgitb.enable()

print("Content-Type: text/html\n")

print(f"<h1> Welcome! </h1><pre><code>{json.dumps(dict(os.environ), indent=4)}<code></pre><br>")
print(f"<h2>Your browser is {os.environ['HTTP_USER_AGENT']}</h2>")
print(f"<h2>Your query string is {os.environ['QUERY_STRING']}</h2>")
print(login_page())


