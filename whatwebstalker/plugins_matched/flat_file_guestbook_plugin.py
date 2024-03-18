import sys
import os
			
class Pluginflat_file_guestbook_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<link rel="stylesheet" type="text/css" href="ffgb_styles.css">" },
			{ "text" : "<a href="guestbook.php">Return to the Guestbook</a><br>&nbsp;<br>" },
			{ "text" : "<td align="right"><input type="password" value=" name="ffgb_pass"></td></tr>" },
			{ "text" : "<a href="ffgb_admin.php"><i>Manage this Guestbook</i></a>" },
		]
		return(self.rules)

