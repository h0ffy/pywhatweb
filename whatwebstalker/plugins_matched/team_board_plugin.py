import plugins
			
class Pluginteam_board_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<meta name="copyright" content="Copyright [0-9]{4}-[0-9]{4} - TEAM5.cn By DayMoon" \/>/" },
			{ "version" : "/[\s]+Powered by <a target=_blank 	href=http:\/\/www.team5.cn><b>TEAM ([\d\.]+) Release<\/b><\/a> - <a href=Licence.asp><b style='color:#FF9900'>ACC<\/b><\/a> &copy; [0-9]{4} Team5 Studio All rights reserved/" },
			{ "version" : "/Powered by <a target=_blank[\s]+href=http:\/\/www.team5.cn><b>TEAM ([\d\.]+)<\/b><\/a>/" },
			{ "version" : "/[\s]+Powered by <a target="_blank" href="http:\/\/www.team5.cn"><b>TEAM ([\d\.]+) Release<\/b><\/a> - <a href="Licence.asp"><b style='color:#FF9900'>SQL<\/b><\/a> &copy; [0-9]{4} Team5 Studio All rights reserved/" },
		]
	return(self.rules)

