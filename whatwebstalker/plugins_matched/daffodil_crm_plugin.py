import plugins
			
class Plugindaffodil_crm_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div id="right_footer">Powered by Daffodil Software Ltd</div>" },
			{ "text" : "<div id="right_footer">Design & Development by Daffodil Software Ltd</div>" },
			{ "regexp" : "/ href="\?app=forgot_passwd&amp;cmd=passwd_send">[^>]*Forgot Password\?<\/a><\/td>/" },
		]
	return(self.rules)

