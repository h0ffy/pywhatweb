import sys
import os
			
class Pluginsitefinity_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "href="http://www.sitefinity.com" class="poweredBySitefinity" title="Sitefinity ASP.NET CMS">Powered by Sitefinity ASP.NET CMS</a></p>" },
			{ "text" : "title="Sitefinity ASP.NET CMS" class="poweredBySitefinity" href="http://www.sitefinity.com">Powered by Sitefinity ASP.NET CMS</a></p>" },
			{ "version" : "/<meta name="Generator" content="Sitefinity ([\d\.:]{1,20}( [A-Z]+)?)" \/>/" },
			{ "certainty" : "75", "regexp" : "/<link href="\/[Ss]ite[Ff]inity\/WebsiteTemplates\//" },
		]

