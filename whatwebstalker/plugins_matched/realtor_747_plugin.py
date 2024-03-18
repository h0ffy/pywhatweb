import sys
import os
			
class realtor_747_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<body onload="start_realtor747_admin();" onunload="stop_realtor747_admin();">' }
			{ "version" : '/    <a href="http:\/\/www.it747.com\/realtor747" target="_blank"><span style="color: green;">Powered by REALTOR 747 - The Property Listings Management System - Version ([\d\.]+)<\/span><\/a><br>/ }
			{ "version" : '/<title>REALTOR 747 - The Property Listings Management System - Administration  - Version ([\d\.]+)<\/title>/ }
	]
