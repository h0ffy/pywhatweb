import plugins
			
class Pluginplone_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "name" : "URL Pattern", "certainty" : "75", "ghdb" : "inurl:"acl_users/credentials_cookie_auth/require_login?came_from"" },
			{ "text" : "<div class="visualIcon contenttype-plone-site">'},
			{ "name" : "X-Caching-Rule-Id: plone-content-types", "search" : "headers[x-caching-rule-id]", "regexp" : "/plone-content-types/i },
			{ "name" : "X-Cache-Rule: plone-content-types", "search" : "headers[x-cache-rule]", "regexp" : "/plone-content-types/i },
		]
		return(self.rules)
