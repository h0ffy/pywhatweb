import plugins
			
class Pluginibm_remote_supervisor_adapter_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<HTML><BODY bgcolor="#FFFFFF"><SCRIPT language="javascript1.2"> top.location = "/"; </SCRIPT> </BODY> </HTML>" },
			{ "regexp" : "/<FRAME scrolling="no" src="\/private\/userlogin_logo\.ssi(\?SESSID=[a-f\d]{32})?" NAME="logo_frame" marginwidth=0 marginheight=0 frameborder=no framespacing=0 noresize ALIGN="/" },
			{ "regexp" : "/<FRAME src="\/private\/userlogin_body\.ssi(\?SESSID=[a-f\d]{32})?" NAME="userlogin_body" marginwidth=20/" },
			{ "url" : "/private/userlogin_logo.ssi", "text" : "<IMG SRC="banner.jpg" WIDTH=110 HEIGHT=53 ALT="banner" >" },
			{ "search" : "headers[location]", "regexp" : "/https?:\/\/[^\/]+\/private\/testcookie\.ssi\?SESSID=[a-f\d]{32}/" },
		]
	return(self.rules)
