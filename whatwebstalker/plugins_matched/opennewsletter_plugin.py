import plugins
			
class Pluginopennewsletter_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "This is a <a href=fsw.php>Free</a> & <a href=osd.php>Open Source</a> mailing list manager developed by <a href=selfexile.php>Self Exile</a> and distributed under the <a href=gpl.php>GPL</a>.", "string" : "Build: Self Exile" },
			{ "text" : "This is a <a href=fsw.php>Free</a> & <a href=osd.php>Open Source</a> mailing list manager developed by <a href=feedback.php>Self Exile</a> and distributed under the <a href=gpl.php>GPL</a>.", "string" : "Build: Self Exile" },
			{ "text" : "This is a Free & Open Source mailing list manager developed by <a href="http://netmeans.net">NetMeans.Net</a> and distributed under the LGPL license. This software is based on the OpenNewsletter project by <a href="http://www.selfexile.com" target="_blank">Self Exile</a>.", "string" : "Build: NetMeans.Net" },
			{ "text" : "This is a Free & Open Source mailing list manager developed by <a href="http://www.quadronet.net">Quadro Net</a> and distributed under the LGPL license. This software is based on the OpenNewsletter project by <a href="http://www.selfexile.com" target="_blank">Self Exile</a> and NmnNewsletter by <a href="http://netmeans.net">NetMeans.Net</a>.", "string" : "Build: Quadro.Net" },
		]
		return(self.rules)
