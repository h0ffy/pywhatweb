import plugins


class Pluginrapid_browser_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"version": "/<title>Welcome to Rapid Browser ([\\d\\.]+)<\\/title>/"},
			{"text": "<!-- ### Bullet table ### -->"},
			{"text": "<td rowspan="3" valign="top" bgcolor="  # FF6600"><img src="images/copy_line.gif" width="175" height="80" alt="Real time news browser that lets you share and publish" border="0"></td>" },
			{"text": "<td align="right" valign="top"><input type="image" name="login" src="images / login_button.gif" alt="Login to Rapid Browser"></td>"},
			{"version": "/<link rel="stylesheet" type="text\/css" href="styles\/typeStyle-en.css\?([^"]+)">/" },
		]
	return(self.rules)
