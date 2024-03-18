import sys
import os
			
class tbdev_yse_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<!-- /////// Top Navigation Menu for unregistered-->' }
			{ "text" : '<!-- /////////// here we go", "with the menu //////////// -->' }
			{ "version" : '/Powered by <a href="(http:\/\/)?(www\.tbdev\.net|bit-torrent\.kiev\.ua\/)" target="_blank" style="cursor: help;" title="[^"]*" class="copyright">TBDev<\/a> v([\d\.]+) /", "offset" : '2 }
		]

