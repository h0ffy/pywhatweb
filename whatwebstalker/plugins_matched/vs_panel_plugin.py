import sys
import os
			
class vs_panel_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '    <td width="10%"><div align="right"><a href="http://www.vertigostudios.com" target="_blank"><img src="images/vs_white.gif" alt="Made in Vertigo Studios" width="48" height="21" hspace="3" vspace="3" border="0" /></a></div></td>' },
			{ "md5" : '54ab59aeb78202bc2ec96abb0c6cff7c", "url" : 'images/vs_white.gif' },
			{ "version" : '/&copy; [0-9]{4} \| Powered by VS PANEL v.([\d\.]+)<\/div><\/td>/ },
			{ "version" : '/&copy; [0-9]{4} \| Powered by VS PANEL v.([\d\.]+)(<\/span>)<\/div><\/td>/ },
		]

