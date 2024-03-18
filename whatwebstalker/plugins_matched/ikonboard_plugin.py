import plugins
			
class Pluginikonboard_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- iB Copyright Information -->" },
			{ "version" : "/Powered by <a href="http:\/\/www.ikonboard.com" class="copyright" target='_blank'>Ikonboard<\/a> ([^\s]+) &copy; 20[\d]{2} <a href='http:\/\/www.ikonboard.com' target='_blank'>Ikonboard<\/a>/" },
			{ "version" : "/Powered by <a href="http:\/\/www.ikonboard.com">Ikonboard v([^<]+)<\/a><br>&copy; 20[\d]{2} Ikonboard.com/" },
			{ "regexp" : "/<\/td><\/tr><\/table><center><hr><p>[^<]+ [P|p]owered by Ikonboard<br>http:\/\/www.ikonboard.com<br>/" },
			{ "version" : "/<meta name="GENERATOR" content="Ikonboard ([^"]+)">/" },
			{ "certainty" : "75", "tagpattern" : "h1,/h1,pre,/pre,p,a,/a,/p" },
		]
		return(self.rules)
