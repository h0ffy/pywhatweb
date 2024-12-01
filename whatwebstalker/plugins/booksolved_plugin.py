```python
import plugins

class Pluginbooksolved_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "text" : "<!-- BOOKSolved - Copyright by www.usolved.net -->" },
            { "version" : r"/<!-- BOOKSolved v([^\s]+)- Copyright by www\\.usolved\\.net -->/" },
            { "version" : r"/<tr><td style=\"text-align: center;\">[\s]*BOOKSolved ([^\s]+) &copy; by <a href=\"http:\\/\\/www\\.usolved\\.net\" (target=\"_blank\" )?class=\"menu\">USOLVED<\\/a>/" },
        ]
        return self.rules
```