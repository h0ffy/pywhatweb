import plugins
			
class Pluginpluxml_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<a href="http:\/\/pluxml.org" title="Blog ou Cms sans base de donn&eacute;es">Pluxml<\/a>[\s]+([\d\.]+)/" },
			{ "text" : "par <a href="http://pluxml.org">Pluxml</a></p>" },
			{ "regexp" : "/Powered by <a href="http:\/\/pluxml\.org/" },
			{ "text" : "<title>PluXml - Page d'authentification</title>" },
			{ "text" : "<p class="auth_return"><a href="../../">Retour au site</a>" },
			{ "text" : "G&eacute;n&eacute;r&eacute; par <a href="http://pluxml.org" title="Blog ou Cms sans base de donn&eacute;es">PluXml</a>" },
			{ "text" : "G&eacute;n&eacute;r&eacute; par <a href="http://pluxml.org">PluXml</a></p>" },
		]
	return(self.rules)
