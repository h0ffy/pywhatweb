import plugins


class Pluginkeyfocus_webserver_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"search": "headers[server]", "regexp": "/^KFWebServer$/"},
            {"search": "headers[server]", "version": "/^KFWebServer\\/([\\d\\.]+)/"},
        ]
        return self.rules
