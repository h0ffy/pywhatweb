import sys
import os
			
class Plugincafeengine_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "  <td id="footer">Copyright &copy; <a href="http://cafeengine.com">CafeEngine</a> 2008-2009</td>" },
			{ "text" : "  <td id="footer">Copyright &copy; CafeEngine</a> 2008-2009</td>" },
			{ "text" : "  <td id=footer>Copyright &copy; <a href=http://cafeengine.com>CafeEngine.com</a> 2008-2009</td>" },
			{ "text" : "  win = window.open(src,","top=20,left=20,height=" + h + ",width=" + w + ",toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=no,resizable=yes")" },
		]

