import sys
import os
			
class atvise_webmi_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^atvise$/ },
			{ "text" : '<td><noscript>N/A</noscript><script type="text/javascript"><!--' },
			{ "url" : '/visu.htm", "text" : '<li class="btn"><a class="button" style="left:93%;" href="javascript:void(0)" target="mainframe" id="alarmlistbutton"><img height="30" width="47" src="buttonc.gif" alt=" /></a></li>' },
		]

