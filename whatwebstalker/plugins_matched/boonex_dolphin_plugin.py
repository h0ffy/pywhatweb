import sys
import os
			
class boonex_dolphin_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<script type="text\/javascript" language="javascript">var aDolLang = \{'_Counter': 'Counter','_PROFILE_ERR': 'Error!\\nYour username or password was incorrect\. Please try again\.'\};<\/script>/ }
			{ "text" : 'Powered by                    Dolphin - <a href="http://www.boonex.com/products/dolphin/">Free Community Software</a>' }
			{ "version" : '/administration\/templates\/base\/images\/admin_login_admin_logo\.png" alt="Dolphin ([\d]+) Admin" \/>/ }
	]
