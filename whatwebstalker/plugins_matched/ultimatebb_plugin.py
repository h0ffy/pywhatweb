import plugins
			
class Pluginultimatebb_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "ghdb" : "filetype:cgi inurl:/ultimatebb.cgi" },
			{ "version" : "/<meta name="generator" content="UBB\.threads ([\d\.]+)" \/>/" },
			{ "version" : "/<center>Powered by <a target="_blank" style="TEXT-DECORATION: none; COLOR: #000066; FONT-SIZE: 10px" href="http:\/\/www.php121.com"><U>PHP121<\/U><\/a> v([\d\.]+)<\/center>/" },
			{ "version" : "/<a href="http:\/\/www.groupee.com\/landing\/goto\.php\?a=ubb\.classic">Powered by UBB.classic&trade;[\s]+([\d\.]+)(<!-- [\d\.]+ -->)?<\/a>/" },
		]
		return(self.rules)
