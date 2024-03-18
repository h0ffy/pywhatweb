import sys
import os
			
class Pluginmambo_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<meta name="Generator" content="Mambo - Copyright 2000 - [0-9]+ Miro International Pty Ltd.  All rights reserved." \/>},
			{ "regexp" : "/<meta name="description" content="Mambo - the dynamic portal engine and content management system" \/>},
			{ "url" : "README.php", "text" : "Mambo is OSI Certified Open Source Software", "released under the GNU General Public License" },
			{ "url" : "administrator/templates/mambo_admin/templateDetails.xml", "regexp" : " /(<name>Mambo Admin<\/name>|<authorUrl>http:\/\/www\.mambo\-foundation\.org<\/authorUrl>)/" },
		]
		return(self.rules)

