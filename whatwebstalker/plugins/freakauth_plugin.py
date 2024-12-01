```python
import plugins

class Pluginfreakauth_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "regexp" : r"/<title>FreakAuth &raquo; [^<]+<\/title>/" },
            { "regexp" : r"/Welcome on board ! \/ <a href=\"http[^\"+\">Login<\/a>\t\t<\/div>/" },
        ]
        return self.rules
```