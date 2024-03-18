import plugins
			
class Pluginalt_n_mdaemon_worldclient_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div id="biglogo" align="center"><img src="LookOut/biglogo.gif" alt="WorldClient" /></div>" },
			{ "text" : "<form action="/WorldClient.dll?View=Main" target="_top" method="post" onsubmit="document.getElementById(\'Logon\').disabled=true;">" },
			{ "text" : "<form action="/WorldClient.dll?View=Main" target="_top" method="post">" },
			{ "version" : "/<strong>[\s]*MDaemon\/WorldClient v([^\s<]+) &copy; 20[\d]{2} Alt-N Technologies\.[\s]*<\/strong>/" },
			{ "version" : "/<strong><a href="http:\/\/www\.altn\.com\/Products\/MDaemon-Email-Server-Windows\/">MDaemon Messaging Server", "BlackBerry Edition<\/a>\/WorldClient v([^\s<]+) &copy; 20[\d]{2} <a href="http:\/\/www\.altn\.com">Alt-N Technologies<\/a>\.<\/strong>/", "string" : "BlackBerry Edition" },
			{ "version" : "/^WDaemon\/([\d\.]+)$/", "search" : "headers[server]" },
		]
		return(self.rules)
