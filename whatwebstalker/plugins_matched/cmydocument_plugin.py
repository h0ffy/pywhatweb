import plugins
			
class Plugincmydocument_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<link href="CmyDocument.css" rel="stylesheet" type="text/css">" },
			{ "text" : "<link href="CmyDocument2.css" rel="stylesheet" type="text/css">" },
			{ "text" : "<link rel="stylesheet" type="text/css" href="CmyDocument.css">" },
			{ "text" : "<link rel="SHORTCUT ICON" href="icon_cmydoc.ico">" },
			{ "text" : "<!-- footer (begin) --><!-- *** Note: Only licensed users are allowed to remove or change the following copyright statement. *** -->" },
			{ "regexp" : "/<td style="white-space: nowrap;"><span class="aspmaker"><a href="myDocview\.asp\?(myDocID|ID)=[\d]+">View<\/a><\/span><\/td>/" },
		]
		return(self.rules)
