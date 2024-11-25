import plugins
			
class Pluginplaysms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "regexp" : "/<div id="wraplogin">[\s]+<table width="100%" height="100%" border="0" cellpadding="0" cellspacing="0">/" },
			{ "regexp" : "/<!--td background="https?:\/\/[^>^"]+\/plugin\/themes\/km2\/images\/header-4\.png"-->/" },
			{ "text" : "<a href='index.php?app=page&inc=register'>Register an account</a>" },
			{ "text" : "<a href='index.php?app=page&inc=forgot'>Forgot password</a>" },
		]
	return(self.rules)
