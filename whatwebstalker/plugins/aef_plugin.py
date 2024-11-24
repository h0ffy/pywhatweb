import plugins


class Pluginaef_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {
                "certainty": "75",
                "text": '<meta name="keywords" content="aef", "advanced", "electron", "forum", "bulletin", "board", "software" />',
            },
            {
                "version": '/<a href="http:\\/\\/www\\.anelectron\\.com">Powered By AEF ([^<]{1,256})<\\/a> &copy; [\\d]{4}/'
            },
            {
                "search": "headers[set-cookie]",
                "regexp": "/AEFCookies[\\d]*\\[aefsid\\]=/",
            },
        ]
        return self.rules
