import plugins


class Pluginatutor_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
                        {"name" : "Meta Generator", "string" : % r{ < meta name = "Generator" content = "ATutor - Copyright ([0-9]{4}) by http://atutor.ca" / >} },
                        {"name": "JavaScript", "certainty": "75", "text": "ATutor.course = ATutor.course || {};"},
                        {"name": "Documentation link", "text": "<span id="howto">For guidance on using ATutor see the official"},
        ]
        return (self.rules)
