import sys
import os
			
class phpquestionnaire_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<tr><td></td><td colspan="2"><h2>Survey List</h2></td></tr>' },
			{ "text" : '	<tr><td colspan="2"><hr size="1" noshade /></td></tr><tr><td colspan="2">Currently no available surveys.</td></tr>	</table>' },
			{ "text" : '   TEXTAREA      { font-family: verdana,arial,helvetica; font-size: 12px; width: 400px; height: 60px; }' },
			{ "text" : '   TEXTAREA      { font-family: verdana,arial,helvetica; font-size: 10px; width: 400px; height: 60px; }' },
			{ "text" : '			<td align="right">powered by <a href="http://www.chumpsoft.com">phpQuestionnaire</a></td>' },
			{ "text" : '			<td align="right">powered by phpQuestionnaire</td>' },
			{ "md5" : 'feae34c62729c85af0b4114bd02d634a", "url" : 'templates/default/images/logo.gif' },
			{ "version" : '/      <TD ALIGN=right><NOBR><B><A HREF="http:\/\/www.chumpsoft.com\/products\/phpq\/" class=link>phpQuestionnaire<\/A> ([\d\.]+) &copy [0-9]{4}-[0-9]{4}/ },
		]

