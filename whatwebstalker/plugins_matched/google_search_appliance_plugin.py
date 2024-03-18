import plugins
			
class Plugingoogle_search_appliance_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<font face=arial,sans-serif size=-1>If you are an end user looking for a Google search service on your network", "please ask your system administrator for the URL of the search service.<p>" },
			{ "certainty" : "75", "search" : "headers[server]", "regexp" : "/^GSE$/" },
			{ "certainty" : "75", "search" : "headers[location]", "regexp" : "/^\/EnterpriseController/" },
			{ "text" : "<tr id="TopBar"><td id="TopBarName">About Google Search Appliance</td></tr></table></td></tr></table>" },
			{ "text" : "<tr id="TopBar"><td id="TopBarName">Welcome to the Google Search Appliance!</td></tr></table></td></tr></table>" },
			{ "text" : "<tr id="TopBar"> <td id="TopBarName">  Welcome to the Google Mini!  </td> </tr> </table>" },
			{ "version" : "/<\/font>[\s]+<br><br>[\s]+<font face="arial,sans-serif">System Version:[\s]+([^\s]+)[\s]+<\/font>[\s]+<br><br>[\s]+<font face="arial,sans-serif">Appliance ID:/" },
		]
		return(self.rules)
