```python
import plugins

class Plugingoogle_talk_chatback_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "regexp" : r"/<iframe[^>]+src[\s]*=[\s]*(\'|")http:\\/\\/www.google.com\\/talk\\/service\\/badge\\/Show\\?tk=[^>]+>/" },
        ]
        return self.rules
```