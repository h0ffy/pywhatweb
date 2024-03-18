import plugins
			
class Pluginkayako_supportsuite_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[set-cookie]", "text" : "SWIFT_client" },
			{ "text" : " - Powered By Kayako eSupport</title>" },
			{ "regexp" : "/<span class="smalltext"><font color="#333333">Powered by e(Support|SupportSuite)<br\/>Copyright &copy; 2001-[0-9]{4} Kayako Infotech Ltd.<\/font><\/span><br \/>/" },
			{ "version" : "/<a href="http:\/\/www.kayako.com" target="_blank">Help Desk Software By Kayako eSupport v([\d\.]+)<\/a>/" },
			{ "version" : "/<a href="http:\/\/www.kayako.com" target="_blank" title="Help Desk Software">Help Desk Software<\/a>&nbsp;by Kayako SupportSuite v([\d\.]+)/" },
			{ "version" : "/<td width="144" align="left" valign="top"><span class="smalltext"><font color="#333333">([\d\.]+)<\/font><\/span><\/td>/" },
			{ "version" : "/SWIFT\.Setup[^}]*"version":"([0-9\.]+)"/" },
			{ "text" : "<div id="bottomfooter" class="bottomfooterpadding"><a href="http://www.kayako.com" target="_blank" class="bottomfooterlink">Help Desk Software"'},
		]
	return(self.rules)
