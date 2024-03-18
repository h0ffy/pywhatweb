import plugins
			
class Plugindigital_scribe_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<BR><A HREF=forgot.php?Submit2=1&email=>Forgot your password</A>?" },
			{ "text" : "<IMG SRC=/DigitalScribe/images/logosmall.gif width=158 height=63 alt="Digital Scribe Logo" border=0></a>" },
			{ "version" : "/<BR><SPAN CLASS=legal>Copyright 2005-20[\d]{2} . <A HREF=http:\/\/www\.digital-scribe\.org>Digital Scribe v\.([^\s^<]+)<\/a> - All Rights Reserved<\/span>/" },
		]
		return(self.rules)
