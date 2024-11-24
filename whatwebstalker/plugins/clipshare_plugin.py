import plugins


class Pluginclipshare_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "<!--!!!!!!!!!!!!!!!!!!!!!!!!! Processing SCRIPT !!!!!!!!!!!!!!!!!!!-->"},
            {"text": "<!--!!!!!!!!!!!!!!!!!!!!!!!! LIBRARY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!-->"},
            {"text": "Powered By <a href="http: // www.clip - share.com">ClipShare</a>"},
        ]
        return (self.rules)
