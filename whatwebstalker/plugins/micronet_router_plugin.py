import plugins


class Pluginmicronet_router_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {
                "certainty": "75",
                "search": "headers[server]",
                "version": "/^RCTTools \\(SecureSOHO Web configuration Tools\\) v([^\\s]+)$/",
            },
            {
                "url": "/image/iso-8859-1/logo.jpg",
                "md5": "25acf0f5466c0ba42901a0a0b3251f5d",
                "model": "SP888B",
            },
        ]
        return self.rules
