import sys
import os
			
class file_upload_manager_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : "75", "ghdb" : "+intitle:"File Upload Manager" "rename to" "file types allowed"" },
			{ "certainty" : "75", "text" : "<title>File Upload Manager</title>" },
			{ "text" : "<!-- Copyright (c) 2003 thepeak. Get your own copy of this free PHP script from www.mtnpeak.net -->" },
			{ "text" : "<a href="http://www.mtnpeak.net" style="text-decoration: none; color: #C0C0C0; font-size: 9px; cursor: default";>&copy; thepeak</a>" },
			{ "version" : "/<!-- File Upload Manager v([\d\.]+[^>]+) -->/" },
		]

