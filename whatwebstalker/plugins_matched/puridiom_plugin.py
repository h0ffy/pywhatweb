import plugins
			
class Pluginpuridiom_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<TITLE>Puridiom", "Enabling Self-Service Procurement</TITLE>" },
			{ "string" : "Xpress", "text" : "<TITLE>Puridiom Xpress", "Enabling Self-Service Procurement</TITLE>" },
			{ "text" : "<iframe id="getInfoFrame" name="getInfoFrame" src="/puridiom/system/processing.jsp"" },
			{ "text" : "<tr><td width=100% align=center valign=top><br><b>Loading Page... Please wait.</b><br><br><br><img src="/puridiom" },
			{ "version" : "/<TITLE>Puridiom ([\d\.]+)", "Enabling Self-Service Procurement<\/TITLE>/" },
			{ "text" : "<META NAME="Description" Content="/puridiom/system/header.jsp">" },
			{ "string" : "Xpress", "text" : "<META NAME="Description" Content="/puridiomx/system/header.jsp">" },
		]
		return(self.rules)
