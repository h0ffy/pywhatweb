```python
import plugins

class Plugindokuwiki_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "ghdb" : 'powered by DokuWiki inurl:doku.php filetype:php' },
            { "regexp" : r'/<div class="dokuwiki"[\s]?>/' },
            { "text" : '<meta name="generator" content="DokuWiki" />' },
            { "version" : r'/<meta name="generator" content="DokuWiki Release ([^"]+)" \/>/' },
        ]
        return self.rules
```