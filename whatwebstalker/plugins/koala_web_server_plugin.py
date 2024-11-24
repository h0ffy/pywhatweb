import plugins


class Pluginkoala_web_server_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"search": "headers[server]", "regexp": "/^Koala Web Server/"},
            {"search": "headers[server]", "version": "/^Koala Web Server\\/([^\\s]+)/"},
        ]
        return self.rules
