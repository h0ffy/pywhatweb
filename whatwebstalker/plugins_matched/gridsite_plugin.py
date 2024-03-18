import sys
import os
			
class Plugingridsite_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<a href="gridsite-admin.cgi?cmd=history&amp;file=index.html">View&nbsp;page&nbsp;history</a>" },
			{ "text" : "<a href="gridsite-admin.cgi?cmd=print&amp;file=index.html">Print&nbsp;View</a>" },
			{ "version" : "/Built with <a href="http:\/\/www.gridsite.org\/">GridSite<\/a>&nbsp;([\d\.]+)/" },
			{ "version" : "/Built with <a href="http:\/\/www.gridsite.org\/">GridSite<\/a> ([\d\.]+)/" },
			{ "text" : "<!-- start of gridsitefoot.txt -->" },
		]

