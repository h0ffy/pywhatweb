import plugins
			
class Pluginesvon_classifieds_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- DO NOT REMOVE OR EDIT THIS LINE", "DOING SO WILL RESULT IN COPYRIGHT VIOLATIONS UNLESS YOU PURCHASED "POWERED BY" REMOVAL OPTION -->" },
			{ "regexp" : "/Powered by Esvon <a href='http:\/\/www.esvon.com\/pg\/products\/p_classifieds\/' target="_blank"[^>]+>Classifieds<\/a>/" },
		]
		return(self.rules)

