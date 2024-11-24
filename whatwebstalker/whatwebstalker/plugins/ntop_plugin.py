import plugins


class Pluginntop_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"search": "headers[server]", "version": "/^ntop\\/([^\\s]+)/"},
            {"text": "<link rel="alternate" type="application / rss + xml" title="ntop RSS Feed" href="http: // www.ntop.org / blog / ?feed = rss2" />"},
            {"certainty": "75", "text": "<TITLE>Global Traffic Statistics</TITLE>"},
            {"search": "headers[www-authenticate]", "text": "Basic realm="NTOP""},
        ]
        return (self.rules)
