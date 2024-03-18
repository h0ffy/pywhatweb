import sys
import os
			
class olat_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<div id="b_footer_version">[\s]+<a href="http:\/\/www\.olat\.org"  title="Homepage of Open Source LMS OLAT" target="_blank">OLAT ([^<]+)<\/a>/ }
			{ "version" : '/<div id="o_footer_version">[\s]+<a href="http:\/\/www\.olat\.org"  title="Homepage of Open Source LMS OLAT" target="_blank">[\s]+OLAT ([^<^\n]+)[\s]+<\/a>/ }
			{ "certainty" : '25", "text" : '<meta name="DC.creator" content="University of Zurich - http://www.uzh.ch" />' }
			{ "certainty" : '75", "text" : '<meta name="DC.subject" content="OLAT - Online Learning And Training - Your Open Source Learning Management System" />' }
			{ "text" : '<meta name="DC.contributor" content="see http://www.olat.org/website/en/html/download_license.html" />' }
			{ "text" : '<title>OLAT - Online Learning And Training</title></head>' }
			{ "text" : '<title>OLAT - Online Learning And Training </title>' }
			{ "certainty" : '75", "text" : '<body onload="b_start();" id="b_body" class="b_lang_en">' }
			{ "certainty" : '75", "text" : '<body onload="b_start();" id="b_body">' }
			{ "certainty" : '75", "text" : '<body onload="o2start();" class="o_body">' }
			{ "text" : '<!-- START olatContentPanel -->' }
			{ "text" : '<a accesskey="2" href="#content" title="Go to "Content"></a>' }
		]

