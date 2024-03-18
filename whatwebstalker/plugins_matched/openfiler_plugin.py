import plugins
			
class Pluginopenfiler_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/uptime.html", "text" : "<div id="uptimeDiv" class="uptimeDiv"><span style="line-height: 10px;" id="uptimeData"></span> </div></body>" },
			{ "url" : "/uptime.html", "text" : "<body bgcolor="#4c555a" style="margin: 0; padding: 0" onload="getSysUptime()">" },
			{ "version" : "/<div><p style="font-size: 90%; color: #aaa; line-height: 14px;"><strong>Distro Release:&nbsp;<\/strong>Openfiler [EN]SA ([^\s]+)/" },
			{ "string" : /<strong>GUI Version:&nbsp;<\/strong>([^<^\s]+)<\/p><\/div>/" },
			{ "string" : /&copy; 2001 - (2[\d]{3}) <a href="http:\/\/www\.openfiler\.com\/">Openfiler<\/a>\. All rights reserved\.<br \/>/" },
		]
		return(self.rules)
