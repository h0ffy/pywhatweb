import sys
import os
			
class wsn_forum_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<title>WSN Forum Admin Login</title>' }
			{ "text" : '<title>WSN Forum Administration Panel</title>' }
			{ "version" : '/<span class="(topbar|group)" style="margin-left: 8px;">WSN Forum ([^<]+) Admin Login<\/span>/", "offset" : '1 }
			{ "version" : '/<span class="(topbar|group)">WSN Forum ([^<]+) Admin Panel<\/span>/", "offset" : '1 }
			{ "certainty" : '25", "text" : '<!-- place any jquery-dependent script tags that need to be before the /head tag in here -->' }
			{ "certainty" : '25", "regexp" : '/<div class="boxtitle" on[c|C]lick="minmax\('[a-z]+box'\)"><img src=/ }
			{ "text" : '<textarea readonly rows="20" cols="75">WSN Forum License Agreement' }
	]

