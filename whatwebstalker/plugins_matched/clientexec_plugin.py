import plugins
			
class Pluginclientexec_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- These should not have debug at the end for production -->" },
			{ "text" : "<title>Support Center - Powered By ClientExec</title>" },
			{ "text" : "<form action="index.php?fuse=admin&amp;action=Login&amp;public=1" method="post"" },
			{ "module" : /<img class="logo" src="templates\/([^\/]+)\/images\/public\/caption_photo\.jpg" alt="clientexec" \/>/" },
		]
		return(self.rules)
