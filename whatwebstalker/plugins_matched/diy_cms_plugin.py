import plugins
			
class Plugindiy_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by: <a href="http://www.diy-cms.com" target="_blank">DIY-CMS</a>" },
			{ "text" : "<a href="http://www.pghost.eu/14/18/diy_cms-25.html">Powered by DIY-CMS</a>" },
			{ "text" : "<title>DIY-CMS Database Error</title>" },
			{ "text" : "<p><b><a href="http://www.diy-cms.com/" target="_blank">Powered by: DIY-CMS</a></b></p></body></html>" },
			{ "text" : "<td valign='middle'><img border='0' src=\"admin_skin/default/images//admin_login.png\"></a></td>" },
			{ "version" : "/<META content="Powered by DiY-CMS ([\d\.]+) [0-9]{4} " name="description">/" },
			{ "version" : "/Powered by <a href="http:\/\/www.pghost.eu[^>]+>DIY-CMS v ([\d\.]+)<\/a>/" },
		]
			return(self.rules)
