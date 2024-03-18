import plugins
			
class Pluginsupport_incident_tracker_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div id='masthead'><h1 id='apptitle'><span>SiT! Support Incident Tracker</span></h1></div>" },
			{ "version" : "/<meta name="GENERATOR" content="SiT! Support Incident Tracker v([^"]+)" \/>/" },
			{ "text" : "<div class='windowtitle'>SiT! - Login</div>" },
		]
		return(self.rules)
