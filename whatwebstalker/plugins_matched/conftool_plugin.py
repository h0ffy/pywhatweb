import sys
import os
			
class Pluginconftool_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<h2 align=center>ConfTool Conference Administration</h2>" },
			{ "string" : "Standard", "text" : "<td class="td_dlg_input" width=67% align=left><input type=text name=\'ctusername\' tabindex=2 size=35></td></tr>" },
			{ "string" : "Pro", "version" : "/<td align="right" nowrap><a href="http:\/\/www\.conftool\.net\/"><span class="[^"]+">Conference Software - <\/span><span class="[^"]+">[\s]+(VSIS )?ConfTool( Pro)? ([^<^\s]+)<\/span><\/a><BR>/", "offset" : "2 },
			{ "string" : "Standard", "version" : "/<td align="right" nowrap><span class="normal8"><a href='http:\/\/www\.conftool\.net'>(Conference |Web-based |Event |Abstract )?(Management|Conference) (Software|System) - VSIS <b>ConfTool<\/b><\/a> Standard ([^<^\s]+)<\/span><BR>/", "offset" : "3 },
		]

