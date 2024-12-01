```python
import plugins

class Plugincontent_security_policy_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "search" : "headers[x-content-security-policy]", "string" : r"^(.*)$/" },
            { "search" : "headers[x-webkit-csp]", "string" : r"^(.*)$/" },
        ]
        return self.rules
```