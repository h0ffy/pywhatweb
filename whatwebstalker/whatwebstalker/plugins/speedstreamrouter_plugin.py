import plugins


class Pluginspeedstreamrouter_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<TITLE>SpeedStream Router Management Interface</TITLE>'},
			{ "certainty" : "50", "regexp" : "/<!-- Copyright(C) [0-9]+ Siemens Subscriber Networks -->},
			{ "certainty" : "75", "text" : "<FRAME SRC="pflogin.htm" NAME="rightFrame"'},
			{ "url" : "/summary.htm", "model" : "/<B>System Type:<\/B><\/TD><TD>SpeedStream ([^\-]+-Series)<\/TD>/" },
			{ "url" : "/summary.htm", "string" : /<TD ALIGN="right" WIDTH="150"><B>MAC Address:<\/B><\/TD><TD>([\dA-F]{2}:[\dA-F]{2}:[\dA-F]{2}:[\dA-F]{2}:[\dA-F]{2}:[\dA-F]{2})<\/TD><\/TR><\/TABLE>/" },
		]
	return(self.rules)
