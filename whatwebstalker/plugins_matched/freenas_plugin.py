import sys
import os
			
class freenas_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<div id="login" data-dojo-type="dijit\.Dialog" data-dojo-props="title: "Welcome to FreeNAS&trade; ([^']+)'">/" },
			{ "version" : "/<div id="login" dojoType="dijit\.Dialog" title="Welcome to FreeNAS ([^\s]+)">/" },
			{ "text" : "<!-- THIS IS A LOGIN WEBPAGE -->" },
			{ "text" : "<a href="/" title="FreeNAS&trade;"><img src="/static/images/ui/freenas-logo.png?cache=" alt="FreeNAS&trade;" style="padding-left:10px;"/></a>" },
			{ "url" : "/static/images/ui/freenas-logo.png", "md5" : "e9f74076206e249ead75559119c028c6" },
			{ "url" : "/", "search" : "headers[location]", "regexp" : "/https?:\/\/[^\/]+\/account\/login\/\?next=\//" },
		]

