import plugins
			
class Pluginavtech_video_web_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>--- VIDEO WEB SERVER ---</title>" },
			{ "text" : "<input type="button" name="Download" value="Download AP" class="button" onClick="MM_goToURL(\'parent\',\'ftp://211.22.74.18/AV732E/setup.exe\');return document.MM_returnValue" title="Download AP">", "version" : "AVC732E" },
			{ "text" : "<input type="submit" name="Download" value="Download AP" class="button" onClick="MM_goToURL(\'parent\',\'ftp://211.22.74.18/AV733/setup.exe\');return document.MM_returnValue" title="Download AP">", "version" : "AVC733" },
		]
		return(self.rules)
