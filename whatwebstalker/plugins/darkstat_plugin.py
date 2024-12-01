```python
import plugins

class Plugindarkstat_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "version" : r'/<li class="label">darkstat ([^\s^<]+)<\/li><li><a href="[^"]+">graphs<\/a><\/li>/' },
            { "version" : r'/<title>darkstat ([^\s]+) : graphs ([^\s^\)]+)<\/title>/' },
            { "search" : "headers[server]", "version" : r'/^darkstat\/([^\s]+)$/' },
        ]
        return self.rules
```