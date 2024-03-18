			{ "version" : "/qdPM ([^\s]+) &nbsp;is redistributable under the\s+<a class="footer-text"/ }
			{ "string" : /Copyright @ (20[\d]{2}) <a class="footer-text" target="_blank"( title="open source project management software")? href="http:\/\/(www\.qds-team\.com|qdpm\.net\/)">/ }
			{ "search" : "headers[set-cookie]", "regexp" : "/qdpm(_extended)?=[^;]+;/ }
