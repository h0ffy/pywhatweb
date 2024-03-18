import plugins
			
class Plugintanberg_videoconference_management_system_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta NAME="AUTHOR" CONTENT="TANDBERG ASA (http://www.tandberg.net)">" },
			{ "text" : "content="TANDBERG is a leading global provider of videoconferencing solutions. The company designs", "develops and manufactures videoconferencing systems and offers sales", "support and value-added services in more than 50 countries worldwide.">" },
			{ "text" : "<title>TANDBERG</title>" },
			{ "text" : "		<frame src="framemiddle.htm" name="No Name" noresize marginheight="0">" },
			{ "text" : "	<title>Middle frame of Videoconference Management System</title>" },
		]
	return(self.rules)
