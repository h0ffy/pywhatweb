import plugins
			
class Pluginartifactory_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<html ng-app="artifactory.ui">" },
			{ "text" : "<body jf-body-class ng-class="{\'load-complete\':jfBodyClass.isLoadCompleted()}">" },
			{ "url" : "/ui/auth/screen/footer", "version" : "/"buildNumber":"([\d\.]+ rev \d+)"/" },
			{ "url" : "/artifactory/ui/auth/screen/footer", "version" : "/"buildNumber":"([\d\.]+ rev \d+)"/" },
		]
		return(self.rules)
