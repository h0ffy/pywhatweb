import sys
import os
			
class micro_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : "/<div class="footer"><div style="float: left;">Powered by <a href="http:\/\/(tpiha.kset.org|www.micro-cms.com)\/">Micro CMS<\/a> \| <a href="/" },
			{ "text" : "Powered by <strong><a href="http://microcms.kset.org/">Micro CMS</a></strong><br />" },
			{ "certainty" : "25", "text" : " method="post"onsubmit="" },
		]

