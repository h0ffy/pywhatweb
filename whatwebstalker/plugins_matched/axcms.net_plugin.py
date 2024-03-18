import plugins
			
class Pluginaxcms.net_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div style="text-align:center;width:100%;"><a href="http://axcms.net" target="_blank"><img src="http://axcms.net/upload/poweredby_150x25_13871.png" height="25" width="150" alt="Powered by AxCMS.net" style="height:25px;width:150px;border-width:0px;" /></a></div></form>" },
			{ "version" : "/<meta name="GENERATOR" content="AxCMS.net ver([\d\.]{1,15})">/" },
			{ "version" : "/<meta name="GENERATOR" content="AxCMS.net ([\d\.]{1,15})" \/>/" },
			{ "version" : "/<!-- Generated by AxCMS.net ([\d\.]{1,15}) -->/" },
			{ "text" : "<!-- Build and published by AxCMS.net | powered by Axinom-->" },
		]
	return(self.rules)

