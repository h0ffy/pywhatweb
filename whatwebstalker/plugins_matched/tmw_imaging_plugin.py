import plugins
			
class Plugintmw_imaging_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/cgi-bin/img-system-status.pl?server", "version" : "/<TD>TMW Imaging Version<\/TD>\s+<TD>([^\s^<]+)<\/TD>/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/TMWImagingSession=[^;]+/" },
			{ "text" : "<!-- TMW Document Imaging -->" },
			{ "text" : "<!-- HTML Library is $Id: TmwHTML.pm" },
		]
		return(self.rules)
