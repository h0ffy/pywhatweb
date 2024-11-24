import plugins


class Pluginstrato_newsletter_manager_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "<td><img src="http: // strato.de / cgi2004 / cgi2.0 / images / transparent120x94.gif" alt="CGI 2004" /></td>"},
            {"certainty": "75", "text": "<title>STRATO Newsletter Manager</title>"},
        ]
        return (self.rules)
