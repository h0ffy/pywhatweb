import sys
import os
			
class mura_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<meta name="generator" content="(Mura|Sava) CMS ([\d\.]+)" \/>/", "offset" : "1 },
			{ "text" : "Powered by <a href="http://www.getmura.com/">Mura CMS</a>" },
			{ "text" : "<form novalidate="novalidate" id="sendLogin" name="sendLogin" method="post" action="index.cfm?fuseaction=cLogin.main" onsubmit="javascript:if(document.sendLogin.email.value !=\'\'){return true;}else{return false;}">" },
		]

