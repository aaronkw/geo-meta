ftp=`echo ftp://ftp.ncbi.nlm.nih.gov/geo/series`

for i in `cat datasets.txt`
do
    
    n=${#i}
    file=`echo ${i}_family.xml.tgz`
    file_xml=`echo ${i}_family.xml`
    if [ ! -f geo_xml/$file_xml ]
    then
	    dir=`echo ${i:0:($n-3)}nnn`
	    url=`echo $ftp/$dir/$i/miniml/`

	    wget $url -nd -nH -r -A '*.tgz' -P geo_xml/

	    ls geo_xml/*.tgz | xargs -n1 tar -xvz -C geo_xml/ --exclude='*.txt' -f 
	    rm -f geo_xml/*.tgz geo_xml/index.html*
    fi
done
