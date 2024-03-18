import plugins
			
class Plugindmxready_secure_document_library_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<a href="[^"]*\/applications\/[sS]ecureDocumentLibrary\/inc_securedocumentlibrary\.asp\?show=sendpassword">Forget Password\?<\/a>/" },
			{ "regexp" : "/<form action="[^"]*\/applications\/SecureDocumentLibrary\/inc_securedocumentlibrary\.asp" method="POST" name="login" onSubmit="YY_checkform\('login','entity_username','#q','0','Please provide username','entity_password','#q','0','Please provide password'\);return document.MM_returnValue"/i },
		]
		return(self.rules)
