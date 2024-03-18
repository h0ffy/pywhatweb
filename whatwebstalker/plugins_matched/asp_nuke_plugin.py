import plugins
			
class Pluginasp_nuke_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name=\"Generator\" CONTENT=\"ASP-Nuke" },
			{ "version" : "2", "text" : "<meta name=\"Generator\" content=\"ASPNUKE v2.0 - distributed under GPL license\">" },
			{ "text" : "<a href=\"http://www.rot.dk\" target=\"_blank\">Asp-Nuke</a> community" },
			{ "regexp" : "/<link rel="Shortcut Icon" href="[^>]*aspnuke.ico">/" },
			{ "regexp" : "/<a href="http:\/\/www.aspnuke.it" target="_blank">ASP-Nuke [0-9\.]*<\/a>/" },
			{ "text" : "Designed with <a href=\"http://www.asp-nuke.net\" target=\"_blank\">ASP-Nuke</a>" },
			{ "version" : "v1.1+", "text" : "<br>Designed with ASP-Nuke v1.1+" },
			{ "version" : "/<meta name="Generator" (content|CONTENT)="(ASPNUKE|ASP-Nuke) ([^->"]+)/", "offset" : "2", "name" : "meta generator tag" },
			{ "version" : "/Designed with <a href="http:\/\/www.asp-nuke.net" target="_blank">ASP-Nuke<\/a> ([^<]+)<br>/", "name" : "desgined by" },
			{ "version" : "/<a href="http:\/\/www.aspnuke.it" target="_blank">Asp-Nuke ([\d\.]+)<\/a>/", "name" : "aspnuke.it" },
			{ "name" : "P3P Privacy Headers", "certainty" : "25", "search" : "headers[p3p]", "text" : "CP=\"NOI CUR OUR IND UNI COM NAV INT\" },
		]
		return(self.rules)
