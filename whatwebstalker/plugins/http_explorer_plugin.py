```python
import plugins

class Pluginhttp_explorer_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "search" : "headers[server]", "version" : r"/^Http explorer ([^\s]+)$/" },
            { "version" : r"/<p id=\"pgfooter_p_main\">\s+<a href=\"http:\/\/http\-explorer\.sourceforge\.net\/\?lang=[^\"]+\">Http explorer\s+([^\s^<]+)<\/a>/" },
        ]
        return self.rules
```