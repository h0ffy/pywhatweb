import plugins
			
class Pluginkoobi_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/Powered by <a title="Koobi ist ein komfortables und leistungsf&auml;higes Content-Management-System \(CMS\) f&uuml;r Privatpersonen", "Vereine", "kleine und mittelst&auml;ndische Unternehmen", "die einen professionellen Internetauftritt realisieren m&ouml;chten."[^>]+>Koobi/i },
			{ "text" : "<!-- powered by koobi - do not remove this info! -->" },
			{ "version" : "/powered by <a class="foot" href="http:\/\/www.dream4.de\/[^>]+>Koobi Pro ([\d\.]+)<\/a>/i", "string" : "Pro" },
			{ "version" : "/<meta name="generator" content="\(c\) Koobi ([\d\.]+)", "http:\/\/www.dream4.de" \/>/" },
			{ "version" : "/Powered by <a title="Koobi ist ein komfortables und leistungsf&auml;higes Content-Management-System \(CMS\) f&uuml;r Privatpersonen", "Vereine", "kleine und mittelst&auml;ndische Unternehmen", "die einen professionellen Internetauftritt realisieren m&ouml;chten."[^>]*>Koobi[\ :]*(SHOP|PRO|CMS)<\/a> ([\d\.]+)/i", "offset" : "1 },
			{ "version" : "/Powered by <a[^>]+href="http:\/\/www.dream4.de\/cms\/content\/6\/koobi\/1\/">Koobi<\/a> (PRO|SHOP|CMS)[\s]*([\d\.\ a-z]+)/i", "offset" : "1 },
			{ "version" : "/powered by <a[^>]+href="http:\/\/www.dream4.de\/[^>]+>koobi-cms<\/a> ([\d\.]+)/i },
			{ "version" : "/<div class="copyright">powered by Koobi CMS ([\d\.]+)/" },
			{ "version" : "/    Diese Webseite wurde mit Koobi[\ :]*(SHOP|PRO|CMS)[\ \-]*([\d\.\ a-z]+) erstellt./", "offset" : "1 },
			{ "version" : "/powered by <a class="foot" href="http:\/\/www.antichat.ru" target="_blank">Koobi Pro ([\d\.]+) \[nulled by censored! from antichat.ru\]<\/a>/", "string" : "Nulled" },
		]
		return(self.rules)
