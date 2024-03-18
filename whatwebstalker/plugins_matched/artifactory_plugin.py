import sys
import os
			
class artifactory_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<html ng-app="artifactory.ui">' }
			{ "text" : '<body jf-body-class ng-class="{\'load-complete\':jfBodyClass.isLoadCompleted()}">' }
			{ "url" : '/ui/auth/screen/footer", "version" : '/"buildNumber":"([\d\.]+ rev \d+)"/ }
			{ "url" : '/artifactory/ui/auth/screen/footer", "version" : '/"buildNumber":"([\d\.]+ rev \d+)"/ }
		]

