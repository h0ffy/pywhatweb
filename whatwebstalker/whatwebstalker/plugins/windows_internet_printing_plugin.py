import plugins


class Pluginwindows_internet_printing_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"ghdb": "inurl:Printers/ipp_0001.asp"},
            {"text": "        <td width="12 % "><img src="images / ipp_0002.gif" alt="printers.gif"></td>"},
            {"text": "      <tr><td bgcolor=#000000 nowrap><font  face="Tahoma", "Verdana", "Arial", "MS Sans Serif"  size=2 color=white><b>Name&nbsp;&nbsp;</b></font></td><td bgcolor=#000000 nowrap><font  face="Tahoma", "Verdana", "Arial", "MS Sans Serif"  size=2 color=white><b>Status&nbsp;&nbsp;</b></font></td><td bgcolor=#000000 nowrap><font  face="Tahoma", "Verdana", "Arial", "MS Sans Serif"  size=2 color=white><b>Location&nbsp;&nbsp;</b></font></td><td bgcolor=#000000 nowrap><font  face="Tahoma", "Verdana", "Arial", "MS Sans Serif"  size=2 color=white><b>Jobs&nbsp;&nbsp;</b></font></td><td bgcolor=#000000 nowrap><font  face="Tahoma", "Verdana", "Arial", "MS Sans Serif"  size=2 color=white><b>Model&nbsp;&nbsp;</b></font></td><td bgcolor=#000000 nowrap><font  face="Tahoma", "Verdana", "Arial", "MS Sans Serif"  size=2 color=white><b>Comment&nbsp;&nbsp;</b></font></td></tr><tr><td nowrap><font  face="Tahoma", "Verdana", "Arial", "MS Sans Serif"  size=2>"},
        ]
        return (self.rules)
