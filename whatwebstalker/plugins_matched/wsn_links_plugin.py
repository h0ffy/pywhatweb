import plugins
			
class Pluginwsn_links_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>WSN Links Administration Panel</title>" },
			{ "version" : "/<span class="group" style="margin-left: 8px;">WSN Links ([\d\.]+) Admin Login<\/span>/" },
			{ "version" : "/<span class="group">WSN Links ([\d\.]+) Admin Panel<\/span>/" },
			{ "certainty" : "25", "text" : "<!-- place any jquery-dependent script tags that need to be before the /head tag in here -->" },
			{ "certainty" : "25", "regexp" : "/<div class="boxtitle" on[c|C]lick="minmax\('[a-z]+box'\)"><img src=/" },
			{ "text" : "<textarea readonly rows="20" cols="75">WSN Links License Agreement" },
		]
		return(self.rules)

