import sys
import os
			
class sourcebans_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/		<a href="http:\/\/www.sourcebans.net" target="_blank"><img src="images\/sb.png" alt="SourceBans" border="0" \/><\/a><br\/>\n		<div id="footqversion">Version ([\d\.]+) <\/div>/" },
			{ "text" : "		<a href="http://www.sourcebans.net" target="_blank"><img src="images/sb.png" alt="SourceBans" border="0" /></a><br/>" },
			{ "regexp" : "/<div class='dbg' id='[0-9a-f]{7}'><span style='font-weight:bold'>Table '[a-z]+\.sb_settings' doesn't exist<\/span> <br \/><br \/><span>SQL Query type: <\/span><span style='font-weight:bold'>EXECUTE<\/span><span><br \/><span>/" },
		]

