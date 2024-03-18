import plugins
			
class Pluginopen_admin_for_schools_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<html><head>[\s]+<title>Open Admin for Schools ([^\s]+) - [^<]+<\/title>/" },
			{ "version" : "/<tr><th style="padding:0.3em;"><span style="font-size: 120%;">[\s]+Open Admin for Schools ([^\s]+)<\/span> [^<]+ Les Richardson<\/th><\/tr>[\s]+<\/table>/" },
			{ "text" : "<form action="/cgi-bin/rptbirthday.pl" method="post" style="display:inline;">" },
			{ "text" : "</h2><!--  === Report Section ===  -->" },
			{ "text" : "<!-- End of Student Reports Section -->" },
			{ "string" : /<!--[\s]+#  Copyright 2001-(20[\d]{2}) Leslie Richardson[\s]+#  This file is part of Open Admin for Schools\./" },
		]
		return(self.rules)
