import sys
import os
			
class sabnzbd_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/    <form action="\/sabnzbd\/[^"]*" method="POST">/ }
	]
