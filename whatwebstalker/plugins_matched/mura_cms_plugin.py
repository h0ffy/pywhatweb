import plugins
			
class Pluginmura_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<meta name="generator" content="(Mura|Sava) CMS ([\d\.]+)" \/>/", "offset" : "1 },
			{ "text" : "Powered by <a href="http://www.getmura.com/">Mura CMS</a>" },
			{ "text" : "<form novalidate="novalidate" id="sendLogin" name="sendLogin" method="post" action="index.cfm?fuseaction=cLogin.main" onsubmit="javascript:if(document.sendLogin.email.value !=\'\'){return true;}else{return false;}">" },
		]
		return(self.rules)
