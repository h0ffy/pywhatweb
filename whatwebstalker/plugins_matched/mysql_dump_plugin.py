import sys
import os
			
class mysql_dump_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/------------------------------------------------------[\r]?\n-- Server version[\s]+([^\r^\n]+)/ }
			{ "version" : '/^# phpMyAdmin MySQL-Dump[\s]+# version [^\s]+[\s]+# http:\/\/www.phpmyadmin.net\/ \(download page\)[\s#]+# Host: [^\s]+[\s]+# Generation Time: [^\n]+[\s]+# Server version: ([\d\.]+)/ }
			{ "string" : /^-- MySQL dump [\d\.]+[\r]?\n--[\r]?\n-- Host: ([^\s]+)[\s]+Database:[\s]+([^\r^\n]+)/ }
			{ "string" : /^-- MySQL dump [\d\.]+[\r]?\n--[\r]?\n-- Host: ([^\s]+)[\s]+Database:[\s]+([^\r^\n]+)/", "offset" : '1 }
			{ "string" : /^# phpMyAdmin MySQL-Dump[\s]+# version [^\s]+[\s]+# http:\/\/www.phpmyadmin.net\/ \(download page\)[\s#]+# Host: ([^\s]+)[\s]+# Generation Time: [^\#]+# Server version:[^\#]+# PHP Version:[^\#]+# Database : `([^\`]+)`/ }
			{ "string" : /^# phpMyAdmin MySQL-Dump[\s]+# version [^\s]+[\s]+# http:\/\/www.phpmyadmin.net\/ \(download page\)[\s#]+# Host: ([^\s]+)[\s]+# Generation Time: [^\#]+# Server version:[^\#]+# PHP Version:[^\#]+# Database : `([^\`]+)`/", "offset" : '1 }
	]
