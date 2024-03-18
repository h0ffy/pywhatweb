import sys
import os
			
class Pluginocportal_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<html id="main_website_html" xmlns="http://www.w3.org/1999/xhtml"" },
			{ "text" : "<meta name="GENERATOR" content="ocPortal" />" },
			{ "version" : "/<!--\nPowered by ocPortal\n([^\n]+) version\nCopyright ocProducts Limited\nhttp:\/\/ocportal\.com\n-->/" },
			{ "version" : "/^ocPortal ([^\(]+) \(PHP/", "search" : "headers[x-powered-by]" },
			{ "name" : "ocp_session cookie", "regexp" : "/ocp_session=[\d]+;/", "search" : "headers[set-cookie]" },
		]

