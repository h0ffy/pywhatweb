import sys
import os
			
class spirepro_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<script xmlns:a="http://www.1stomni.com/spire/aml" type="text/javascript"" },
			{ "text" : "<meta name="Spire-Last-Modified" content="" },
			{ "regexp" : "/<meta name="Spire-Editor" content="([^"]+)">/" },
			{ "string" : /^SpirePRO CMS v([\d\.]+ \(Microkernel v[\d]+; CMS Server v[\d]+\)) /", "search" : "headers[x-generator]" },
			{ "string" : /^SpirePRO CMS v([\d\.]+ \(Microkernel v[\d]+; CMS Server v[\d]+\)) /", "search" : "headers[generator]" },
			{ "regexp" : "/^SpirePRO CMS/", "search" : "headers" },
		]

