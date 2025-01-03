import plugins


class Pluginoracle_siebel_crm_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"md5": "a28ebcac852795fe30d8e99a23d377c1",
			    "url": "/favicon.ico", "string": "eService"},
			{"text": "<html OT='SiebWebMainWindow'>"},
			{"text": "<p>Scripting is used to manage data interactions between the Siebel server/Web Server and the User Interface. This requires JavaScript to be enabled  in the web browser </p>"},
			{"text": "<body>The server you are trying to access is either busy or experiencing difficulties. Please close the Web browser", "open a new browser window", "and try logging in again.", "string": "Temporarily Unavailable"},
			{"text": "alert("Your session timed out because you were idle for too long.  Please log in again to resume.\nIf you had a Siebel attachment open", "your changes may have been lost.  Please save the file locally", "close it", "and reattach it to the appropriate record.");" },
			{ "text" : "<script language="javascript">top._swescript = window;</script>" },
			{ "text" : "<!-- SWELogin.swt  -->" },
			{ "text" : "<body onLoad=\"GotoUrl('start.swe?SWECmd=Start')\">", "string" : "eService" },
			{ "text" : "</form><script language="javascript">var formObj = document.forms["RedirectForHost"];formObj.SWEHo.value=top.location.hostname;formObj.submit();</script></body></html>" },
		]
	return(self.rules)
