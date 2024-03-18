import sys
import os
			
class Pluginsphider_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "regexp" : "/<html>[\s]+<head>[\s]+<title>[\s]+Sphider installation script\.[\s]+<\/title>[\s]+<LINK REL=STYLESHEET HREF="admin\.css" TYPE="text\/css">[\s]+<\/head>[\s]+<body>/" },
			{ "regexp" : "/<title>Sphider Admin Login<\/title>[\s]+<LINK REL=STYLESHEET HREF="admin\.css" TYPE="text\/css">[\s]+<\/head>/" },
		]

