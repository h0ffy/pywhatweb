import plugins


class Pluginwebasyst_shop_script_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "Powered by WebAsyst Shop-Script <a href="http: // www.shop - script.com / " style="font - weight: normal">shopping cart software</a>"},
            {"text": "Powered by <a href="http: // www.shop - script.com" style="font - weight: bold
             " target="_blank">WebAsyst Shop-Script</a> - <a href="http: // www.shop - script.com / " style="font - weight: normal
             " target="_blank">shopping cart software</a>"},
            {"regexp": "/[\\s]+var WAROOT_URL = '[^\']+';\\/\\/ok/"},
            {"md5": "34a3750e95f81f5bb7b552393b3b37b6", "url": "published/common/html/res/images/logo.gif"},
            {"md5": "d7139ea1c479be1993d01e22e2c36a12", "url": "images/logos/wa_logo136_white.gif"},
        ]
        return (self.rules)
