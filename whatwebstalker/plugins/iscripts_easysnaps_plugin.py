```python
import plugins

class Pluginiscripts_easysnaps_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "text" : '          <td height="25" align="center" bgcolor="#000000">Powered by <a href="http://www.iscripts.com/gallery/" target="_blank">iScripts EasySnaps</a>. A premium product from <a href="http://www.iscripts.com/" target="_blank">iScripts.com</a>' },
        ]
        return self.rules
```