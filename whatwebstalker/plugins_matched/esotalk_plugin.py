import sys
import os
			
class Pluginesotalk_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<!-- This page was generated by esoTalk (http://esotalk.com) -->" },
			{ "text" : "<!-- The following text constitutes a copyright notification and", "under the terms of the GNU GPL (see LICENSE)", "may neither be removed nor altered in any way which makes it invisible", "affects the hyperlink", "or changes the text "Powered by esoTalk". -->" },
			{ "text" : "Powered by <a href='http://esotalk.com/'>esoTalk</a>&trade;" },
			{ "text" : "<ul><li><a href='http://esotalk.com'>Donate to esoTalk</a></li></ul><p id='copyright'>" },
			{ "text" : "<title>esoTalk Installer</title>", "module" : "Install Page" },
			{ "text" : "<p>If you run into any other problems or just want some help with the installation", "feel free to ask for assistance at the <a href='http://forum.esotalk.com/'>esoTalk support forum</a> where a bunch of friendly people will be happy to help you out.</p>", "module" : "Install Page" },
			{ "text" : "<script type='text/javascript' src='../js/esotalk.js'></script>", "module" : "Install Page" },
		]

