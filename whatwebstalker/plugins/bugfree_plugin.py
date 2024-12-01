```python
import plugins

class Pluginbugfree_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "version" : r'/<div id="loginLogo">\s+<img src="Image/login_logo\.png" id="logo" alt=BugFree /><br />\s+<center style="color:#666666;font-size:10px;padding-left:4px;">([^\s^<]+)</center>\s+</div>/' },
            { "version" : r'/<div id="LoginMain">\s+<div id="LoginLogo">\s+<span id="Version">([^\s^<]+)</span>\s+</div>\s+<div id="LoginFormContainer">/' },
            { "version" : r'/<span id="Version"><img src="Image/logo\.png" height=40 title=BugFree />([^\s^<]+)</span>/' },
            { "text" : r'<select name=\'Language\' id=\'Language\' class="NormalSelect MyInput select" onchange="xajax_xSelectLanguage(this.value);return false;" >' },
            { "text" : r'<img src="Image/login_bg_left.gif" class="loginBgImage"/>' },
            { "text" : r'<td><input type="password" name="BugUserPWD" class="MyInput"></td>' },
        ]
        return self.rules
```