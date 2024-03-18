import sys
import os
			
class Plugingallery_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<a href="#" id="g-password-reset" class="g-right g-text-small">Forgot your password?</a>" },
			{ "version" : "/<li class="(g-)?first">Powered by <a href="http:\/\/gallery\.menalto\.com">(<bdo dir="ltr">)?Gallery ([^<]+)(<\/bdo>)?<\/a><\/li>/", "offset" : "2 },
			{ "filepath" : "/We've found a place to store your photos:\s+<code class="location">([^<]+)<\/code>/" },
			{ "certainty" : "75", "text" : "<title>Gallery 3 Installer</title>" },
		]

