import sys
import os
			
class qr_code_panel_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<tr><td width='100%' align='center' class='small'>QR-Code Panel<a title='V[^\s^<]+ \([\d]{2}\/[\d]{2}\/[\d]{4}\)'> V([^\s^<]+)<\/a><br \/>/" },
			{ "certainty" : "75", "regexp" : "/&copy; [\d]{4} by <a href='http:\/\/www\.g0lgs\.co\.uk\/downloads\.php'>G0LGS<\/a><\/td><\/tr>/" },
		]

