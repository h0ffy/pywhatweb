import plugins


class Pluginhp_system_management_homepage_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {
                "certainty": "75",
                "regexp": "/<TITLE>HP System Management Homepage Login<\\/TITLE>/",
            },
            {"search": "headers[set-cookie]", "regexp": "/Compaq-HMMD=/"},
            {
                "search": "headers[server]",
                "version": "/CompaqHTTPServer\\/[^\\s]+ HP System Management Homepage\\/([\\d\\.]+)$/",
            },
        ]
        return self.rules
