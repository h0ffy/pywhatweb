import plugins


class Pluginilient_sysaid_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "</a><u class="LookLikeLink"><span class="LookLikeLink"> by SysAid</span></u>"},
			{"account": "/<a href="ForgotPassword\.jsp\?accountid=([^\s^"]+)" style="color: #363a3d;">/" },
			{ "text" : "<p><a href="http://www.ilient.com">Help Desk Software by Ilient</a></p>" },
			{ "text" : "<p><a href="http://www.ilient.com">Help Desk Software by SysAid</a></p>" },
		]
	return(self.rules)
