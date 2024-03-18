import plugins
			
class Pluginmrtg_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "name" : "Title", "regexp" : "/<TITLE>MRTG Index Page<\/TITLE>/i},
			{ "name" : "Logo in footer", "regexp" : "/HREF="http:\/\/oss.oetiker.ch\/mrtg\/"><IMG[\s]*BORDER=0 SRC="mrtg-l.png"/mi},
			{ "name" : "Logo in footer2", "regexp" : "/HREF="http:\/\/www.ee.ethz.ch\/~oetiker\/webtools\/mrtg\/">.*src=mrtg-l.png alt=MRTG/mi},
			{ "name" : "Logo image", "url" : "/mrtg-l.png", "md5" : "241244d0d8845dcad7e891e84e79d63f"},
			{ "version" : "/<title>MRTG Index Page.*version ([^<]+)<\/font><\/td>/mi},
		]
	return(self.rules)

