import plugins


class Pluginmojoportal_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"certainty": "25", "ghdb": "Powered by mojoPortal"" },
			{ "text" : "<a href='http://www.mojoportal.com' >Powered by mojoPortal</a>" },
			{ "text" : "<a href='http://www.mojoportal.com'  title='mojoPortal.com'>Powered by mojoPortal</a>" },
			{ "certainty" : "25", "regexp" : "/<head id="ct[0-9]+_Head[0-9]+"><title>/i },
			{ "text" : "	<img src="../Data/SiteImages/mojoportal-logo-med.gif" alt="mojoPortal Content Management System" />" },
			{ "text" : "<link id="Link1" runat="server" rel="stylesheet" href="../Data/style/setup.css" type="text/css"  />" },
		]
	return(self.rules)
