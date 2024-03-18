import sys
import os
			
class timelive_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<img id="CtlLogin1_Login1_imgCompanyOwnLogo" src="Images/TopHeader.jpg" alt="CompanyLogo" style="height:50px;border-width:0px;" /></td>" },
			{ "string" : /<span id="CtlLogin1_Login1_Label1">Copyright .{1,2} 2007 - (20[\d]{2}) Livetecs LLC\. All rights reserved\.<\/span>/" },
			{ "version" : "/<td style="width: 15%" align=right>[\s]+<span id="CtlLogin1_Login1_VersionLabel">v ([^<^\s]+)<\/span><\/td>/" },
		]

