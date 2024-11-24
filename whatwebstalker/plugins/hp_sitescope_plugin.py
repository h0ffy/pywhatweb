import plugins


class Pluginhp_sitescope_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "<center><H2>SiteScope Login</H2></center><hr>"},
            {
                "url": "/",
                "version": "/<p class=fine align=center><small>SiteScope ([\\d\\.]+)/",
            },
        ]
        return self.rules
