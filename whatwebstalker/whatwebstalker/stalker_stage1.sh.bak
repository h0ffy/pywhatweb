#!/bin/bash


if [ ! -d "plugins_matched" ]; then
	mkdir plugins_matched
fi


cd plugins_original
for i in `ls`; do sed -n "/^matches \[/,/\]$/p" $i | tee ../plugins_matched/$i; done
cd -


if [ ! -d "plugins_clean" ]; then
	mkdir plugins_clean
fi


cd plugins_matched
#for i in `ls`; do cat $i | sed -n "/^{/p" | sed 's/{:/{ :/g' | sed 's/:url\=>/\"url\" : /g' | sed "s/:regexp=>/\"regexp\" : \"/g" | sed "s/:version=>/\"version\" : \"/g" | sed 's/:string=>/\"string\" : /g' | sed 's/:text=>/\"text\" : /g' | sed 's/:name=>/\"name\" : /g' | sed 's/:search=>/\"search\" : /g' | sed 's/:module=>/\"module\" : /g' | sed 's/:md5=>/"md5" : /g' | sed 's/:certainty=>/"certainty" : "/g'  | sed "s/: '\"/: \"/g" | sed 's/, /", "/g' | sed 's/""/"/g' | sed 's/, " "/, "/g' | tee ../plugins_clean/$i; done

for i in `ls`; 
do 
	PRE_CLASS=$(echo $i | sed 's/-/_/g' | sed 's/\.rb/_plugin/')
	#PRE_CODE=$(cat ../precode.txt | sed 's/CLASS_NAME/'${PRE_CLASS}'/' | tee )
	END_FILE=$(echo $i | sed 's/-/_/g' | sed 's/\.rb/\_plugin.py/')
	PRE_CODE=$(cat ../precode.txt | sed 's/CLASS_NAME/Plugin'$PRE_CLASS'/' | tee $END_FILE)
	
	echo $END_FILE

	cat $i | sed -n "/^{/p" | sed 's/{:/{ :/g' | sed 's/:url\=>/\"url\" : /g' | sed 's/:url => /\"url\" : /g' | sed "s/:regexp=>/\"regexp\" : \"/g" | sed 's/regex=>/\"regex\" : \"/g' | sed 's/regxp=>/\"regxp\" : \"/g' | sed "s/:version=>/\"version\" : \"/g" | sed 's/:version => /\"version\" : \"/g' | sed 's/:version =>/\"version\" : \"/g' | sed 's/:string=>/\"string\" : /g' | sed 's/:string => /\"string\" : /g' | sed 's/:string =>/\"string\" : /g' | sed 's/:string  =>/\"string\" : /g'| sed 's/:firmware=>/\"firmware\" : \"/g' | sed 's/:text=>/\"text\" : /g' | sed 's/:text => /\"text\" : /g' | sed 's/:name=>/\"name\" : /g' | sed 's/:name => /\"name\" : /g' | sed 's/:path=>/\"path\" : /g' | sed 's/:filepath=>/\"filepath\" : \"/g' | sed 's/:search=>/\"search\" : /g' | sed 's/:search => /\"search\" : /g' | sed 's/:regexp => /\"regexp\" : \"/g' | sed 's/:status=>/\"status\" : \"/g' | sed 's/:status => /\"status\" : \"/g' | sed 's/:offset=>/\"offset\" : \"/g' | sed 's/:offset => /\"offset\" : \"/g' | sed 's/:os=>/\"os\" : \"/g' | sed 's/:account=>/\"account\" : \"/g' | sed 's/:account => /\"account\" : \"/g' | sed 's/:account =>/\"account\" : \"/g' | sed 's/:ghdb=>/\"ghdb\" : /g' | sed 's/:tagpattern=>/\"tagpattern\" : /g' |sed 's/:module=>/\"module\" : /g' | sed 's/module => /\"module\" : /g' | sed 's/:model=>/\"model\" : \"/g' | sed 's/:model => /\"model\" : \"/g' | sed 's/:model =>/\"model\" : \"/g' | sed 's/:model   =>/\"model\" : \"/g' | sed 's/:md5 => /\"md5\" : /g' | sed 's/:md5=>/"md5" : /g' | sed 's/:certainty=>/"certainty" : "/g' | sed 's/:certainty => /\"certainty\" : \"/g' | sed "s/: '\"/: \"/g" | sed 's/, /", "/g' | sed 's/""/"/g' | sed 's/, " "/, "/g' | sed 's/\/}/}/g' | sed 's/,$//' | sed "s/'\",/\",/g" | grep "^{" | grep "}$" | grep -v ":method=>:get" | sed 's/^{/\t\t\t{/' | sed 's/}$/},/' | sed "s/: '/: \"/g" | sed "s/' }/\" }/" | sed 's/\/ }/\/" }/' | tee -a $END_FILE
	 

	printf "\t\t]\r\n\treturn(self.rules)\r\n" | tee -a $END_FILE
done

rm -rf *.rb
#rm -rf plugins_matched


