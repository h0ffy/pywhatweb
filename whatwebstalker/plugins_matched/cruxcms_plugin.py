import sys
import os
			
class cruxcms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<font color="#666666"><center>Powered by <a href="http://www.cruxcms.co.uk">Crux CMS</a></center> </font>' }
			{ "text" : '<font color="#666666"><center>Powered by <a href="http://www.cruxsoftware.co.uk">Crux CMS</a></center> </font>' }
			{ "text" : '<meta name="Generator" content="Created by CruxCMS http://www.cruxsoftware.co.uk">' }
			{ "text" : '<meta name="Generator" content="Created by Crux CMS http://www.cruxcms.co.uk">' }
		]

