import sys
import os
			
class Plugintelerik_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "type="text/css" rel="stylesheet" class="Telerik_stylesheet" />" },
			{ "regexp" : "/\$create\(Telerik\.Web\.UI\.Rad[a-zA-Z]+,/" },
			{ "regexp" : "/(src|href)="\/(Telerik.Web.UI.)?WebResource.axd\?/" },
			{ "url" : "/Telerik.Web.UI.WebResource.axd?type=rau", "text" : "{ "message" : "RadAsyncUpload handler is registered succesfully", "however", "it may not be accessed directly." }", "},
		]
		return(self.rules)

