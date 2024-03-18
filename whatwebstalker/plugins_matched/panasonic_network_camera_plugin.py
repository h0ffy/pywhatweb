import plugins
			
class Pluginpanasonic_network_camera_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<HEAD><TITLE>WJ-NT104 MAIN PAGE</TITLE></HEAD>", "version" : "WJ-NT104" },
			{ "text" : "      <FONT FACE="Arial" STYLE="font-size: 24px" COLOR="#ffffff"><B>Network Camera</B></FONT>" },
			{ "regexp" : "/<BODY BACKGROUND="image\/Hcm1[0]?\.gif" 		[\t]?BGCOLOR="#efefef" TEXT="#000000" LINK="#000000" 			VLINK="#000000" ALINK="#000000">/" },
			{ "regexp" : "/<FRAME name=bar src="CgiTagMenu\?page=[^&]+&Language=[\d]+" scrolling=no NORESIZE>/" },
			{ "text" : "<META name="copyright" content="Copyright (C) 2003 Matsushita Electric Industrial Co.", "Ltd. All rights reserved.">" },
			{ "text" : "<TITLE>Digital Disk Recorder WJ-HD220 CONTROL MAIN PAGE</TITLE>", "version" : "WJ-HD220" },
			{ "text" : "<TITLE>WJ-HD200 DigitalDiskRecorder CONTROL MAIN PAGE</TITLE>", "version" : "WJ-HD200" },
			{ "text" : "window.location.replace("/view/idconv.cgi?UID=%i&FILE=/hdrindex.html&PAGE="+myDate.getTime());" },
		]
			return(self.rules)
