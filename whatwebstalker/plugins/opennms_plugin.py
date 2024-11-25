import plugins
			
class Pluginopennms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<h1 id="headerlogo"><a href="[^"]*index\.jsp"><img src="[^"]*images\/logo\.png" alt="OpenNMS Web Console Home"\/><\/a><\/h1>/" },
			{ "string" : /<p>\s+OpenNMS <a href="(support|help)\/about\.jsp">Copyright<\/a> &copy; 2002-(20[\d]{2})\s+/", "offset" : "1 },
			{ "regexp" : "/<p><input type="checkbox" name="_(spring|acegi)_security_remember_me"> Don't ask for my password for two weeks<\/p>/" },
		]
	return(self.rules)
