import plugins


class Pluginmacs_cms_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "<title>Mac's CMS - Admin Login</title>"},
            {"text": "    <!-- START: This block contains all code that the framework generates -->"},
            {"text": "Site Powered by Mac\'s PHP MVC Framework <a href="http: // macs - framework.sourceforge.net / " target="_blank">Framework of the future</a><br />"},
        ]
        return (self.rules)
