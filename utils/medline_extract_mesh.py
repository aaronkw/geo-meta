import sys
import os
import math
from optparse import OptionParser
from collections import defaultdict

usage = "usage: %prog [options]"
parser = OptionParser(usage, version = "%prog dev-unreleased")
parser.add_option("-d", "--medline-dir", dest="dir", help="medline directory", metavar="FILE")
parser.add_option("-o", "--output-file", dest="ofile", help="output file", metavar="FILE")

(options, args) = parser.parse_args()

files = os.listdir(options.dir)

dset_terms = defaultdict(set)

for f in files:
    for l in open(options.dir+'/'+f):
        if l.startswith('MH '):
            term = l.strip().split(' - ')[1]
            term = term.split('/')[0].replace('*','')
            dset_terms[f].add(term)

ofile = open(options.ofile, 'w')
for dset,terms in dset_terms.iteritems():
    ofile.write( dset + '\t' + '|'.join(list(terms)) + '\n' )

