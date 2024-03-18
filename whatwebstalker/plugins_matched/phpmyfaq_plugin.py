import sys
import os
			
class phpmyfaq_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<meta name="generator" content="phpMyFAQ ([\d\.]+)" \/>/" },
			{ "version" : "/<p id="copyrightnote">powered by <a href="http:\/\/www.phpmyfaq.de[\/]*" target="_blank">phpMyFAQ<\/a> ([\d\.]+)/" },
			{ "md5" : "8390bf2d1fe24799bbd381d1b7d6d00b", "url" : "template/favicon.ico" },
			{ "md5" : "8390bf2d1fe24799bbd381d1b7d6d00b", "url" : "template/default/favicon.ico" },
		]

