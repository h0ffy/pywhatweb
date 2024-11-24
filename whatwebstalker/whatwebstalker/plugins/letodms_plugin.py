import plugins


class Pluginletodms_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "<div class="disclaimer">This is a classified area. Access is permitted only to authorized personnel. Any violation will be prosecuted according to the national and international laws.</div>"},
            {"text": "letoDMS free document management system - www.letodms.com</div></body>"},
            {"search": "headers[location]", "regexp": "/out\\/out\\.ViewFolder\\.php/"},
        ]
        return (self.rules)
