import plugins
			
class Pluginilo_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Derivative Work - 1996", "1998-2000 Copyright 1996", "1998-2000 The Regents of the University of California<br>" },
			{ "regexp" : "/<title>[\s]+HP Integrated Lights-Out( [\d])?[\s]+<\/title>/" },
			{ "text" : "<a href="http://www.hp.com/servers/lights-out" target="new"><IMG height=60 src="ilo.gif" width=150 border=0 alt="Integrated Lights-Out"></a>" },
			{ "text" : "document.title="Integrated Lights Out: "+serverName;" },
			{ "text" : "<a href="http://www.hp.com/go/ilo" target="new"><IMG src="iLO2_blue.jpg" height=57 border=0 alt="Integrated Lights-Out"></a>", "version" : "2.x" },
			{ "version" : "/(\*|&copy;)[\s]{1,2}Copyright 2002,[\s]?([\d]{4}) Hewlett-Packard Development Company", "L\.P\./", "offset" : "1 },
			{ "version" : "/(\*|&copy;)[\s]{1,2}Copyright ([\d]{4}) Hewlett-Packard Development Company", "L\.P\./", "offset" : "1 },
			{ "text" : "document.title="Integrated Lights Out 2: "+serverName;", "version" : "2.x" },
		]
		return(self.rules)
