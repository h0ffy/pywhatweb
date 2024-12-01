```python
import plugins

class Plugindynamicweb_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "version" : r'/<meta name="generator" content="Dynamicweb ([^\s]+)"/' },
            { "certainty" : "100", "regexp" : r'/\(c\) 1999-(20[\d]{2}) Dynamicweb Software A\/S/' },
            { "certainty" : "75", "search" : "headers[set-cookie]", "regexp" : r'/Dynamicweb/' },
        ]
        return self.rules
```