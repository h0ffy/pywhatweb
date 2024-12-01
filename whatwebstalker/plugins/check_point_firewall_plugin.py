```python
import plugins

class Plugincheck_point_firewall_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "search" : "headers[location]", "regexp" : "/\\/fwauthredirect[\\d]{1,3}\\.[\\d]{1,3}\\.[\\d]{1,3}\\.[\\d]{1,3}id[\\d]+$/" },
            { "status" : "401", "string" : "FW-1 at ([^\\s]+): Unauthorized to access the document\\." },
        ]
        return self.rules
```