import sys
import os
			
class tangocms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/Powered by <a href="http:\/\/(www\.)?tangocms\.org" title="(Open Source CMS|TangoCMS)">TangoCMS<\/a>\./ },
			{ "text" : '<input type="checkbox" id="sessionRemember" name="session[remember]" value="1" checked="checked"> <label class="horizontal" for="sessionRemember">Remember me?</label>' },
		]

