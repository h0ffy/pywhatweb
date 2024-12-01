```python
import plugins

class Pluginiptime_router_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "model" : r"<head><title>EFM Networks ipTIME ([A-Z0-9]+)<\/title>" },
            { "model" : r"<head><title>EFM networks - ipTIME ([A-Z0-9]+)<\/title>" },
            { "url" : "/login/login.cgi", "string" : r"([\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3})<\/span><br>[\s]*<span class=item_text><b>Version [\d\.]+<\/b><\/span>" },
            { "url" : "/login/login.cgi", "firmware" : r"(No IP|[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3})<\/span><br>[\s]*<span class=item_text><b>(F\/W )?Version ([\d\.]+)<\/b><\/span>", "offset" : 2 },
        ]
        return self.rules
```