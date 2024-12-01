```python
import plugins

class Pluginbulletlink_newspaper_template_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "text" : "<br><div style='width: px; margin-left: auto; margin-right: auto;'><br><center><a href='http://bulletlink.com' target=_blank><font size=1>{ powered by bulletlink.com }</font></a></center><br></div>" },
            { "certainty" : "75", "text" : "<link rel='stylesheet' href='/ModalPopup/core-modalpopup.css' type='text/css'>" },
            { "text" : "<div class='copyright'><script type='text/javascript' language='JavaScript'>GetCopyright();</script>&nbsp;&nbsp;&nbsp;<a class='copyright' href='/sitemap.asp'>sitemap</a></div>" },
        ]
        return self.rules
```