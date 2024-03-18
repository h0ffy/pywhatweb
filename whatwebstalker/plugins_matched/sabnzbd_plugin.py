import sys
import os
			
class Pluginsabnzbd_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/    <form action="\/sabnzbd\/[^"]*" method="POST">/" },
		]
		return(self.rules)

