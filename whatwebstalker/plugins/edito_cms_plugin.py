```python
import plugins

class Pluginedito_cms_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "regexp" : r'/<meta name="(g|G)enerator" content="(E|e)dito( CMS)? - www\\.edito\\.pl"[\s]*\/?>/' },
            { "regexp" : r'/Powered by[\s]*:?[\\s]+<a[^>]+href="http:\\/\\/www.edito.pl[\\/]"[^>]+title="Edito CMS"[^>]*>/i' },
        ]
        return self.rules
```