import plugins
			
class Pluginsquarespace_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "text" : "This site is completely powered by the Squarespace platform." },
			{ "text" : "new Squarespace.FixedPositionTip("Logout Successful", "You have been successfully logged out.", "{ xMargin: 15", "yMargin: 15", "icon: "/universal/images/helptip-info.png", "orientation: "upper-right", "viewportFixed: true", "autoHide: 1800 }).show();" },
			{ "url" : "favicon.ico", "md5" : "89cc5689b952ee12d13a68e98119183f" },
			{ "search" : "headers[set-cookie]", "regexp" : "/^WebPersCookie/", "name" : "WebPersCookie cookie" },
			{ "search" : "headers[set-cookie]", "regexp" : "/^SS_MID/", "name" : "SS_MID cookie" },
			{ "search" : "headers[set-cookie]", "regexp" : "/^ss_sd/", "name" : "ss_sd cookie" },
		]
		return(self.rules)
