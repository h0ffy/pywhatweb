```python
import plugins

class Plugininfomaster_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "version" : r"/<head><title>\s+MasterView ([\d\.]+) Property Master\s+<\/title>/", "string" : "MasterView" },
            { "regexp" : r"/class=\"ackn\">\s*Powered by InfoMaster/" },
            { "text" : "<link href=\"../../MasterView.css\" type=\"text/css\" rel=\"stylesheet\"", "string" : "MasterView" },
            { "text" : "<link href=\"../../App_Themes/MasterView/MPLeftNavStyle/PanelBar.MPIFMA.css\" type=\"text/css\" rel=\"stylesheet\" />", "string" : "MasterView" },
            { "text" : "<script language=\"javascript\" src=\"../../common/masterView.js\"></script>", "string" : "MasterView" },
            { "string" : r"/<form name=\"frm(MasterView|MasterPlan)\" method=\"post\" action=\"default\.aspx/" },
        ]
        return self.rules
```