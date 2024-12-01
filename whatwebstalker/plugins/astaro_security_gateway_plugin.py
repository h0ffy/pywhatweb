```python
import plugins

class Pluginastaro_security_gateway_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "text" : '<script src="wfe/asg/js/app_selector.js?t=">' },
            { "certainty" : "75", "text" : '<script src="wfe/asg/js/_variables_from_backend.js?t=">' },
            { "url" : "/core/img/topbar/topbar_center.png", "md5" : "2e6cdce49c669ec305b2d73eead50e4c", "version" : "8.x" },
        ]
        return self.rules
```