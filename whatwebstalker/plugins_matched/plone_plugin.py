import sys
import os
			
class plone_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "name" : "URL Pattern", "certainty" : "75", "ghdb" : "inurl:"acl_users/credentials_cookie_auth/require_login?came_from"" },
			{ "text" : "<div class="visualIcon contenttype-plone-site">'},
			{ "name" : "X-Caching-Rule-Id: plone-content-types", "search" : "headers[x-caching-rule-id]", "regexp" : "/plone-content-types/i },
			{ "name" : "X-Cache-Rule: plone-content-types", "search" : "headers[x-cache-rule]", "regexp" : "/plone-content-types/i },
		]

