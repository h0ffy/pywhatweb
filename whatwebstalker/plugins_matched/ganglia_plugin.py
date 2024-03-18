import sys
import os
			
class Pluginganglia_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<TITLE>Ganglia:: Cluster Report</TITLE>" },
			{ "text" : "(Nodes colored by 1-minute load) | <A HREF="./node_legend.html">Legend</A>" },
			{ "text" : "<B>Metric</B>&nbsp;&nbsp;<SELECT NAME="m" OnChange="ganglia_form.submit();">" },
			{ "version" : "/<CENTER>\n<FONT SIZE="-1" class=footer>\n(Gmetad|Ganglia) Web Frontend version ([\d\.]+)\n<A HREF="http:\/\/ganglia\.sourceforge\.net\/downloads\.php\?component=ganglia-webfrontend&amp;\nversion=[\d\.]+">Check for Updates\.<\/A><BR>\n/", "offset" : "1 },
			{ "version" : "/Web Backend <i>\(gmetad\)<\/i> version ([\d\.]+)\n<A HREF="http:\/\/ganglia\.sourceforge\.net\/downloads\.php\?component=gmetad&amp;\nversion=[\d\.]+">Check for Updates\.<\/A><BR>/", "offset" : "1 },
		]
		return(self.rules)

