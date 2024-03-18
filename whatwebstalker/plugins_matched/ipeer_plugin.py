import sys
import os
			
class ipeer_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<title>iPeer V(\d) with TeamMaker<\/title>/ },
			{ "text" : '<h1 align="center"><span class="footer">Powered by iPeer and TeamMaker - Created by UBC and Rose-Hulman</span></h1>' },
			{ "version" : '/<span class="bannerText"><span style='font-size: 120%;'>([^<]+)<\/span>&nbsp;&nbsp;with TeamMaker<\/span><\/td>/ },
			{ "search" : 'headers[set-cookie]", "regexp" : '/IPEER=[^;]+;/ },
		]

