import plugins
			
class Pluginlanrtc_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/Logo.gif", "md5" : "2fe5a40924a7b13c61fcc66a7dacec94" },
			{ "model" : "/<tr><td><h2>LanRTC([\d]{4})<br>System information<\/h2><\/td>/" },
			{ "model" : "/<title>LanRTC([\d]{4})-System information<\/title>/" },
			{ "text" : "<td align=right><h2><img src="Logo.gif" width="120" height="59" alt="MBB Gelma"></h2>" },
			{ "text" : "<p><font size=-1><strong><a href="javascript:window.history.back()">Back</a> | <a href="Index.htm">System Info</a> | <a href="TmStatus.htm?TM=1">TM Status</a> | <a href="LanStat.htm">LAN Akt.</a> | <a href="de/Buchen.htm">Booking</a></strong></font></p></body></html>" },
			{ "version" : "/^LanRTC\/([\d\.]{1,5})$/", "search" : "headers[server]" },
			{ "regexp" : "/^LanRTC/", "search" : "headers[server]" },
		]
		return(self.rules)

