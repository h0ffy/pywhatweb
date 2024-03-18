import sys
import os
			
class Pluginib_lite_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<tr class="w_r"><td class="w_n">Access code</td><td width="140" class="w_v"><input id="psw_id" type="password" maxLength="15" size="20" name="q" value="></td></tr>" },
		]

