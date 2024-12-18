import plugins


class Pluginsymantec_endpoint_protection_manager_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "<tr><td align="left" style="font - family: Arial
             font - size: 18pt"><b>Symantec Endpoint Protection Manager<br>Web Access</b></td></tr>"},
            {"text": "<!-- Now", "if it is IE on Windows platform", "we check to see which version of JWS is installed -->"},
            {"url": "/portal/About.jsp", "version": "/<div style="font - family: Tahoma", "Verdana", "Arial", "Helvetica", "sans - serif
             font - size: 11px
             ">Version ([^\\s^<]+)<\\/div>/"},
        ]
        return (self.rules)
