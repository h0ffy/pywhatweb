import plugins
			
class Plugincollabtive_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Login @ Collabtive</title>" },
			{ "text" : "<!--<div id = "jslog" style = "color:red;position:absolute;top:60%;right:5%;width:300px;border:1px solid;background-color:grey;"></div>-->" },
			{ "text" : "<form id = "loginform" name = "loginform" method="post" action="manageuser.php?action=login"  onsubmit="return validateCompleteForm(this,\'input_error\');">" },
		]
		return(self.rules)
