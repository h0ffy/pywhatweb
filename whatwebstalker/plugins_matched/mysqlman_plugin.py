import sys
import os
			
class mysqlman_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "| <A href="mysql.cgi?do=top_level_op&data_source=&action=create_db">Create</A>" },
			{ "version" : "/<p align="right"><a href="http:\/\/www\.gossamer-threads\.com\/scripts\/"><font face="Verdana", "Arial", "Helvetica" size="1">MySQLMan[\s]+v\. ([^\s^<]+)<br>/" },
		]

