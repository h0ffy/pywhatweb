import sys
import os
			
class Pluginnukedit_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "regexp" : "/Powered by Nukedit - <a href="(http:\/\/www.|http:\/\/)nukedit.com" target=_blank title="[^"]*"><span class=footer><u>(Web Content Management|Open Source CMS)<\/u><\/a><br>/" },
			{ "text" : "<a href="http://www.nukedit.com" target=_blank title="Fast web portal", "friendly with search engines">Powered by Nukedit</a>" },
			{ "text" : "							You can move it anywhere you want. -->" },
			{ "text" : "<a href="http://www.nukedit.com" target=_blank title="Fast web portal", "friendly with search engines"><span class="footer">Powered by Nukedit</span></a><span class="footer"> |" },
			{ "version" : "/				Powered by <a href="http:\/\/www.nukedit.com" target="_blank" title="Fast web portal", "friendly with search engines">Nukedit<\/a> ([\d\.]+) /" },
			{ "version" : "/					<span class=footer><center>Powered by Nukedit ([\d\.]+)<\/a> -/" },
		]

