import logging
logger = logging.getLogger(__name__)

import sys
import os
import xml.etree.ElementTree as ET
from optparse import OptionParser

usage = "usage: %prog [options]"
parser = OptionParser(usage, version="%prog dev-unreleased")

parser.add_option("-d", "--geo_xml_dir", dest="geo_xml_dir", help="Directory of GEO xml files", metavar="FILE")
parser.add_option("-o", "--output-file", dest="output", help="Output file", metavar="FILE")

(options, args) = parser.parse_args()

NAMESPACE = '{http://www.ncbi.nlm.nih.gov/geo/info/MINiML}'

ofile = open(options.output, 'w')

for geof in os.listdir(options.geo_xml_dir):
    xml = (options.geo_xml_dir + '/' + geof)
    if not xml.endswith('.xml'):
        continue

    try:
        meta = ET.parse(xml)
    except ET.ParseError:
        print >> sys.stderr, "Error parsing", xml 
        continue

    root = meta.getroot()
    s = root.find(NAMESPACE+'Series')

    plat_xml = root.findall(NAMESPACE+'Platform')
    gpls = []
    for plt in plat_xml:
        gpls.append(plt.get('iid'))

    pmids_xml = s.findall(NAMESPACE+'Pubmed-ID')
    pmids = []
    for pmid in pmids_xml:
        pmids.append(pmid.text)

    if len(pmids) > 0:
        for gpl in gpls:
            ofile.write( s.get('iid') + '.' + gpl + '\t' + ','.join(pmids) + '\n' )

ofile.close()
