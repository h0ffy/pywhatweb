import sys
import os
			
class real_estate_portal_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'Powered by <a href="http://www.netartmedia.net/realestate" target="_blank">Real Estate Portal</a>' }
			{ "text" : 'Powered by <a href="http://www.netartmedia.net/realestate">Real Estate Portal</a>' }
			{ "text" : '			document.form1.property_type.options[i] = new Option(CurrentModels[i]", "CurrentModels[i]", "0", "0);' }
		]

