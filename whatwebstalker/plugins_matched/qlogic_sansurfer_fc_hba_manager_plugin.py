import sys
import os
			
class qlogic_sansurfer_fc_hba_manager_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<!-- Developers should be aware that for Gecko-based browsers (NS 6.x)' }
			{ "text" : '<!---- This initializes the navigator.family object ---->' }
			{ "regexp" : '/<SCRIPT LANGUAGE="Javascript">\s+<!--\s+insertLink\("sansurfer\.jnlp",\s+"Start SANsurfer FC HBA Manager"\);/ }
	]

