import sys
import os
			
class Plugintaskfreak_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<br>Powered by <a href="http:\/\/www.taskfreak.com">TaskFreak <\/a> v([\d\.]+) - Released on [\d\-]+ under GNU General Public License/" },
			{ "version" : "/    <a href="http:\/\/www.taskfreak.com">TaskFreak! multi user<\/a> v([\d\.]+) - Released on [\d\-]+ under GNU General Public License/" },
		]
		return(self.rules)

