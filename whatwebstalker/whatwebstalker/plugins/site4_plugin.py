import plugins


class Pluginsite4_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"path": "/error.asp", "text": "<title>SITE4.dk Site4 Setup Error..</title>"},
            {"text": "<div class="caption" align="center"><b>A Site4 event or error occured..</b></div></td>"},
            {"text": "To read more about SITE4.dk please <a class="smalltext" style="text - decoration: none
             " href="http: // www.site4.dk"><b>click here</b></a>"},
        ]
        return (self.rules)
