import plugins
			
class Plugineverfocus_cctv_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/^	If the page is not redirected", "please click <a href="\/login\.html\?[\d]{4}&1">here<\/a><br>$/" },
			{ "text" : "<!--mei20071101 input type="image" name="recMode" style="visibility:hidden" src="stoprec.gif" onclick="changeRecordMode()"-->" },
		]
		return(self.rules)

