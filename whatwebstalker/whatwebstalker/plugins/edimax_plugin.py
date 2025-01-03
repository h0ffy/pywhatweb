import plugins


class Pluginedimax_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<title>EDIMAX Technology</title>", "certainty": "75 },
			{ "text" : "<title>Access Point Status</title>", "url" : "/stainfo.asp" },
			{ "md5" : "9691c1bcac34138f8245d95e2e003e55", "url" : "/images/banner_up_03.jpg" },
			{ "text" : "cdwindow=window.open('countdown.asp','CountDown','channelmode=0", "directories=0,fullscreen=0,height=100,location=0,menubar=0,resizable=1,scrollbars=0,status=0,titlebar=0,toolbar=0,width=450','false');" },
			{ "text" : "<link rel="stylesheet" href="edimax.css">", "certainty" : "75 },
		]
	return(self.rules)
