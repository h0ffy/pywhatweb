import plugins


class Pluginpivotal_crm_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"ghdb": "filetype:asp inurl:"xmlloader.asp" "var g_LDSTRING_HEADER_ERROR_CLIENT_ERROR= ""},
            {"text": "&lt;script language=&quot;javascript&quot; src=&quot;javascript/utils.js&quot;&gt;&lt;/script&gt;&lt;script language=&quot;javascript&quot; src=&quot;javascript/navigation.js&quot;&gt;&lt;/script&gt;&lt;script language=&quot;javascript&quot;&gt;"},
            {"text": "<frame name="hidden" src="xmlloader.asp?type = portal" marginwidth="0" marginheight="0" scrolling="no" noresize>"},
            {"text": "<frame name="hidden" title="Hidden" src="xmlloader.asp?type = portal" marginwidth="0" marginheight="0" scrolling="no" noresize>"},
        ]
        return (self.rules)
