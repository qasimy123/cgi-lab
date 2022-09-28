#!/usr/bin/env python3

import templates
import cgi
import os
import secret
import cgitb
cgitb.enable()
try:
    post_data = cgi.FieldStorage()
except Exception as e:
    pass

page = None
cookies = os.environ.get("HTTP_COOKIE")
logged_in = False
for cookie in cookies.split(";"):
    if cookie.startswith("logged_in="):
        val = cookie.split("=")[1]
        if val == "True":
            logged_in = True


if logged_in:
    page = templates.secret_page(secret.username, secret.password)
else:
    if post_data.getvalue("username") is None or post_data.getvalue("password") is None:
        page = templates.login_page()
    elif post_data.getvalue("username") == secret.username and post_data.getvalue("password") == secret.password:
        page = templates.secret_page(secret.username, secret.password)
        print("Set-Cookie: logged_in=True")
    else:
        page = templates.after_login_incorrect()

result = templates._wrapper(page)
print(result)
