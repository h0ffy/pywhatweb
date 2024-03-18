import sys
import os
			
class Pluginibm_web_traffic_express_caching_proxy_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^IBM-PROXY-WTE\/([^\s]+)/" },
			{ "url" : "/admin-bin/webexec/wte.html", "string" : /<a href="https?:\/\/([^\/^"]+)(:\d+)?\/"><img src="https?:\/\/([^\/^"]+)(:\d+)?\/Docs\/docmast\.gif" alt="Caching Proxy Version ([^"]+)"><\/a>/" },
			{ "url" : "/admin-bin/webexec/wte.html", "version" : "/<a href="https?:\/\/([^\/^"]+)(:\d+)?\/"><img src="https?:\/\/([^\/^"]+)(:\d+)?\/Docs\/docmast\.gif" alt="Caching Proxy Version ([^"]+)"><\/a>/", "offset" : "4 },
		]

