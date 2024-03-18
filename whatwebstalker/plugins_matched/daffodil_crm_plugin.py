import sys
import os
			
class daffodil_crm_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<div id="right_footer">Powered by Daffodil Software Ltd</div>' }
			{ "text" : '<div id="right_footer">Design & Development by Daffodil Software Ltd</div>' }
			{ "regexp" : '/ href="\?app=forgot_passwd&amp;cmd=passwd_send">[^>]*Forgot Password\?<\/a><\/td>/ }
	]

