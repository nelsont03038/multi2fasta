############################################################################
# multi2fasta.py
# written by Thomas Nelson, October 2, 2014 
# thomas dot c dot nelson at gmail dot com
# This script requires the Biopython module and nothing else
# Get the Biopython module here here: http://biopython.org/wiki/Download
# This script will extract individual sequences from a multi fasta file
#     and write each sequence to its own file named the sequence id
############################################################################

import sys
from Bio import SeqIO

#usage statement
if len(sys.argv) < 2:
      print "Usage: python multi2fasta.py [ MULTIFASTA file name ]"
      sys.exit()

for sequence in SeqIO.parse(sys.argv[1], "fasta"):
    fileName = str(sequence.id) + ".fa"
    myFile = open(fileName, 'w')    
    myFile.write(">" + sequence.id + "\n")
    myFile.write(str(sequence.seq))
    myFile.close()

