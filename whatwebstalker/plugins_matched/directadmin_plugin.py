import sys
import os
			
class Plugindirectadmin_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<td class=listtitle colspan=2>Please enter your Username and Password</td></tr>" },
			{ "text" : "<title>DirectAdmin Login</title>" },
			{ "text" : "*{ FONT-SIZE: 8pt; FONT-FAMILY: verdana; } b { FONT-WEIGHT: bold; } .listtitle { BACKGROUND: #425984; COLOR: #EEEEEE; white-space: nowrap; } td.list { BACKGROUND: #EEEEEE; white-space: nowrap; } </style>" },
			{ "text" : "onload=\"document.form.username.focus();if(document.form.referer.value.indexOf('#')==-1)document.form.referer.value+=location.hash;\">" },
			{ "version" : "/^DirectAdmin Daemon v([^\s]+) Registered to /", "search" : "headers[server]" },
		]
		return(self.rules)

