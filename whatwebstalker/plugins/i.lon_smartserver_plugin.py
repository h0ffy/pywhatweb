```python
import plugins

class LonSmartserverPlugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = []
        return self.rules
```