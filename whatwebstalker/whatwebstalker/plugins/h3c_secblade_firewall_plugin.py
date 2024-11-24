import plugins


class Pluginh3c_secblade_firewall_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"search": "headers[server]", "regexp": "/^Switch$/"},
            {"text": "<script language=javascript src="js / MulPlatAPI.js"></script>"},
            {"text": "<a href=".. / cn / login.html"><img border="0" src=".. / images / Cnlink.jpg" alt="Chinese"></a>"},
            {"text": "<a href=".. / en / login.html"><img border="0" src=".. / images / Enlink.jpg" alt="English"></a>"},
            {"text": "<script language=javascript src=" / js / MulPlatAPI.js"></script>"},
        ]
        return (self.rules)
