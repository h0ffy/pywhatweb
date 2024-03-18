import plugins
			
class Plugindigioz_guestbook_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- NOTE: PLEASE DO NOT REMOVE THE BELLOW 3 LINES FROM YOUR HEADER FILE -->" },
			{ "text" : "<!-- NOTE: PLEASE DO NOT REMOVE THE ABOVE 3 LINES FROM YOUR HEADER FILE -->" },
			{ "version" : "/<title>Powered by DigiOz Guestbook Version ([\d\.]+)<\/title>/" },
			{ "version" : "/<a href="http:\/\/www\.digioz\.com"[^>]*>DigiOz (\.NET )?Guestbook Version ([\d\.]+)<br( \/)?>&copy; 20[\d]{2} DigiOz Multimedia\./", "offset" : "1 },
		]
		return(self.rules)

