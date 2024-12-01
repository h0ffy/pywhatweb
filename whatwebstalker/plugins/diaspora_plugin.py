```python
import plugins

class Plugindiaspora_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "search" : "headers[set-cookie]", "regexp" : "/_diaspora_session=/" },
            { "search" : "headers[x-git-update]", "string" : r"^([\d]{4}-[\d]{2}-[\d]{2} [\d]{2}:[\d]{2}:[\d]{2} .+)$" },
            { "search" : "headers[x-git-revision]", "regexp" : r"/^[a-f\d]{32}$/" },
            { "text" : '<input name="user[remember_me]" type="hidden" value="0" /><input id="user_remember_me" name="user[remember_me]" type="checkbox" value="1" />' },
        ]
        return self.rules
```