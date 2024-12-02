import plugins


class Pluginphpwcms_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {
                "text": "	phpwcms is copyright 2003-2010 of Oliver Georgi. Extensions are copyright of"
            },
            {
                "text": "	created by Oliver Georgi (oliver at phpwcms dot de) and licensed under GNU/GPL."
            },
        ]
        return self.rules
