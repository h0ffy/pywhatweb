import plugins
			
class Pluginmicrosoft_remote_web_workplace_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "</title><link href="signinStyle.css" rel="stylesheet" type="text/css" />" },
			{ "regexp" : "/<form name="form1" method="post" action="logon\.aspx\?ReturnUrl=%2f[^"]" id="form1" autocomplete="OFF" onsubmit="OnUserNameFocus\(\);">/" },
			{ "text" : "<input id="rememberMe" type="checkbox" name="rememberMe" tabindex="3" /><label for="rememberMe">Remember me on this computer</label>", "certainty" : "25 },
			{ "text" : "<meta name="copyright" content="Copyright (c) Microsoft Corporation.  All rights reserved." />", "certainty" : "25 },
			{ "text" : "<head id="Head1"><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>", "certainty" : "25 },
		]
	return(self.rules)

