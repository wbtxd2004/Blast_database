#!/opt/local/bin/python
#Filename : strict.py
from Bio import SeqIO
for index,record in enumerate(SeqIO.parse(open("/Volumes/MACDATA/wubin/Workspace/Project/Blast_database/data/ls_orchid.gbk"),"genbank")):
    print "index %i,ID=%s,length %i,with %features"\
        %(index,record.id,len(record.seq),len(record.features))
