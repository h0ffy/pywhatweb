import plugins
			
class Plugindv_cart_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div id="KT_tngdeverror"><label>Message:</label><div>You must have the proper credentials to access this page. Please login.</div></div>" },
			{ "text" : "<table cellpadding="2" cellspacing="0" class="KT_tngtable">" },
		]
	return(self.rules)

