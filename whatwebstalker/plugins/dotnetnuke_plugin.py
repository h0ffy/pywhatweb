b'import plugins\n\n\nclass Plugindotnetnuke_plugin(plugins.Base):\n    def __init__(self):\n        self.rules = []\n    def start(self):\n        return self.rules\n'