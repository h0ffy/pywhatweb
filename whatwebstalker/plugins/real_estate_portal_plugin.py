import plugins


class Pluginreal_estate_portal_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "Powered by <a href="http: // www.netartmedia.net / realestate" target="_blank">Real Estate Portal</a>"},
            {"text": "Powered by <a href="http: // www.netartmedia.net / realestate">Real Estate Portal</a>"},
            {"text": "			document.form1.property_type.options[i] = new Option(CurrentModels[i]", "CurrentModels[i]", "0", "0);"},
        ]
        return (self.rules)
