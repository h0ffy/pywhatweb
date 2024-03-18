import plugins
			
class Pluginjenkins_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script>var isRunAsTest=false; var rootURL="[^"]*";<\/script>/" },
			{ "version" : "/<\/span><a href="http:\/\/jenkins\-ci\.org\/">Jenkins ver\. ([^<]+)<\/a>/" },
			{ "search" : "headers[x-hudson-theme]", "regexp" : "/^.*$/" },
			{ "search" : "headers[x-instance-identity]", "regexp" : "/^.*$/" },
			{ "search" : "headers[x-hudson-cli-port]", "regexp" : "/^.*$/" },
			{ "search" : "headers[x-jenkins]", "version" : "/^(.+)$/" },
			{ "search" : "headers[x-hudson]", "regexp" : "/^.*$/" },
			{ "search" : "headers[x-jenkins-cli-port]", "regexp" : "/^.*$/" },
			{ "search" : "headers[x-ssh-endpoint]", "regexp" : "/^.*$/" },
		]
		return(self.rules)
