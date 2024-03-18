import plugins
			
class Pluginposterita_pos_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<img src="images/newUI/logo.gif" alt="Powered by Posterita POS" width="133px" height="41px" border="0px"/>" },
			{ "certainty" : "75", "text" : "<!-- chooseApplication.jsp -->" },
			{ "version" : "/<div class="footer">[\s]+<div class="floatLeft">[\s]+All Contents .[\s]+Posterita 20[\d]{2}[\s]+<b>Version &nbsp;([^\s^<]+)<\/b>[\s]+<\/div>[\s]+<\/div>/" },
		]
	return(self.rules)

