import sys
import os
			
class Pluginsimple_directory_listing_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name='keywords' content='simple", "directory", "listing'></meta>" },
			{ "regexp" : "/<meta name='keywords' content='simple", "directory", "listing", "\/[^\/]*\/? - Simple Directory Listing'><\/meta>/" },
			{ "text" : "<form action='?system=login' method='post' onsubmit='Sdl.login.submit(); return false;'>" },
			{ "text" : "<i><b>powered by <a href='http://simpledirectorylisting.net'>SimpleDirectoryListing</a></b></i>" },
			{ "text" : "Powered by <a href="http://sourceforge.net/simpledirectory">SimpleDirectoryListing</a>" },
		]
		return(self.rules)

