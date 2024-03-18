import plugins
			
class Pluginwacintaki_poteto_bbs_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<a href="http:\/\/www\.NineChime\.com\/products\/" title="Get your own free BBS!">Wacintaki ([^\s^<]+)<\/a> by Waccoon/" },
			{ "regexp" : "/<div align="center">OekakiPoteto v([^\s]+) by <a href="http:\/\/suteki\.nu">RanmaGuy<\/a> and <a href="http:\/\/www\.cellosoft\.com">Marcello<\/a>/" },
			{ "text" : "OekakiPoteto 5.x by <a href="http://www.suteki.nu">RanmaGuy</a> and <a href="http://www.cellosoft.com">Marcello</a><br />" },
		]
		return(self.rules)
