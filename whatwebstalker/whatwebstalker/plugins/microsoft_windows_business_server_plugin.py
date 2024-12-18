import plugins


class Pluginmicrosoft_windows_business_server_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"version": "2003", "text": "<title>Welcome to Windows Small Business Server 2003</title>"},
			{"version": "2008", "text": "<title>Welcome to Windows Small Business Server 2008</title>"},
			{"text": "<TD id="Remote_Link" class="linkHeader"><A HREF=" / Remote">Remote Web Workplace</A></TD>"},
			{"certainty": "75", "text": "<IMG alt=" src = "images/sbslogo.gif" border = "0" width = "200" height = "55" >" },
			{ "text" : "</title><link href="signinStyle.css" rel="stylesheet" type="text/css" />", "module" : "Remote Web Workplace" },
			{ "regexp" : "/<form name="form1" method="post" action="logon\.aspx\?ReturnUrl=%2f[^"]" id="form1" autocomplete="OFF" onsubmit="OnUserNameFocus\(\);">/", "module" : "Remote Web Workplace" },
			{ "text" : "<input id="rememberMe" type="checkbox" name="rememberMe" tabindex="3" /><label for="rememberMe">Remember me on this computer</label>", "module" : "Remote Web Workplace" },
			{ "text" : "<meta name="copyright" content="Copyright (c) Microsoft Corporation.  All rights reserved." />", "module" : "Remote Web Workplace", "certainty" : "25 },
			{ "text" : "<head id="Head1"><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>", "module" : "Remote Web Workplace", "certainty" : "25 },
		]
	return(self.rules)
