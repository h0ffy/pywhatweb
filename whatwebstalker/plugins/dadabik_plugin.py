```python
import plugins

class Plugindadabik_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "version" : r'/<meta name="Generator" content="DaDaBIK ([^"^>]{1,10}) - http:\/\/www\.dadabik\.org\/">/' },
            { "text" : r'<div class="powered_by_dadabik" align="right">Powered by: <a href="http://www.dadabik.org/">DaDaBIK</a> database front-end</div>' },
        ]
        return self.rules
```