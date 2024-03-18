import sys
import os
			
class siemens_simatic_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "url" : '/Default.html", "text" : '<META HTTP-EQUIV="refresh" content="0;URL=/www/start.html">' },
			{ "url" : '/www/start.html", "text" : '<title> Miniweb Start Page </title>' },
			{ "text" : '<img src="/Images/Siemens_Firmenmarke.gif" alt="Siemens" border="0"></td>' },
			{ "text" : '<font color="#ffffff"> <!-- font ist da", "um bei einer Anzeige OHNE CSS nicht schwarz auf schwarz anzuzeigen -->", "model" : 'HMI" },
			{ "url" : '/Images/Siemens_Firmenmarke.gif", "md5" : '09539daf4dfe27a0157040eb83570ee5", "model" : 'HMI" },
			{ "module" : /	<tr><td class="sph_td"><b>Device Type<\/b><\/td><td class="sph_td">([^<]+)&nbsp;<\/td><\/tr>/ },
			{ "firmware" : '/	<tr><td class="sph_td"><b>Image version<\/b><\/td><td class="sph_td">([^<]+)&nbsp;<\/td><\/tr>/ },
			{ "string" : /	<tr><td class="sph_td"><b>Device Name<\/b><\/td><td class="sph_td">([^<]+)&nbsp;<\/td><\/tr>/ },
			{ "model" : 'HMI", "text" : 'Hint:<br> When the devicename contains an underscore ( _ ) some browsers have a bug that makes it impossible to log in.<br> One possible solution may be to use the IP address of the device instead of the name", "or to use another browser." },
			{ "text" : '<title>SIMATIC NET IT-CP</title>", "model" : 'NET" },
			{ "url" : '/home/siemens.gif", "md5" : 'ecfe2d0a8a1e5dba82120f10f119e327", "model" : 'NET" },
			{ "url" : '/home/itcp.gif", "md5" : '6f3ad9cac1c0ffb5ba09de040752d7ca7", "model" : 'NET" },
			{ "url" : '/__Additional", "module" : /<HTML><HEAD><TITLE>([^<]+) Server Information<\/TITLE><\/HEAD>/ },
			{ "url" : '/__Additional", "module" : /<TABLE BORDER=2><TR><TD><B>Device-Name: <\/B><\/TD><TD>([^<]+)<\/TD><\/TR>/ },
			{ "url" : '/__Additional", "firmware" : '/<TR><TD><B>Firmware-Version: <\/B><\/TD><TD>V([\d\.]+)<\/TD><\/TR>/ },
			{ "text" : '<td class="Login_Area" colspan="2"><img src="/SIMATIC_CONTROLLER.png" alt="Simatic S7 CP"></td>", "model" : 'PCS 7" },
			{ "text" : '<td><img src="/Siemens_Firmenmarke_Header.gif" alt="Siemens" border="0"></td>", "model" : 'PCS 7" },
			{ "url" : '/Siemens_Firmenmarke_Header.gif", "md5" : '157e8a1ebe2786f2e10346d9f518bb99", "model" : 'PCS 7" },
			{ "text" : '<link rel="stylesheet" type="text/css" href="/S7Web.css">' },
			{ "text" : '<td class="MainMenu_Navigation_Level1"><a class="MainMenu_Navigation_Text_Level1" href=\'Portal5000.htm\'>PROFINET IO</a></td>", "model" : 'PCS 7" },
			{ "url" : '/Portal0000.htm", "string" : /<tr>[\r\n\s]*<td class="static_field">Station name:<\/td>[\r\n\s]*<td class="output_field_long">([^<]+)<\/td>/ },
			{ "url" : '/Portal0000.htm", "module" : /<tr>[\r\n\s]*<td class="static_field">Module name:<\/td>[\r\n\s]*<td class="output_field_long">([^<]+)<\/td>/ },
			{ "url" : '/Portal0000.htm", "module" : /<tr>[\r\n\s]*<td class="static_field">Module type:<\/td>[\r\n\s]*<td class="output_field_long">([^<]+)<\/td>/ },
		]

