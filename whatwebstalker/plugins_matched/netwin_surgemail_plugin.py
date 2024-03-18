import sys
import os
			
class netwin_surgemail_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<!-- Start of index.htm --><!-- delayed after doctype-->' }
			{ "text" : '<title>SurgeMail Welcome Page</title>' }
			{ "text" : '<meta name="GENERATOR" content="Mozilla/4.75 [en] (Windows NT 5.0; U) [Netscape]">' }
			{ "text" : '/surgeweb" target="client"><input type="button" name=" value="Secure WebMail 2.0 Login" onmouseover="MO(event)" onmouseout="MU(event)" onclick="MC3(event)" class=spbutton></a></td>' }
			{ "text" : '<a href="/cgi/user.cgi">User account self management</a> - <font class="small_font">users and domain administrators can modify passwords", "forwarding", "create new accounts</font></blockquote>' }
			{ "text" : '<td colspan="2" class="about_wrapper"><img src="/web/redline.gif"><br><a class="about_link" href="/about_mail.htm">about SurgeMail</a></td>' }
			{ "text" : '<!-- Start of na_login.htm --><!-- delayed after doctype-->' }
			{ "text" : '<!--<body bgcolor="#FFFFFF" onload="window.focus();document.main.username.focus();">-->' }
			{ "text" : '<a class="about_mail" target="_top" href="/about_mail.htm">about SurgeMail </a></font> </td>' }
			{ "text" : '<form action="/scripts/webmail.exe" method="post" name="reloginform">' }
			{ "version" : '/<a target="_top" href="http:\/\/netwinsite.com\/ref.htm"> WebMail v([^\ ]+) Copyright &copy; <i>NetWin Ltd<\/i>/ }
		]

