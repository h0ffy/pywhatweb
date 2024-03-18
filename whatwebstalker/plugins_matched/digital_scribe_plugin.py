import sys
import os
			
class Plugindigital_scribe_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<BR><A HREF=forgot.php?Submit2=1&email=>Forgot your password</A>?" },
			{ "text" : "<IMG SRC=/DigitalScribe/images/logosmall.gif width=158 height=63 alt="Digital Scribe Logo" border=0></a>" },
			{ "version" : "/<BR><SPAN CLASS=legal>Copyright 2005-20[\d]{2} . <A HREF=http:\/\/www\.digital-scribe\.org>Digital Scribe v\.([^\s^<]+)<\/a> - All Rights Reserved<\/span>/" },
		]

