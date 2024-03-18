import plugins
			
class Pluginwsn_classifieds_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>WSN Classifieds Admin Login</title>" },
			{ "text" : "<title>WSN Classifieds Administration Panel</title>" },
			{ "version" : "/<span class="(topbar|group)" style="margin-left: 8px;">WSN Classifieds ([\d\.]+) Admin Login<\/span>/", "offset" : "1 },
			{ "version" : "/<span class="(topbar|group)">WSN Classifieds ([\d\.]+) Admin Panel<\/span>/", "offset" : "1 },
			{ "certainty" : "25", "text" : "<!-- place any jquery-dependent script tags that need to be before the /head tag in here -->" },
			{ "certainty" : "25", "regexp" : "/<div class="boxtitle" on[c|C]lick="minmax\('[a-z]+box'\)"><img src=/" },
			{ "text" : "<textarea readonly rows="20" cols="75">WSN Classifieds License Agreement" },
		]
		return(self.rules)

