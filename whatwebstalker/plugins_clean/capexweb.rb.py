{ "text" : '<frame name="main" src="capexmain_middle.htm" scrolling="no" target="_top">' }
{ "version" : "/<title>cApexWEB ([^\s^<]+)<\/title>/ }
{ "text" : '<!-- Change Company & Address Line ", "Enter First Line for Company Name and 2nd Line of Address --->' }
{ "string" : /<input type="hidden" value="([^\s^"^>]+)"  name="dfcode">/ }
{ "string" : /<input type="hidden" name="dfparentdb" value="([^\s^"^>]+)">/ }
{ "string" : /<input type="hidden" name="dfparentip" value="([^\s^"^>]+)">/ }
{ "text" : '<td><form method="post" name="parentpage" action="../servlet/capexweb.parentvalidatepassword">' }
{ "text" : '<form method="post" action="../servlet/capexweb.parentvalidatepassword">' }
{ "text" : 'var winPop = window.open("../servlet/capexweb.parentvalidatepassword?dfuserid="+dfuserid.value+"&dfpassword="+dfpassword.value+"&dfparentip="+dfparentip.value+"&dfparentdb="+dfparentdb.value+"&dfcode="+dfcode.value+","mywin","width=550,height=550,toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=yes,resizable=yes,fullscreen=yes");' }
