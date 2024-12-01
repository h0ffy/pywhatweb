```python
import plugins

class Plugincomersus_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "regexp" : r'/<meta NAME="DESCRIPTION" CONTENT="Powered by Comersus http:\/\/www.comersus.com">/i' },
            { "regexp" : r'/<title>[^<]*Powered by Comersus ASP Shopping Cart Open Source[^<]*<\/title>/i' },
            { "regexp" : r'/<a href="[^"]*comersus_showCart.asp">/i' },
            { "regexp" : r'/Powered by <[^>]*>Comersus<\/a>/i' },
        ]
        return self.rules
```