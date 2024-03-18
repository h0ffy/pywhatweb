import plugins
			
class Pluginquick.cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "  <title>Admin - Quick.Cms - simple content management system</title>" },
			{ "text" : "    var cfLangNoWord      = "Please fill in all required fields";" },
			{ "text" : "      <div class="foot" id="powered"><a href="http://opensolution.org/">Powered by <strong>Quick.Cms</strong></a></div>" },
			{ "text" : "        LICENSE REQUIREMENTS - DONT DELETE/HIDE LINK "powered by Quick.Cms" TO www.OpenSolution.org" },
			{ "text" : "  <meta name="Author" content="OpenSolution.org" />" },
			{ "version" : "/      <div id="version"><a href="http:\/\/opensolution.org\/">Quick.Cms v([\d\.]+)<\/a><\/div>/" },
		]
	return(self.rules)
