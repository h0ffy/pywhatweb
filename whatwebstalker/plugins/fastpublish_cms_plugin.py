```python
import plugins

class Pluginfastpublish_cms_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "url" : "favicon.ico", "md5" : "e95aa1d29e576c9ebdb08e0c5160cdfa" },
            { "version" : r'/<meta name="Generator" content="fastpublish CMS ([^"]{1,15})">/' },
        ]
        return self.rules
```