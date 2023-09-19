# def DNA_strand(dna):
#     DNA_Transfer = ""
#     for i in dna:
#         if i == 'A':
#             DNA_Transfer = DNA_Transfer + 'T'
#         elif i == 'T':
#             DNA_Transfer = DNA_Transfer + 'A'
#         elif i == 'C':
#             DNA_Transfer = DNA_Transfer + 'G'
#         else:
#             DNA_Transfer = DNA_Transfer + 'C'
#     return (DNA_Transfer)
from string import *

def DNA_strand(dna):
   tbl = dna.maketrans('ATCG', 'TAGC')
   return(dna.translate(tbl)) 

print(DNA_strand('ATTGC'))
            