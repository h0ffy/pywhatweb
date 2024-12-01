```python
import plugins

class Plugincinvoice_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "version" : r'/<small>Powered by <a href="http:\\/\\/www\\.forperfect\\.com\\/" class="footerlink">cInvoice system ([\\d\\.]+)<\\/a><\\/small>/' },
            { "regexp" : r'/\\/images\\/footer_bg\\.gif" width="[\\d]{2}%" align="center" cellspacing="1" cellpadding="1"><td class=copyright align="center">/' },
        ]
        return self.rules
```