```python
import plugins

class Plugincommonspot_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "regexp" : r'/<meta[^>]+name="Generator"[^>]+content="CommonSpot[^"]+"[^>]*\/>/' },
            { "regexp" : r'/<img[^>]+src="[^"]+commonspot[^"]+"[^>]*\/>/' },
            { "regexp" : r'/<link[^>]+href="[^"]commonspot\/commonspot\.css"[^>]+\/>/' },
            { "version" : r'/<meta[^>]+name="Generator"[^>]+content="CommonSpot[^\\d^"]+([\d\.]+)"[^>]*\/>/' },
        ]
        return self.rules
```