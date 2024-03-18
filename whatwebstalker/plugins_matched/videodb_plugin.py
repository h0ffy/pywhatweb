import sys
import os
			
class Pluginvideodb_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<a href="index.php?export=pdf&amp;ext=.pdf"><img src="images/pdfexport.png" /></a>" },
			{ "text" : "<!-- /content --><!-- footer.tpl -->" },
			{ "text" : "<link rel="alternate" type="application/rss+xml" title="VideoDB RSS" href="index.php?export=rss" />" },
			{ "text" : "<meta name='description' content='VideoDB' />" },
			{ "text" : "<meta name="description" content="VideoDB" />" },
			{ "version" : "/<a href="http:\/\/www\.splitbrain\.org\/go\/videodb" class="splitbrain">v\.([^<]+)<\/a>/" },
			{ "version" : "/<div id="footerversion">[\s]*<a href="http:\/\/www\.videodb\.net">v([^<]+)<\/a>[\s]*<\/div>/" },
		]

