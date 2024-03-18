import plugins
			
class Plugindli_lpc_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Power Controller </title>" },
			{ "text" : "<FORM NAME="login" ID="login" ACTION="/login.tgi" METHOD=post>" },
			{ "text" : "<FORM NAME="secin" ID="secin" ACTION="/login.tgi" METHOD=post>" },
			{ "text" : "<tr><td align=center><h1>Warning: Insecure Authentication</h1></td></tr>" },
			{ "text" : "<TD><INPUT onClick="calcResponse(); return false;" TYPE="Submit" NAME="Submitbtn" VALUE="OK">" },
		]
	return(self.rules)
