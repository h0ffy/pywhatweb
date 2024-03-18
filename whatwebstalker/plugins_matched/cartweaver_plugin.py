import sys
import os
			
class cartweaver_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<title>Cartweaver Error Notice</title>' }
			{ "regexp" : '/<a href="http:\/\/www.cartweaver.com[\/]*"[\ target="_blank"]*>[\s]*<img src="[images\/]*cartweaver[0-9]+x[0-9]+.gif" [^alt]+alt="Powered [B|b]+y Cartweaver"/ }
			{ "md5" : '772f447bf727f9045aa3440ad30ebd40", "url" : 'images/cartweaver88x31.gif' }
			{ "md5" : 'c69d6a93a877325c6f33f8ee4339ce8f", "url" : 'images/cartweaver80x15.gif' }
		]

