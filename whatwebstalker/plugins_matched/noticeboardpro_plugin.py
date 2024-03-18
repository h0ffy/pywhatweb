import sys
import os
			
class noticeboardpro_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<td align="center" colspan="4" height="38" width="572" bgcolor="#f5f5dc"><p class="copy">Version ([\d\.]+) -/ },
			{ "text" : '<A HREF="registerOutline.php" CLASS="Xref" style="margin-right:10">[Register]</A>' },
			{ "text" : '<A HREF="loginOutline.php" CLASS="Xref" style="margin-left:165; margin-right:10">[Sign In]</A>' },
		]

