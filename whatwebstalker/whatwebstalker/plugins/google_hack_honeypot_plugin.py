import plugins


class Plugingoogle_hack_honeypot_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"module": "PHPFM", "text": "<td>&nbsp;index.php</td><td width=60 align='right'>2,81&nbsp;KB</td><td width=35 align='center'>666</td><td width=110 align='right'>20:36 06-19-2003</td><td width=20>&nbsp;</td><td width=20><a href='?&amp;&amp;path=&amp;filename=index.php&amp;action=edit'><img src='icon/edit.gif' width=20 height=22 alt='Edit file' border=0></a></td><td width=20><a href='?&amp;&amp;path=&amp;filename=index.php&amp;action=rename'><img src='icon/rename.gif' width=20 height=22 alt='Rename file' border=0></a></td><td width=20><a href='?&amp;&amp;path=&amp;filename=index.php&amp;action=download'><img src='icon/download.gif' width=20 height=22 alt='Download file' border=0></a></td><td width=20><a href='?&amp;&amp;path=&amp;filename=index.php&amp;action=delete'><img src='icon/delete.gif' width=20 height=22 alt='Delete file' border=0></a></td></tr><tr><td width=20><img src='icon/text.gif' width=20 height=22 border=0 alt='File'></td><td>&nbsp;readme.txt</td><td width=60 align='right'>2,13&nbsp;KB</td><td width=35 align='center'>666</td><td width=110 align='right'>22:26 06-19-2003</td><td width=20>&nbsp;</td><td width=20><a href='?&amp;&amp;path=&amp;filename=readme.txt&amp;action=edit'><img src='icon/edit.gif' width=20 height=22 alt='Edit file' border=0></a></td><td width=20><a href='?&amp;&amp;path=&amp;filename=readme.txt&amp;action=rename'><img src='icon/rename.gif' width=20 height=22 alt='Rename file' border=0></a></td><td width=20><a href='?&amp;&amp;path=&amp;filename=readme.txt&amp;action=download'><img src='icon/download.gif' width=20 height=22 alt='Download file' border=0></a></td><td width=20><a href='?&amp;&amp;path=&amp;filename=readme.txt&amp;action=delete'><img src='icon/delete.gif' width=20 height=22 alt='Delete file' border=0></a></td></tr><tr><td colspan=9>&nbsp;</td></tr></table></td></tr></table><br /><br /><table class='bottom' cellpadding=0 cellspacing=0><tr><td align='center'>Powered by <a href='http://phpfm.zalon.dk/' target='_new' class='bottom'>PHPFM</a> 0.2.3</td>"},
        ]
        return (self.rules)
