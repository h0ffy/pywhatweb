import sys
import os
			
class Pluginibm_web_traffic_express_caching_proxy_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^IBM-PROXY-WTE\/([^\s]+)/" },
			{ "url" : "/admin-bin/webexec/wte.html", "string" : /<a href="https?:\/\/([^\/^"]+)(:\d+)?\/"><img src="https?:\/\/([^\/^"]+)(:\d+)?\/Docs\/docmast\.gif" alt="Caching Proxy Version ([^"]+)"><\/a>/" },
			{ "url" : "/admin-bin/webexec/wte.html", "version" : "/<a href="https?:\/\/([^\/^"]+)(:\d+)?\/"><img src="https?:\/\/([^\/^"]+)(:\d+)?\/Docs\/docmast\.gif" alt="Caching Proxy Version ([^"]+)"><\/a>/", "offset" : "4 },
		]
		return(self.rules)

