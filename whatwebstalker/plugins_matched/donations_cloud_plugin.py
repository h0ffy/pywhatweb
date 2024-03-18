import plugins
			
class Plugindonations_cloud_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "wp-content/plugins/donationscloud//donationscloud.css' type='text/css' media='screen' />" },
			{ "text" : "if (dc_get('pp_amount').value == '') { alert(\"Please enter a donation amount.\"); return false; }" },
			{ "regexp" : "/<p id='dc_credits'>powered by <a href=[\'|\"]+http:\/\/www.zirona.com\/software\/[^>]+>Donations Cloud<\/a><\/p>/i },
			{ "text" : "<form action='https://www.paypal.com/cgi-bin/webscr' method='post' id='dc_paypal_form' onsubmit='if (!dc_checkform()) return false;'>" },
		]
			return(self.rules)
