import sys
import os
			
class serendipity_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<meta name="Powered-By" content="Serendipity v.([^"]+)" \/>/i },
			{ "version" : "/My weblog is proudly powered by <a href="http:\/\/www.s9y.org">Serendipity ([^<]+)<\/a>.<br \/>/" },
			{ "text" : "<p>Powered by <a href="http://www.s9y.org" target="_blank">Serendipity</a>" },
			{ "text" : "<div class="copyright">Powered by <a href="http://www.s9y.org" title="a PHP Weblog/Blog software">Serendipity</a>" },
			{ "text" : "serendipity_entry_body" },
			{ "text" : "serendipity_entry_author_Admin" },
			{ "text" : "serendipity_entryFooter" },
			{ "text" : "<div id="serendipityLeftSideBar">" },
		]

