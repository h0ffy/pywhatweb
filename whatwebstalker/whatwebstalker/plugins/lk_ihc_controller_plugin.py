import plugins


class Pluginlk_ihc_controller_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "<title>LK IHC controller forside</title>"},
            {"text": "<table width="640" height="480" border="0" cellspacing="0" cellpadding="0"  background="images / bg_image_LK.jpg">"},
            {"url": "/images/bg_image_LK.jpg", "md5": "c23378580cb58ee4c404106dda5757b3"},
        ]
        return (self.rules)
