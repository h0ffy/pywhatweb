import plugins


class Pluginadaptcms_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"version": "/Powered by <a href=\"http:\\/\\/www.adaptcms.com\">[<b>]*AdaptCMS([^<]*)<\\/a>/"},
        ]
        return (self.rules)
