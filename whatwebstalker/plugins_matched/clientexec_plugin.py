import sys
import os
			
class Pluginclientexec_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<!-- These should not have debug at the end for production -->" },
			{ "text" : "<title>Support Center - Powered By ClientExec</title>" },
			{ "text" : "<form action="index.php?fuse=admin&amp;action=Login&amp;public=1" method="post"" },
			{ "module" : /<img class="logo" src="templates\/([^\/]+)\/images\/public\/caption_photo\.jpg" alt="clientexec" \/>/" },
		]

