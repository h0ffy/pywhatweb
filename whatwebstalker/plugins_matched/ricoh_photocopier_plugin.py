import sys
import os
			
class ricoh_photocopier_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<table width="100%" border="0" cellspacing="0" cellpadding="0" style="background:url(/images/settingDivision.gif) repeat-x bottom;">' }
			{ "text" : '<meta http-equiv="refresh" content="1; URL=/web/guest/en/websys/webArch/message.cgi?messageID=MSG_JAVASCRIPTOFF&buttonURL=/../../../">' }
			{ "url" : '/web/guest/en/websys/webArch/header.cgi", "model" : '/<span class="modelName">([^<]+)<\/span>/ }
			{ "url" : '/web/guest/en/websys/webArch/topPage.cgi", "model" : '/<td nowrap align=">Device Name<\/td>[\s]+<td nowrap>:<\/td>[\s]+<td nowrap>([^<]+)<\/td>/ }
			{ "url" : '/web/guest/en/websys/webArch/topPage.cgi", "string" : /<td nowrap align=">Host Name<\/td>[\s]+<td nowrap>:<\/td>[\s]+<td nowrap>([^\s^<]+)<\/td>/ }
			{ "url" : '/web/guest/en/websys/netw/getInterface.cgi", "string" : /<td (xmlns:axsl="[^"]+" )?nowrap align="left" width="150">MAC Address<\/td>[\s]+<td xmlns:axsl="http:\/\/localhost" nowrap>:<\/td>[\s]+<td nowrap>([^\s^<]+)<\/td>/", "offset" : '1 }
			{ "url" : '/web/guest/en/websys/status/configuration.cgi", "model" : '/<td nowrap align=">Model Name<\/td>[\s]+<td nowrap>:<\/td>[\s]+<td nowrap>([^<]+)<\/td>/ }
			{ "url" : '/web/guest/en/websys/status/configuration.cgi", "string" : /<td nowrap align="left">Total Memory<\/td>[\s]+<td nowrap>:<\/td>[\s]+<td nowrap>([^\s^<]+)<\/td>/ }
	]
