import plugins
			
class Plugincultbooking_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "ghdb" : "inurl:cultbooking.php filetype:php" },
			{ "text" : "<tr><td width="3%" align="center"><img src="img/default/small/pfeil_vor.gif" id="up2"/></td><td width="32%"> <p>Enter the promotioncode (if any)</p></td><td><input size="10" maxlength="20" name="promotionCode" align="right" value=" >" },
			{ "text" : "<tr><td width="3%" align="center"><img src="img/default/small/pfeil_vor.gif" id="up2"/></td><td width="45%"> <p>Enter the promotion code (if any)</p></td><td><input size="10" maxlength="20" name="promotionCode" align="right">" },
			{ "text" : "<tr><td width="3%" align="center"><img src="img/default/small/pfeil_vor.gif" id="up2"/></td><td width="45%"> <p>Promotioncode eingeben (falls vorhanden)</p></td><td><input size="10" maxlength="20" name="promotionCode" align="right">" },
			{ "text" : "<span class="font" onclick="small();"> <img src="img/default/small.gif" alt="small font"> </span> <span class="font" onclick="medium();"><img src="img/default/medium.gif" alt="medium font" > </span> <span class="font" onclick="large();"> <img src="img/default/large.gif" alt="large font"></span></td>" },
			{ "text" : "<span class="font" onclick="small();"> <img src="img/default/small.gif" alt="small font"> </span> <span class="font" onclick="medium();"><img src="img/default/medium.gif" alt="medium font" > </span> <span class="font" onclick="large();"> <img src="img/default/large.gif" alt="large font"></span></td>" },
		]
		return(self.rules)

