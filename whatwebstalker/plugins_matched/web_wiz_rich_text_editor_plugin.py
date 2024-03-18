import sys
import os
			
class web_wiz_rich_text_editor_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<a href="http:\/\/www\.richtexteditor\.org" target="_blank" style="font-size:10px">Web Wiz Rich Text Editor<\/a> version ([^<]+)<\/span><\/td>/" },
			{ "version" : "/<\!\-\-\/\/\s+\/\* [^\s]+\s+Software: Web Wiz Rich Text Editor\(TM\) ver\. ([^\s]+)/" },
			{ "text" : "<form method="post" action="RTE_popup_file_atch.asp" name="frmImageInsrt">" },
		]

