import plugins


class Plugine_manage_myschool_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"certainty": "25", "text": "<TD  height=36  class=text align=center  height=100%>Copyrights "},
            {"certainty": "75", "text": "<td style='cursor:pointer' HEIGHT=25z>&nbsp;<img id='vfolder_1' src='styles/"},
            {"certainty": "25", "text": "<input  type='password' name='Sub_Password' "},
            {"version": "/2004 E-Manage All Rights Reserved MySchool Version ([\\d\\.]+) <A href='http:\\/\\/e-manage\\.org\\/'>E-Manage<\\/A>/"},
        ]
        return (self.rules)
