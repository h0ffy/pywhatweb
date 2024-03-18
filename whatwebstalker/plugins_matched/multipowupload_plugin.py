import sys
import os
			
class multipowupload_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'Upload result:<br><pre>No files sent. Script is OK!Here is some more debugging info:Array' },
			{ "version" : '/		<title>Element-It MultiPowUpload ([\d\.]+) Examples<\/title>/ },
			{ "version" : '/		<h2>Element-<font color="#de0000">It<\/font> MultiPowUpload ([\d\.]+) Examples<\/h2>/ },
			{ "text" : '		Visit <a href="http://www.element-it.com/MultiPowUpload.aspx">MultiPowUpload</a> web site for new release and support information.' },
			{ "text" : '		Visit <a href="http://www.element-it.com/multiple-file-upload/flash-uploader.aspx">MultiPowUpload</a> web site for new release and support information.' },
			{ "text" : '<PARAM NAME="FlashVars" VALUE="uploadUrl=FileProcessingScripts/PHP/uploadfiles.php' },
			{ "text" : '<embed bgcolor=[^>]+src="ElementITMultiPowUpload.swf" quality="high" pluginspage="http://www.macromedia.com/shockwave/download/index.cgi?P1_Prod_Version=ShockwaveFlash"' },
			{ "version" : '/<embed bgcolor=[^>]+src="ElementITMultiPowUpload([\d\.]{1,5}).swf" quality="high" pluginspage="http:\/\/www.macromedia.com\/shockwave\/download\/index.cgi\?P1_Prod_Version=ShockwaveFlash"/ },
		]

