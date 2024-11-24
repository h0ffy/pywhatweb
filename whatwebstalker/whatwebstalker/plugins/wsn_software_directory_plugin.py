import plugins


class Pluginwsn_software_directory_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<title>WSN Software Directory Admin Login</title>"},
			{"text": "<title>WSN Software Directory Administration Panel</title>"},
			{"version": "/<span class="(topbar | group)" style="margin - left: 8px; ">WSN Software Directory ([\\d\\.]+) Admin Login<\\/span>/", "offset": "1 },
			{ "version" : "/<span class="(topbar|group)">WSN Software Directory ([\d\.]+) Admin Panel<\/span>/", "offset" : "1 },
			{ "certainty" : "25", "text" : "<!-- place any jquery-dependent script tags that need to be before the /head tag in here -->" },
			{ "certainty" : "25", "regexp" : "/<div class="boxtitle" on[c|C]lick="minmax\('[a-z]+box'\)"><img src=/" },
			{ "text" : "<textarea readonly rows="20" cols="75">WSN Software Directory License Agreement" },
		]
	return(self.rules)
