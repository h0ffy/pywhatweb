import sys
import os
			
class bab.stats_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<meta NAME="Author" CONTENT="Bab.Stats Team">' },
			{ "certainty" : '25", "regexp" : '/<title>[^:]+ :: [^:]+ :: Powered by BAB.stats<\/title>/ },
			{ "version" : '/Powered by BAB.Stats :: <a href="index.php\?action=about&bms=" onmouseover="doTooltip\(event", "'About BaB.Stats'\)" onmouseout="hideTip\(\)">BabStats v([\d\.]+)<\/a>/ },
			{ "version" : '/Powered by <a href="index.php\?action=about&bms=">BAB.stats<\/a> version ([\d\.]+)/ },
			{ "text" : '<meta NAME="Author" CONTENT="Tomas Stucinskas a.k.a Baboon">", "string" : 'Chronos" },
			{ "text" : ' - Powered by BAB.stats Chronos</title>", "string" : 'Chronos" },
			{ "text" : '<!-- AUTHOR : Tomas Stucinskas a.k.a Baboon -->", "string" : 'Chronos" },
			{ "version" : '/Powered by Bab.stats ::[\r\n\s]*<a[^>]+href="(http:\/\/www.babstats.com\/|\/Neos_Chronos\/index.php\?action=about)">Neos.Chronos<\/a> ::[\s\r\n]*Version ([^\(]+) \(Standalone\)/", "offset" : '1", "string" : 'Chronos" },
		]

