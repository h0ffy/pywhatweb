import sys
import os
			
class ipcop_firewall_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '    <title>IPCop - Main page</title>" }
			{ "text" : '    <style type="text/css">@import url(/include/ipcop.css);</style>'}
			{ "text" : '	<td valign='bottom'><a href='http://sf.net/projects/ipcop/' target='_blank'><img src='/images/sflogo.png' width='88' height='31' alt='Sourceforge logo' /></a></td>" }
			{ "text" : '<td style='background-color: #EAE9EE;' align='left' width='100%'><b>Home</b> | <a href='/cgi-bin/updates.cgi'>Updates</a> | <a href='/cgi-bin/changepw.cgi'>Passwords</a> | <a href='/cgi-bin/remote.cgi'>SSH Access</a> | <a href='/cgi-bin/gui.cgi'>GUI Settings</a> | <a href='/cgi-bin/backup.cgi'>Backup</a> | <a href='/cgi-bin/shutdown.cgi'>Shutdown</a> | <a href='/cgi-bin/credits.cgi'>Credits</a></td></tr></table>" }
			{ "version" : '/	    <img src='\/images\/null.gif' width='1' height='29' alt='' \/>([\d\.]+)<\/td>/ }
			{ "text" : '<!-- IPCOP FOOTER -->' }
			{ "version" : '/<small>IPCop v([^\s]+) &copy; 2001-20[\d]{2} The IPCop Team<\/small><\/td>/ }
			{ "url" : '/include/ipcop.css", "text" : '/* used in status.cgi (among others) */' }
	]

