import plugins
			
class Pluginqlogic_sansurfer_fc_hba_manager_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- Developers should be aware that for Gecko-based browsers (NS 6.x)" },
			{ "text" : "<!---- This initializes the navigator.family object ---->" },
			{ "regexp" : "/<SCRIPT LANGUAGE="Javascript">\s+<!--\s+insertLink\("sansurfer\.jnlp",\s+"Start SANsurfer FC HBA Manager"\);/" },
		]
		return(self.rules)
