```python
import plugins

class Pluginapplet_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "string" : r'<applet[^>]+code[\s]*=[\s]*["|\']?([^\\s^>^"^\'^]+)[^>]*>' },
        ]
        return self.rules
```