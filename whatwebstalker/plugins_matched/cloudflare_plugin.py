import sys
import os
			
class cloudflare_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "name" : 'access restricted iframe", "text" : '<iframe frameborder="0" width="100%" height="100%" src="http://anti-virus.cloudflare.com/cdn-cgi/anti-virus-challenge?h='}
			{ "name" : 'footer", "text" : '&nbsp;&nbsp;Performance &amp; Security by <a id="FooterCloudFlare" href="https://www.cloudflare.com" target="_blank">CloudFlare</a>'}
			{ "search" : 'headers[server]", "regexp" : '/cloudflare\-nginx/", "name" : 'server header" }
			{ "search" : 'headers[set-cookie]", "regexp" : '/__cfduid/", "name" : '__cfduid cookie" }
			{ "name" : 'email address protection", "regexp" : '/\/cdn-cgi\/l\/email-protection#[a-f0-9]{36}/ }
	]
