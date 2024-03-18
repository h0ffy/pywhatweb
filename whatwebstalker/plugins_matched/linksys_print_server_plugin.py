import sys
import os
			
class linksys_print_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<td align="right" class="pname" height="25" colspan="5">Print Server for USB with 4-Port Switch &nbsp; &nbsp; </td>", "model" : 'PSUS4" }
			{ "firmware" : '/<td width="585" colspan="2" bgcolor="#6666CC" valign="bottom" align="right"><span class="fwversion">Firmware Version: &nbsp; ([^\s]{1,10}) <\/span> &nbsp;&nbsp;<\/td>/ }
			{ "certainty" : '25", "version" : '/^PRINT_SERVER WEB ([\d\.]+)$/", "search" : 'headers[server]" }
			{ "certainty" : '25", "regexp" : '/^PRINT_SERVER WEB/", "search" : 'headers[server]" }
		]

