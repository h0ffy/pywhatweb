import sys
import os
			
class tickets_cad_system_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<HEAD><TITLE>Tickets - Top Frame</TITLE>' }
			{ "text" : '<HEAD><TITLE>Tickets - Login Module</TITLE>' }
			{ "regexp" : '/<NOFRAMES>\s+<BODY>\s+Tickets requires a frames-capable browser\.\s+<\/BODY>\s+<\/NOFRAMES>/ }
			{ "version" : '/<TITLE>Tickets ([^<]+)<\/TITLE>\s+<LINK REL=StyleSheet HREF="/ }
			{ "text" : '<TR CLASS='even'><TD ROWSPAN=6 VALIGN='middle' ALIGN='left' bgcolor=#EFEFEF><BR /><BR />&nbsp;&nbsp;<IMG BORDER=0 SRC='open_source_button.png'>" }
	]

