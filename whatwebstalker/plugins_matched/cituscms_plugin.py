import sys
import os
			
class cituscms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<title>Administration &#149; Webseitenname</title>' }
			{ "text" : '<!-- Powered by CitusCMS - http://www.citus-cms.org -->' }
			{ "text" : 'Powered by <a href="http://www.citus-cms.org" target="_blank" title="Powered by CitusCMS"><strong>CitusCMS</strong></a>' }
			{ "text" : '<meta name="generator" content="CitusCMS - http://www.citus-cms.org" />' }
			{ "text" : '<meta name="generator" content="CitusCMS [http://www.citus-cms.org]" />' }
			{ "version" : '/<!-- CitusCMS Core Version: ([^\s]+) -->/ }
	]

