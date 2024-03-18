import sys
import os
			
class kampyle_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<script [^>]*src=["']http:\/\/cf\.kampyle\.com\/k_button\.js["'][^>]*>/i }
			{ "text" : '<!--Start Kampyle Feedback Form Button-->' }
			{ "text" : '<!--End Kampyle Feedback Form Button-->' }
		]

