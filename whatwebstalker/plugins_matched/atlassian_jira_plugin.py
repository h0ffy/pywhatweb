import plugins
			
class Pluginatlassian_jira_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<noscript><h1>Warning: either you have javascript disabled or your browser does not support javascript. To work properly", "this page requires javascript to be enabled.</h1></noscript>" },
			{ "text" : "<a class="seo-link" href="http://www.atlassian.com/software/jira/bug-tracking.jsp">Bug tracking</a> and <a class="seo-link" href="http://www.atlassian.com/software/jira/tour/project-tracking.jsp">project tracking</a> for <a class="seo-link" href="http://www.atlassian.com/software/jira/tour/software-development.jsp">software development</a> powered by <a href="http://www.atlassian.com/software/jira" class="smalltext">Atlassian JIRA</a>" },
			{ "version" : "/<span id="footer-build-information"  style="color: #666666;" >\(([^\)^\s]+)\)<\/span>/" },
			{ "text" : "<meta name="decorator" content="atl.general">" },
		]
		return(self.rules)
