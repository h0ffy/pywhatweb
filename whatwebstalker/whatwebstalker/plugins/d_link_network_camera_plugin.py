import plugins


class Plugind_link_network_camera_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "<title>DCS-5300</title></head>", "version": "DCS-5300"},
            {"text": "<TITLE>DCS-950G</TITLE>", "version": "DCS-950G"},
            {"text": "if (document.domain.toLowerCase() == "DCS - 950G".toLowerCase())", "version": "DCS-950G"},
        ]
        return (self.rules)
