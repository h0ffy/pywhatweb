import plugins


class Pluginop5_monitor_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "<title>op5 Monitor login</title>"},
            {"text": "<link type="text / css" rel="stylesheet" href=" / monitor / application / views / themes / default / css / default / common.css" />"},
            {"url": "/monitor/application/views/themes/default/icons/16x16/favicon.ico", "md5": "7ed48f7e1e0b8d6ead4317f84b64ab86"},
        ]
        return (self.rules)
