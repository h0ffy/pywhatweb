import plugins
			
class Pluginektron_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[set-cookie]", "regexp" : "/EktGUID=[a-f\d]{8}-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}; expires=/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/EkAnalytics/", "name" : "EkAnalytics cookie" },
			{ "search" : "headers[set-cookie]", "regexp" : "/ecm=user_id=[\d]+&isMembershipUser=[\d]+&site_id=&username=&new_site=[^&]+&unique_id=[\d]+&site_preview=[\d]+&langvalue=[\d]+&DefaultLanguage=[\d]+/" },
			{ "text" : "<script id="EktronJS" type="text/javascript" src="/WorkArea/java/ektron.js">" },
			{ "text" : "<script id="EktronRegisteredJs" type="text/javascript" src="/workarea/java/ektronJs.ashx?id=" },
			{ "text" : "<script id="EktronModalJS" type="text/javascript" src="/WorkArea/java/plugins/modal/ektron.modal.js">" },
		]
	return(self.rules)
