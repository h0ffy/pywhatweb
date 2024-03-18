import sys
import os
			
class ocs_inventory_ng_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<LINK REL='StyleSheet' TYPE='text/css' HREF='css/ocsreports.css'>" },
			{ "version" : '/<img src=image\/banner-ocs\.png><\/a><\/td><td width='33%' align='right'>[\s]+<b>Ver\. ([^&]+)&nbsp&nbsp&nbsp;<\/b>/ },
		]

