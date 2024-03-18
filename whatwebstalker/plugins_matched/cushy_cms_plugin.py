import sys
import os
			
class cushy_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'Content Management Powered by <a href="http://www.cushycms.com">CushyCMS</a>'},
			{ "text" : '<li id="poweredBy"><img alt="Powered by CushyCMS" src="/images/cushy_badge.gif'},
			{ "text" : '<span id="cushycms-footer">Powered by CushyCMS</span>'},
			{ "regexp" : '/<[^>]+class="cushycms"},
		]

