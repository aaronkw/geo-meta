mkdir -p geo_xml
mkdir -p pubmed 

# download meta data for GSEs in datasets.txt
bash wget-geo.sh

# extract pubmed ids
python utils/geo_extract_pubmed.py -d geo_xml -o gse_pubmed.txt

# retrieve pubmed medline entries
bash retrieve-pubmed.sh

# make gse to mesh mapping 
python utils/medline_extract_mesh.py -d pubmed -o gse_mesh.txt
