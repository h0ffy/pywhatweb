import plugins


class Plugincisco_ip_phone_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"model": "/<td HEIGHT="50" bgcolor="  # 003031"><p ALIGN=center><B><font color="#FFFFFF" size="6">[^<]{5,50}<\/FONT><\/B><p ALIGN=center><B><font color="#FFFFFF" size="4">Cisco[^\(]{0,15} IP Phone ([^\(]{4,20}) \( [^\)]{15} \)[\s]?<\/FONT><\/FONT><\/B><\/TD>/" },
			{"string": / <td HEIGHT = "50" bgcolor = "#003031" > <p ALIGN = center > <B > <font color = "#FFFFFF" size = "6" > [ ^ <]{5, 50} <\/FONT><\/B><p ALIGN=center><B><font color="#FFFFFF" size="4">Cisco[^\(]{0,15} IP Phone [^\(]{4,20} \( ([^\)]{15}) \)[\s]?<\/FONT><\/FONT><\/B><\/TD>/" },
			{ "model" : "/<td HEIGHT="50" bgcolor="#003031"><p ALIGN=center><B><font color="#FFFFFF" size="6">[^<]{5,50}<\/FONT><\/B><p ALIGN=center><B><font color="#FFFFFF" size="4">Cisco Unified IP Phone ([^\(]{4,20}) \( [^\)]{15} \)[\s]?<\/FONT><\/FONT><\/B><\/TD>/", "version" : "Unified" },
			{ "string" : /<td HEIGHT="50" bgcolor="#003031"><p ALIGN=center><B><font color="#FFFFFF" size="6">[^<]{5,50}<\/FONT><\/B><p ALIGN=center><B><font color="#FFFFFF" size="4">Cisco Unified IP Phone [^\(]{4,20} \( ([^\)]{15}) \)[\s]?<\/FONT><\/FONT><\/B><\/TD>/", "version" : "Unified" },
			{ "model" : "/<title>Cisco Unified Wireless IP Phone ([^<]{4,20})<\/title><link href="\/style.css" type=text\/css rel=stylesheet><\/head>/", "version" : "Unified Wireless" },
			{ "model" : "/<p align=center style='text-align:center'><b><span style='font-size:13.5pt; color:white'>Cisco Unified Wireless IP Phone ([^\(]{4,20}) \( [^\)]{15} \)<\/span><\/b><\/p>/", "version" : "Unified Wireless" },
			{ "string" : /<p align=center style='text-align:center'><b><span style='font-size:13.5pt; color:white'>Cisco Unified Wireless IP Phone [^\(]{4,20} \( ([^\)]{15}) \)<\/span><\/b><\/p>/", "version" : "Unified Wireless" },
		]
	return(self.rules)
