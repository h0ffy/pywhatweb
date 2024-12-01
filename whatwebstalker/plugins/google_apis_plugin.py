```python
import plugins

class Plugingoogle_apis_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "regexp" : r"/<script[^>]+src[\s]*=[\s]*[\"|']?http:\/\/www.google.com\/jsapi[^>]*>[\s]*<\/script[\s]*>/i", "string" : "Dynamic" },
            { "regexp" : r"/<script[^>]+src[\s]*=[\s]*[\"|']?http:\/\/ajax.googleapis.com\/([a-zA-Z0-9\/\.-_]+)[\"|']?[^>]*>[\s]*<\/script[\s]*>/i" },
        ]
        return self.rules
```