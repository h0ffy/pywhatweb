import plugins
			
class Pluginadobe_connect_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<script src="/common/scripts/showContent.js"></script><script type="text/javascript" src="/common/scripts/breezeUI.js"></script><script>" },
			{ "version" : "/<a class="loginHelp" title="([^\s^\"]+)" target="_blank" href="\/common\/help\/[^\/]+\/go\/login_ts\.html"( target="_blank")?>Help<\/a>/" },
			{ "search" : "headers[BREEZESESSION]", "regexp" : "/BREEZESESSION=breez[^;]+;/" },
			{ "url" : "/favicon.ico", "md5" : "b93d28579e6a42ca452c35e8f1eb23ea" },
		]
		return(self.rules)

