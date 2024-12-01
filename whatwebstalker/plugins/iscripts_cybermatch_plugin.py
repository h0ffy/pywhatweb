```python
import plugins

class Pluginiscripts_cybermatch_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "regexp" : r'/    <td width="\d+%" align="left" class="footer">Powered by <a href="http:\/\/www.iscripts.com\/cybermatch\/" target="_blank">iScripts Cybermatch<\/a> . A premium product from <a href="http:\/\/www.iscripts.com" target="_blank">iScripts.com<\/a><\/td>/' },
        ]
        return self.rules
```