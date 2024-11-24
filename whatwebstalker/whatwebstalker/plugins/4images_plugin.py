import plugins


class Plugin4images_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"regexp": "/Copyright &copy; 2002-[0-9]{4} <a href=\"http:\\/\\/www.4homepages.de[\\>]*>4homepages.de<\\/a>/"},
            {"version": "/Powered by <b>4images<\\/b> ([\\d\\.]+)/"},
        ]
        return (self.rules)
