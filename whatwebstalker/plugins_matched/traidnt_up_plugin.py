import sys
import os
			
class traidnt_up_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<!-- # START HEDARE -->' },
			{ "text" : '<font color='#000080'><a href='http://traidnt.net' target='_blank'>" },
			{ "text" : '			<span style='text-decoration: none'><font color='#000000'>Traidnt&nbsp;UP</font></span></a></font></span></b>" },
			{ "version" : '/<p align='center' dir='ltr'>Powered by Traidnt UP Version ([\d\.]+)<\/p>/ },
			{ "version" : '/<div class="footer">Powered by <a href="http:\/\/traidnt.net" target="_blank">TRAIDNT UP<\/a> Version ([\d\.]+)[\s]*<\/div>/ },
			{ "version" : '/			<span style='text-decoration: none'><font color='#000000'>Traidnt&nbsp;UP<\/font><\/span><\/a><\/font><\/span><\/b>[\r\n]{2}			Version ([\d\.]+)<\/p>/ },
		]

