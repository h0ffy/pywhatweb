import sys
import os
			
class indico_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<td class="menuConfTopCell" align="left" valign="bottom">" },
			{ "version" : "/<\/span>&nbsp;Powered by(\ CERN)? <a href="http:\/\/cern\.ch\/indico">Indico ([^<]+)<\/a>&nbsp;<span class="separator">/", "offset" : "1 },
		]

