import sys
import os
			
class tmw_imaging_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "url" : '/cgi-bin/img-system-status.pl?server", "version" : '/<TD>TMW Imaging Version<\/TD>\s+<TD>([^\s^<]+)<\/TD>/ },
			{ "search" : 'headers[set-cookie]", "regexp" : '/TMWImagingSession=[^;]+/ },
			{ "text" : '<!-- TMW Document Imaging -->' },
			{ "text" : '<!-- HTML Library is $Id: TmwHTML.pm' },
		]

