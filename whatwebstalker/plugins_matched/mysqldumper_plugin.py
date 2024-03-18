import plugins
			
class Pluginmysqldumper_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<select class="SQLCombo" name="tablecombo" onchange="this.form.sqltextarea.value=this.options[this.selectedIndex].value;this.form.execsql.click();">" },
			{ "text" : "align="center">The execution of SQL Statements can manipulate data. TAKE CARE! The Authors don\'t accept any liability for damaged or lost data.</div>" },
			{ "text" : "<a title="Select Database / Datebase functions / Import - Export " href="sql.php?db=&amp;dbid=0&amp;context=3" },
		]
		return(self.rules)

