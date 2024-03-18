import sys
import os
			
class ez_publish_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<title>eZ publish administration</title>" },
			{ "text" : "<link rel="stylesheet" type="text/css" href="/admin/templates/ezpublish/style.css" />" },
			{ "text" : "topmargin=\"6\" marginheight=\"6\" leftmargin=\"6\" marginwidth=\"6\" onload=\"MM_preloadImages('/admin/images/ezpublish/redigerminimrk.gif','/admin/images/ezpublish/slettminimrk.gif','/admin/images/ezpublish/downloadminimrk.gif')\">" },
			{ "search" : "headers[x-powered-by]", "regexp" : "/^eZ [p|P]ublish/" },
		]

