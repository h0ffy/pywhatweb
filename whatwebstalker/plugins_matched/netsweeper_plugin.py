import sys
import os
			
class Pluginnetsweeper_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<DIV id="overDiv" style="position:absolute; visibility:hidden; z-index:104;"></DIV>" },
			{ "text" : "<div id="overDiv" style="position:absolute; visibility:hidden; z-index:104;"></div>" },
			{ "text" : "<!-- Body of content starts here -->" },
			{ "text" : "<BR><SPAN class='netsweepersmbtextatbottomofloginscreen'>" },
			{ "text" : "<br><span class='netsweepersmbtextatbottomofloginscreen'>" },
			{ "text" : "<!-- full_page_header.html START -->" },
			{ "text" : "<!-- full_page_footer.html START-->" },
			{ "text" : "<a target=_parent href="../" >Please click <u>here</u> to continue.</a>" },
			{ "text" : "<a href="http://www.poweredbynetsweeper.com"><img src="http://www.poweredbynetsweeper.com/images/deny/global/poweredbynetsweeper.gif" border="0" alt=" align="top" /></a></td>" },
			{ "text" : "<a href="http://www.poweredbynetsweeper.com"><img align=top border=0 src="http://www.poweredbynetsweeper.com/images/deny/global/poweredbynetsweeper.gif"></a>" },
		]

