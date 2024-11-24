import plugins


class Pluginorite_301_camera_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "	<TITLE>ORITE Audio IP-Camera IC-301 </TITLE>"},
            {"text": "<TITLE>Orite IC301</TITLE>"},
            {"text": "	var s=\'<frameset cols="220", " * " id=totalframeset frameborder="NO" border="0" framespacing="0" noresize>\'"},
        ]
        return (self.rules)
