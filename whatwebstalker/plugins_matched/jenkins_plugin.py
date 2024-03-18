import sys
import os
			
class jenkins_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<script>var isRunAsTest=false; var rootURL="[^"]*";<\/script>/ }
			{ "version" : '/<\/span><a href="http:\/\/jenkins\-ci\.org\/">Jenkins ver\. ([^<]+)<\/a>/ }
			{ "search" : 'headers[x-hudson-theme]", "regexp" : '/^.*$/ }
			{ "search" : 'headers[x-instance-identity]", "regexp" : '/^.*$/ }
			{ "search" : 'headers[x-hudson-cli-port]", "regexp" : '/^.*$/ }
			{ "search" : 'headers[x-jenkins]", "version" : '/^(.+)$/ }
			{ "search" : 'headers[x-hudson]", "regexp" : '/^.*$/ }
			{ "search" : 'headers[x-jenkins-cli-port]", "regexp" : '/^.*$/ }
			{ "search" : 'headers[x-ssh-endpoint]", "regexp" : '/^.*$/ }
		]

