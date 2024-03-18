import sys
import os
			
class ilient_sysaid_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '</a><u class="LookLikeLink"><span class="LookLikeLink"> by SysAid</span></u>' }
			{ "account" : '/<a href="ForgotPassword\.jsp\?accountid=([^\s^"]+)" style="color: #363a3d;">/ }
			{ "text" : '<p><a href="http://www.ilient.com">Help Desk Software by Ilient</a></p>' }
			{ "text" : '<p><a href="http://www.ilient.com">Help Desk Software by SysAid</a></p>' }
	]

