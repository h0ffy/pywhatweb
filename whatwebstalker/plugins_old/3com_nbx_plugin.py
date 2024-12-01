import plugins
			
class Plugin3com_nbx_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<head><title>NBX NetSet</title>" },
			{ "text" : "<HEAD><TITLE>NBX NetSet</TITLE>" },
			{ "text" : "3Com Corporation or its subsidiaries" },
			{ "text" : "<!-- Gregory Brucato  4/22/98  NBX Corporation -->" },
			{ "version" : "/<META HTTP-EQUIV=\"sysObjectID\" CONTENT=\"([\d\.]{20,30})\">/" },
			{ "text" : "<span class=\"splashTitleIPTelephony\">&nbsp;3Com<SUP><span class=\"splashTitleNBXReg\">&reg;</span></SUP> IP Telephony Solution</span>" },
			{ "firmware" : "/<td colspan=\"3\" class=\"splashVersionCol\" valign='bottom'>[\s]+Version:&nbsp;([^<]+)<br \/>[\s]+Created:&nbsp;/" },
			{ "firmware" : "/<TABLE BORDER=\"0\" CELLPADDING=\"0\" CELLSPACING=\"0\"><TR><TD ALIGN=\"right\" WIDTH=\"130\" HEIGHT=\"75\">[\s]+Version:(&nbsp;)?([^<]+)<BR>/", "offset" : "1" },
			{ "model" : "/<span class=\"splashTitleNBX\">NBX<SUP><span class=\"splashTitleNBXReg\">&reg;<\/span><\/SUP><\/span>[\s]+<span class=\"splashTitlePlatform\">(&nbsp;)?([^<]+)<\/span>/", "offset" : "1" },
        ]  
        return(self.rules)
