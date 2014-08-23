#!/opt/local/bin/python
#Filename: importPYdb.py
from BioSQL import BioSeqDatabase
server = BioSeqDatabase.open_database(driver = "MySQLdb",user = "chapmanb",passwd = "biopython", host = "localhost", db = "pygenome")
db = server.new_database("pygenome_db")
from Bio import GenBank
parser = GenBank.FeatureParser()
iterator = GenBank.Iterator(open("/Volumes/MACDATA/wubin/Workspace/Project/Blast_database/data/PY.structure/PY800K.gb"),parser)
db.load(iterator)
server.adaptor.commit()
