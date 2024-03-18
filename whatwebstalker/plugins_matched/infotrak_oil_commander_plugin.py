import plugins
			
class Plugininfotrak_oil_commander_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Login - Powered By: Infotrak's Oil Commander</title>" },
			{ "text" : "<div id="pnlContent_Shadow" style="background-color:DarkGray;overflow:hidden;position:absolute;left:23;top:163;z-index:-1;width:98%;height:700 ;">" },
			{ "text" : "<span id="lblMessage">After entering your email address and clicking on Continue", "an email with your login details will be sent. Please allow some time for the email. If you do not receive it please contact your dealership. </span>" },
		]
		return(self.rules)

