import sys
import os
			
class posterous_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<meta name="generator" content="Posterous" />' }
			{ "text" : '<div class="posterous_site_data" data-post-id="' }
			{ "account" : '/<meta property="og:site_name" content="([^"]+)'s posterous" \/>/ }
			{ "text" : '<li class="first"><a href="http://posterous.com/login?jumpto=http' }
			{ "regexp" : '/<html><body>You are being <a href="http:\/\/([^"]+)\.posterous\.com\/">redirected<\/a>\.<\/body><\/html>/ }
	]

