import plugins
			
class Pluginav_arcade_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!--MUST BE INCLUDED IN ALL TEMPLATES AND UNMODIFIED UNLESS YOU HAVE PAID FOR COPYRIGHT REMOVAL-->" },
			{ "text" : "	  <!--MUST BE INCLUDED IN ALL TEMPLATES AND UNMODIFIED UNLESS YOU HAVE PAID FOR COPYRIGHT REMOVAL-->", "version" : "3.x" },
			{ "text" : "<b><span class="copytext">Powered by <a href="http://www.avscripts.net/avarcade/">AV Arcade Free Edition</a> - Copyright 2006-2010 <a href="http://www.avscripts.net">AV Scripts</a></span></b>", "version" : "Free" },
			{ "text" : "<b><span class="copytext">Powered by <a href="http://www.avscripts.net/avarcade/">AV Arcade v3</a> - Copyright 2006-2008 <a href="http://www.avscripts.net">AV Scripts</a></span></b>", "version" : "3.x" },
			{ "text" : "Powered by <a href="http://www.avscripts.net/avarcade/">AV Arcade Pro</a> - Copyright <a href="http://www.avscripts.net">AV Scripts</a> 2006-2010 <a href="http://www.avscripts.net"></a>", "version" : "Pro" },
		]
	return(self.rules)
