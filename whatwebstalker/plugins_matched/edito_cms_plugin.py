import sys
import os
			
class edito_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : "/<meta name="(g|G)enerator" content="(E|e)dito( CMS)? - www\.edito\.pl"[\s]*\/?>/" },
			{ "regexp" : "/Powered by[\s]*:?[\s]+<a[^>]+href="http:\/\/www.edito.pl[\/]?"[^>]+title="Edito CMS"[^>]*>/i },
		]

