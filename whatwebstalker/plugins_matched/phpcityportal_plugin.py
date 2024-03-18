import sys
import os
			
class phpcityportal_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : "75", "text" : "<meta name="author" content="Cr8Soft" />" },
			{ "text" : "<center><a href="http://phpcityportal.com">Powered by PHPCityPortal.com</a></center><p>" },
			{ "text" : "<center><a href="http://www.phpcityportal.com/index.php">Powered by PHPCityPortal.com</a></center>" },
			{ "text" : "<form id="frm_login_left" name="frm_login_left" action="includes/check_user.php" method="post">" },
			{ "text" : "<form id="frm_login_left" name="frm_login_left" action="includes/check_user.php.inc" method="post">" },
		]

