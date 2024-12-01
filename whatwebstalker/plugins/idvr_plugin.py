```python
import plugins

class Pluginidvr_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "text" : "<title>iDVR</title>" },
            { "regexp" : r"codebase='http:\\/\\/\' + szDomainFull + \'\\/NSIDVRCtrlX.ocx#version=[\d]{1},[\d]{1},[\d]{1},[\d]{1}'" },
            { "text" : "classid='clsid:16A017B9-6CB4-47C7-8E81-6E9396FAC2B6'" },
            { "regexp" : r"monitorDiv.innerHTML = '<object id=\'monitorObject\' style=\'display:none\' classid=\'clsid:574B47E8-A366-4AB9-B2EA-57F145CA3780\' codebase=\'lib\\/monitor.cab#version=[\d]{1},[\d]{1},[\d]{1},[\d]{1}\' VIEWASTEXT></object>'" },
            { "version" : "<title>iDVR (.*)[\d\.]+ \(Build ([\d\.]+)\)<\/title>", "offset" : "1" },
        ]
        return self.rules
```