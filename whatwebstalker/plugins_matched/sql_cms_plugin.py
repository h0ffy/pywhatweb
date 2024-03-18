import sys
import os
			
class sql_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<script type="text/javascript">var LoginAttempts=0;</script><link href="CSS/styles/default.css" type="text/css" rel="stylesheet" /></head>' },
			{ "text" : '<tr><td>Language</td><td><select id="ddlLanguage" onchange="location.href=\'admin.aspx?lang=\'+SelectedValue(\'ddlLanguage\')"><option value="English" selected="selected">English</option>' },
			{ "version" : '/<a href="http:\/\/www.developerinabox.com" target="_blank"><img src="Img\/poweredby.png" style="position:absolute;right:0px;bottom:-30px;margin-top:2px;border:0px" title="SQLCMS v([\d\.]+)"\/><\/a>/ },
		]

