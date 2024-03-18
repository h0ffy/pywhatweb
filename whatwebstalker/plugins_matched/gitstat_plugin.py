import plugins
			
class Plugingitstat_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<a href="http:\/\/sourceforge\.net\/projects\/gitstat\/"<font size=4>\(Powered by gitstat v([^\)^\s]+)\)<\/font><\/a>/" },
			{ "text" : "<!-- FIXME: We should have some reference to the website of the git tree if available -->" },
			{ "text" : "Powered by <a href="http://sourceforge.net/projects/gitstat/">gitstat</a> <br><img src="images/separator.gif" alt=" />Design: <a href="http://www.oswd.org/">OSWD.ORG</a></p>" },
		]
			return(self.rules)
