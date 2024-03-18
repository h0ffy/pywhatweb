import sys
import os
			
class ezboo_webstats_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '75", "ghdb" : '+"Administrator Panel" +intitle:"ezBOO WebStats"' }
			{ "text" : '<title>ezBOO WebStats</title>' }
			{ "text" : '<div align="center" class="titre"><font color="#FFFFFF">&gt;&gt; Administrator Panel        &lt;&lt; </font></div>' }
			{ "text" : '<td height="60" valign="top" align="center"><img src="image/logo_ez1.gif" border="0"></td>' }
		]

