import sys
import os
			
class jcow_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<meta name="Generator" content="Jcow Social Networking Software\. ([\d\.]+)" \/>/ }
			{ "version" : '/Powered by <a href="http:\/\/www\.jcow\.net" title="Social Networking Software", "Community Software" target="_blank"><strong>Jcow<\/strong> ([\d\.]+)<\/a>/ }
			{ "text" : '<meta name="Generator" content="Powered by Jcow" />' }
			{ "text" : '<!-- do NOT remove the Jcow Attribution Information -->' }
			{ "text" : '<!-- jcow branding -->' }
			{ "text" : '<!-- end jcow_application_box -->' }
		]

