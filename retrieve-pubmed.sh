mkdir -p pubmed


IFS=$'\n'
#for l in `cat pmid_exact_hs.txt`
#for l in `cat gse_plat_pubmed.txt`
for l in `cat gse_pubmed.txt`
do 
    gse=`echo $l | cut -f1`
    pmids=`echo $l | cut -f2`
    if [ ! -f pubmed/$gse ]
    then
	    wget -O pubmed/$gse "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=text&rettype=medline&id=$pmids"
        #sleep 1s
    fi
done
unset IFS
