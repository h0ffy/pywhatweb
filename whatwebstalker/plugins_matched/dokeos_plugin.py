import sys
import os
			
class dokeos_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '25", "text" : '<ul id="dokeostabs">' },
			{ "text" : '<!-- start of #main wrapper for #content and #menu divs -->' },
			{ "certainty" : '75", "text" : '<link href="http://www.dokeos.com/documentation.php" rel="Help" />' },
			{ "certainty" : '75", "text" : '<link href="http://www.dokeos.com/team.php" rel="Author" />' },
			{ "certainty" : '75", "text" : '<link href="http://www.dokeos.com" rel="Copyright" />' },
			{ "text" : '<meta name="Generator" content="Dokeos">' },
			{ "certainty" : '75", "text" : '<title>Dokeos has not been installed</title>' },
			{ "regexp" : '/<form action="main\/install\/index\.php" method="get"><button class="save" type="submit"[^>]+value="&nbsp;&nbsp; Click to INSTALL (Dokeos|DOKEOS)[\s]+&nbsp;&nbsp;" >Click to INSTALL (Dokeos|DOKEOS)[\s]*<\/button><\/form><br \/>/", "string" : 'Install Page" },
			{ "string" : /<div class="copyright">[^<]+<a href="http:\/\/www\.dokeos\.com" target="_blank">[\s]*Dokeos [\d\.]*<\/a> &copy; (20[\d]{2})[\s]*<\/div>/ },
			{ "version" : '/<div class="copyright">[^<]+<a href="http:\/\/www\.dokeos\.com" target="_blank">[\s]*Dokeos ([\d\.]+)<\/a>/ },
			{ "version" : '/<title>&mdash; Dokeos Installation &mdash; Version ([\d\.]+)<\/title>/", "string" : 'Install Page" },
		]

