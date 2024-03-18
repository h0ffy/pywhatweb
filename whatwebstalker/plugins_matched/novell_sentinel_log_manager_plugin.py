import sys
import os
			
class Pluginnovell_sentinel_log_manager_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/<h1 id="site-logo" class="logo" title="Novell Sentinel Log Manager"><span class="accessible">Novell Identity Audit<\/span><\/h1>\s+<p class="publisher">Novell<\/p>\s+<p class="version">Version ([^>]+)<\/p>/" },
			{ "text" : "<p class="content">Novell Sentinel Log Manager supports Firefox 3 (works best on 3.6) and Internet Explorer 8 (works best on 8.0)</p>" },
			{ "text" : "<META HTTP-EQUIV="refresh" CONTENT="0;URL=/novelllogmanager">" },
		]

