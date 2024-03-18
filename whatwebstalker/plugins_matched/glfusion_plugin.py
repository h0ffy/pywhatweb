import sys
import os
			
class Pluginglfusion_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "certainty" : "75", "regexp" : "/<div (class|id)="gl_moomenu1">/" },
			{ "certainty" : "75", "text" : "<ul class="gl_moomenu1">" },
			{ "regexp" : "/Page created in [\d\.]+ seconds( |&nbsp;)by <a href="http:\/\/www.glfusion.org\/"[^>]*>glFusion<\/a>/" },
		]

