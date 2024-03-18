import sys
import os
			
class infomaster_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<head><title>[\s]+MasterView ([\d\.]+) Property Master[\s]+<\/title>/", "string" : 'MasterView" }
			{ "regexp" : '/class="ackn">[\s]*Powered by InfoMaster/ }
			{ "text" : '<link href="../../MasterView.css" type="text/css" rel="stylesheet"", "string" : 'MasterView" }
			{ "text" : '<link href="../../App_Themes/MasterView/MPLeftNavStyle/PanelBar.MPIFMA.css" type="text/css" rel="stylesheet" />", "string" : 'MasterView" }
			{ "text" : '<script language="javascript" src="../../common/masterView.js"></script>", "string" : 'MasterView" }
			{ "string" : /<form name="frm(MasterView|MasterPlan)" method="post" action="default\.aspx/ }
		]

