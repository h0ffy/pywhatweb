```python
import plugins

class Pluginfcms_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "text" : '<meta name="author" content="Ryan Haudenschilt"/>' },
            { "regexp" : r"/- [pP]owered by Family Connections<\/title>/" },
            { "version" : r"/- [pP]owered by Family Connections ([^\s^<]+)[\s]*<\/title>[\s]*(<meta|<link)/" },
        ]
        return self.rules
```