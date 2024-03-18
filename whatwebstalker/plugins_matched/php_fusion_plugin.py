import plugins
			
class Pluginphp_fusion_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "ghdb" : "Powered by PHP-Fusion copyright" +intitle:News" },
			{ "string" : /Powered by <a href='http:\/\/www\.php-fusion\.co\.uk'>PHP-Fusion<\/a> copyright &copy; 2002 - ([\d]{4})/" },
			{ "text" : "<td align='right' class='tbl1 profile_user_level'><!--profile_user_level-->" },
			{ "text" : "<td align='right' class='profile_user_level tbl1'><!--profile_user_level-->" },
			{ "text" : "class='tbl profile_user_avatar'><!--profile_user_avatar--><img src='images/avatars/" },
			{ "text" : "<td align='right' class='tbl1 profile_user_name'><!--profile_user_name-->" },
			{ "text" : "<td align='right' class='profile_user_name tbl1'><!--profile_user_name-->" },
			{ "certainty" : "75", "regexp" : "/<!--counter-->[\d,]+ unique visits</" },
			{ "search" : "headers[set-cookie]", "name" : "fusion_visited Cookie", "regexp" : "/fusion_visited=/" },
		]
	return(self.rules)
