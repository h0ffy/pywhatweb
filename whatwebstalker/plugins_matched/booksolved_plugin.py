import sys
import os
			
class booksolved_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<!-- BOOKSolved - Copyright by www.usolved.net -->' }
			{ "version" : '/<!-- BOOKSolved v([^\s]+)- Copyright by www\.usolved\.net -->/ }
			{ "version" : '/<tr><td style="text-align: center;">[\s]*BOOKSolved ([^\s]+) &copy; by <a href="http:\/\/www\.usolved\.net" (target="_blank" )?class="menu">USOLVED<\/a>/ }
	]

