import plugins
			
class Pluginezcms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "        <td align="right"><a href="http://www.ezwebsites.com.au" class="credits">Site Powered by EZCMS</a></td>" },
			{ "text" : "      <td width="100%" align="left" valign="bottom" background="images/headerbg.png"><div align="right"><img src="images/headerright.png" border="0"></div></td>" },
			{ "md5" : "3f9861ab3124420694f663c82bf770ab", "url" : "admin/images/headerright.png" },
			{ "text" : "<title>EZCMS Content Management System</title>" },
			{ "version" : "/<center><strong>EZCMS ([\d\.]+) /" },
			{ "version" : "/Powered by <a href="http:\/\/ezcms.eztechhelp.com\/">EZCMS ([\d\.]+)<\/a>/" },
		]
	return(self.rules)

