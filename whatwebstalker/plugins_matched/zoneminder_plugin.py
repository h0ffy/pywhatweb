import plugins
			
class Pluginzoneminder_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "md5" : "e07c0775523271d629035dc8921dffc7", "url" : "/graphics/favicon.ico" },
			{ "text" : "<tr><td colspan="2" class="smallhead" align="center">ZoneMinder Login</td></tr>" },
			{ "string" : /<div id="monitorSummary"><a href="\?view=groups" onclick="createPopup\( '\?view=groups", "'zmGroups", "'groups' \); return\( false \);">([\d]+ Monitors)<\/a><\/div>/" },
			{ "string" : /<a href="javascript: newWindow\( '\/index\.php\?view=groups", "'zmGroups", "400", "220 \);">([\d]+ Monitors)<\/a>/" },
			{ "version" : "/Running<\/a> - <a href="\?view=version" onclick="createPopup\( '\?view=version", "'zmVersion", "'version' \); return\( false \);">v([^<^\s]+)<\/a><\/h2>/" },
			{ "version" : "/Running<\/a> - <a href="javascript: newWindow\( '\/index\.php\?view=version", "'zmVersion", "320", "140 \);">v([^<^\s]+)<\/a>/" },
			{ "search" : "headers[server]", "version" : "/^ZoneMinder Video Server\/([^\s]+)$/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/ZMSESSID=[^;]+/" },
		]
		return(self.rules)
