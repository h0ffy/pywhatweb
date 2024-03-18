import plugins
			
class Pluginlyris_listmanager_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<!-- page: [^,]+", "version: (Lyris )?ListManager(SQL)? (LINUX|WIN32) [^>]*version ([^-]+) - [A-Z][a-z]{2} [\d]{1,2} [\d]{4}( [\d]{2}:[\d]{2}:[\d]{2})?", "interface:/", "offset" : "3 },
			{ "os" : "/<!-- page: [^,]+", "version: (Lyris )?ListManager(SQL)? (LINUX|WIN32) [^>]*version ([^-]+) - [A-Z][a-z]{2} [\d]{1,2} [\d]{4}( [\d]{2}:[\d]{2}:[\d]{2})?", "interface:/", "offset" : "2 },
			{ "filepath" : "/<!-- this page created by: "([^'^\(]+)", "line: [\d]+", "package: "lweb' -->/" },
			{ "version" : "/<!-- (Lyris )?List[\s]*Manager (WIN32|LINUX) version ([^\/]+) (- [A-Z][a-z]{2} [\d]{1,2} [\d]{4})?( [\d]{2}:[\d]{2}:[\d]{2})?\/ lyrispg.pl version [^>]+ -->/", "offset" : "2 },
			{ "os" : "/<!-- (Lyris )?List[\s]*Manager (WIN32|LINUX) version ([^\/]+) (- [A-Z][a-z]{2} [\d]{1,2} [\d]{4})?( [\d]{2}:[\d]{2}:[\d]{2})?\/ lyrispg.pl version [^>]+ -->/", "offset" : "1 },
			{ "regexp" : "/<INPUT TYPE="hidden" NAME="check_code" VALUE="[^"^>]+">/" },
			{ "text" : "<html><h3>This Lyris ListManager Server is currently unavailable.<br>" },
			{ "text" : "<font face="Arial", "Helvetica", "sans-serif" color="#000000"><b><i>Main Menu</i></b></font><br>" },
		]
		return(self.rules)

