import plugins
			
class Pluginshoretel_converged_conferencing_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "url" : "/ics?action=display&display=opener", "text" : "<script src="/ics?action=get_branding_js" charset="UTF-8"></script>" },
			{ "certainty" : "75", "url" : "/ics?action=display&display=opener", "text" : "<DIV style="visibility:hidden;display:none" id="TEXT_OPENING_PRODUCT">Opening *brand_product_name*</DIV>" },
			{ "url" : "/branding/default/ENG-US.js", "text" : "this.product_name_long = "ShoreTel Converged Conferencing";" },
			{ "url" : "/branding/default/ENG-US.js", "md5" : "560374321ea7b2a57e5cac1df6611e36" },
		]
		return(self.rules)

