#!/usr/local/bin/python
#Filename: importdb.py
from BioSQL import BioSeqDatabase
server = BioSeqDatabase.open_database(driver = "MySQLdb",user = "chapmanb",passwd = "biopython", host = "localhost", db = "testbiodb")
db = server.new_database("test")
from Bio import GenBank
parser = GenBank.FeatureParser()
iterator = GenBank.Iterator(open("/Volumes/MACDATA/wubin/Workspace/Project/Blast_database/data/ls_orchid.gbk"),parser)
db.load(iterator)
server.adaptor.commit()
