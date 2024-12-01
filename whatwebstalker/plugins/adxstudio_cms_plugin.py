import plugins
			
class Pluginadxstudio_cms_plugin(plugins.Base):
    def __init__(self):
    	self.rules = []
    	
    def start(self):
        self.rules = [
			{ "name" : "Set-cookie Header", "search" : "headers[set-cookie]", "regexp" : "/anonprofile/i" },
			{ "name" : "PoweredByADX.gif", "search" : "text", "regexp" : "/PoweredByADX.gif" },
			{ "name" : "Powered by Adxstudio", "search" : "text", "regexp" : "alt=\"Powered by Adxstudio\""},
			{ "name" : "poweredbyadx.png", "search" : "text", "regexp" : "/poweredbyadx.png"},
		]
        return self.rules