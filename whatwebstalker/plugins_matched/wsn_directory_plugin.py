import plugins
			
class Pluginwsn_directory_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>WSN Directory Admin Login</title>" },
			{ "text" : "<title>WSN Directory Administration Panel</title>" },
			{ "version" : "/<span class="(group|topbar)" style="margin-left: 8px;">WSN Directory ([\d\.]+) Admin Login<\/span>/", "offset" : "1 },
			{ "version" : "/<span class="(group|topbar)">WSN Directory ([\d\.]+) Admin Panel<\/span>/", "offset" : "1 },
			{ "certainty" : "25", "text" : "<!-- place any jquery-dependent script tags that need to be before the /head tag in here -->" },
			{ "certainty" : "25", "regexp" : "/<div class="boxtitle" on[c|C]lick="minmax\('[a-z]+box'\)"><img src=/" },
			{ "text" : "<textarea readonly rows="20" cols="75">WSN Directory License Agreement" },
		]
		return(self.rules)
