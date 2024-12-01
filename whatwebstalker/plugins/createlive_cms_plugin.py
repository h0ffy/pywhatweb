```python
import plugins

class Plugincreatelive_cms_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "version" : r'/Powered by:(<a href="http:\\/\\/www.aspoo.cn\\/" target="_blank">)?CreateLive CMS Version ([\\d\\.]+)/i' },
            { "version" : r'/<!--By CreateLiveCms (\d)\\.00-->/' },
            { "search" : "headers[set-cookie]", "regexp" : r'/Kill=kill=(Yes|No)/' },
        ]
        return self.rules
```