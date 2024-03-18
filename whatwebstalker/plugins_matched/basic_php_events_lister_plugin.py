import sys
import os
			
class basic_php_events_lister_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "Powered by: <a href="http://www.mevin.com/">mevin productions</a>" },
			{ "text" : "<br /><center><input class="text" type="submit" name="submitBtn" value="Login" /></center>" },
			{ "text" : "<center><br> <a href=recover.php>Lost your password?</a></center>" },
		]

