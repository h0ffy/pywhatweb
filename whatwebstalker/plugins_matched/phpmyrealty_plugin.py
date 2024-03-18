import sys
import os
			
class phpmyrealty_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<!-- Main Content table : stop -->" },
			{ "text" : "Powered by <a href="http://www.phpmyrealty.com" target="_blank" style="font-size: 12px; font-family: arial">phpMyRealty Professional</a>" },
			{ "text" : "<span class="table_header_text"> &nbsp;Administrator Control Panel</span>" },
		]

