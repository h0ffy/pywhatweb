import sys
import os
			
class runcms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : "powered by RunCMS" inurl:module inurl:viewcat.php" },
			{ "version" : "/<div align='center'><a href='http:\/\/www.runcms.org\/' target='_blank'> Powered by  RunCms ([\d\.a-z]+)[^&]* &copy; [\d]{4}-[\d]{4} /" },
			{ "version" : "/<meta name="generator" content="[\s^"]*RUNCMS ([\d\.a-z]+)[^"]*"/i },
		]

