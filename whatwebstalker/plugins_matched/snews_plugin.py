import plugins
			
class Pluginsnews_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<p>This site is powered by <a href="http://snewscms.com/" title="sNews CMS" onclick="target=\'_blank\';">sNews</a>" },
			{ "text" : "powered by <a href="http://www.solucija.com/home/snews/" title="sNews">sNews</a>" },
			{ "text" : "Powered by <a href="http://snews.solucija.com" title="Single file CSS and XHTML valid CMS">sNews</a>" },
			{ "text" : "Powered by <a href="http://snewscms.com/" title="Single file CMS">sNews</a>" },
			{ "text" : "<meta name="description" content="sNews CMS" />", "certainty" : "75 },
			{ "text" : "<p><label for="uname">Username</label>:<br /><input type="text" name="uname" id="uname" class="text" value=" /></p><p><label for="pass">Password</label>:<br /><input type="password" name="pass" id="pass" class="text" value=" /></p>" },
			{ "version" : "/<meta name="Generator" content="sNews ([\d\.]+)" \/>/" },
		]
		return(self.rules)
