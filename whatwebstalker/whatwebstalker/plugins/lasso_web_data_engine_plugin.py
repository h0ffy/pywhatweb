import plugins


class Pluginlasso_web_data_engine_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"certainty": "25", "ghdb": "filetype:lasso"},
            {"search": "headers[server]", "version": "/Lasso\\/([^\\s]+)/"},
        ]
        return self.rules
