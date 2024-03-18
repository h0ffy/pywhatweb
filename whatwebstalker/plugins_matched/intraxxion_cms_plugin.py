import sys
import os
			
class intraxxion_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<meta name="generator" content="Intraxxion CMS ([\d\.]{1,5})" \/>/ },
			{ "text" : '<!-- site built by Intraxxion", "www.intraxxion.com", "info@intraxxion.com", "tel: +31 45 5650207", "fax: +31 45 5650123' },
			{ "text" : '<!-- site built by Intraxxion", "www.intraxxion.com", "more_info@intraxxion.com", "tel: +31 45 5650207", "fax: +31 45 5650123' },
		]

