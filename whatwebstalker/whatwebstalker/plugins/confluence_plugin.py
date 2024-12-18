import plugins


class Pluginconfluence_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"certainty": "75", "ghdb": "Atlassian Confluence" "the Enterprise Wiki" "Intranet software for documentation and knowledge management" "Report a bug"" },
			{ "text" : "<meta id="confluence-context-path" name="confluence-context-path" content=">" },
			{ "text" : "<li class="noprint"><a href="http://www.atlassian.com/software/confluence" class="hover-footer-link">Atlassian Confluence</a>" },
			{ "version" : "/Powered by <a href="http:\/\/www\.atlassian\.com\/software\/confluence"[^>]*>Atlassian Confluence<\/a> ([\d\._]+)/" },
		]
	return(self.rules)
