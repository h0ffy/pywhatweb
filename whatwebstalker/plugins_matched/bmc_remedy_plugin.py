import sys
import os
			
class bmc_remedy_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<!-- common to all login jsps - not localized information -->' }
			{ "text" : '<!-- Added to prevent iFrame exploit. Need to comment out for portlet to work -->' }
			{ "text" : '<input type="button" name="clear" value="Clear" class="Login" onClick="clearLogin();"><!--;-->' }
			{ "text" : '<input type="button" name="clear" value="Clear" onClick="clearLogin();"><!--;-->' }
			{ "version" : '/<title>(BMC&nbsp;)?Remedy&nbsp;Mid&nbsp;Tier&nbsp;([^\s]+) - (Error page|Login)<\/title><!--;-->/", "offset" : '1 }
			{ "version" : '/<title>(BMC )?Remedy Mid Tier ([^\s]+) - (Error page|Login)<\/title>/", "offset" : '1 }
	]

