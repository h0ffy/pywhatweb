import plugins
			
class Plugincogent_datahub_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/images/Cogent.gif", "md5" : "c8f57d665418321b0248c22cd65efaff" },
			{ "url" : "/scripts/livedata.js", "text" : "timerID = setTimeout ("DataHubConnection.updateTimer()", "this.timerTick);" },
			{ "text" : "<link type="text/css" rel="stylesheet" href="css/dhwebserver.css" />" },
			{ "text" : "<img src="images/Cogent.gif" alt=" width="449" height="47" border="0">" },
			{ "text" : "<!-- The DataHub script that determines if the DataPid is running is at the top of this file. The DataHub script is not visable" },
			{ "certainty" : "25", "text" : "<title>Cogent DataHub WebView</title>" },
			{ "text" : "<!-- The following ASP code generates the table of DataHub point values -->" },
		]
	return(self.rules)
