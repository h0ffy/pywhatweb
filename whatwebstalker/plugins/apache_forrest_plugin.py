```python
import plugins

class Pluginapache_forrest_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "text" : '<meta content="Apache Forrest" name="Generator">' },
            { "version" : r'/<meta content="([^"^>]+)" name="Forrest-version"/' },
            { "version" : r'/<meta name="Forrest-version" content="([^"^>]+)"/' },
            { "module" : r'/<meta content="([^"^>]+)" name="Forrest-theme-name"/' },
            { "module" : r'/<meta name="Forrest-theme-name" content="([^"^>]+)"/' },
            { "module" : r'/<meta name="Forrest-skin-name" content="([^"^>]+)"/' },
            { "module" : r'/<meta content="([^"^>]+)" name="Forrest-skin-name"/' },
        ]
        return self.rules
```