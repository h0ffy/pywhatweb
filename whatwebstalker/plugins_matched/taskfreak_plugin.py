import sys
import os
			
class taskfreak_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<br>Powered by <a href="http:\/\/www.taskfreak.com">TaskFreak <\/a> v([\d\.]+) - Released on [\d\-]+ under GNU General Public License/ }
			{ "version" : '/    <a href="http:\/\/www.taskfreak.com">TaskFreak! multi user<\/a> v([\d\.]+) - Released on [\d\-]+ under GNU General Public License/ }
		]

