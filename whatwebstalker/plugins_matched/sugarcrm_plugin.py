import sys
import os
			
class sugarcrm_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<h3 style='color:red'>Possible Cross Site Request Forgery (XSRF) Attack Detected</h3>" },
			{ "text" : '<span>|</span>    <a href=" javascript:void window.open(\'http://support.sugarcrm.com\')">Support</a>' },
			{ "text" : '<script>var module_sugar_grp1 = 'Users';</script><script>var action_sugar_grp1 = 'Login';</script><script>jscal_today" },
			{ "module" : /<script type="text\/javascript">[\s]+<!--[\s]+SUGAR\.themes\.theme_name      = '([^']+)';[\s]+SUGAR\.themes\.theme_ie6compat = / },
			{ "text" : '<img style='margin-top: 2px' border='0' width='106' height='23' src='include/images/poweredby_sugarcrm.png' alt='Powered By SugarCRM'>" },
			{ "string" : /\* SugarCRM is a customer relationship management program developed by[\s]+ \* SugarCRM", "Inc\. Copyright \(C\) 2004-([\d]{4}) SugarCRM Inc\./ },
		]

