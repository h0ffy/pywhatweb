import sys
import os
			
class collegiatelink_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/Powered by <a href="http:\/\/www\.collegiatelink\.net">CollegiateLink<\/a> Version ([\d\.]+)<\/p><div id="links">CollegiateLink uses /" },
			{ "text" : "</div></div></div><div class="salink"><span class="shadow"><!----></span></div></div><span class="clearDiv"><!----></span></div></div><span class="clearDiv"><!----></span><script type="text/javascript">" },
		]

