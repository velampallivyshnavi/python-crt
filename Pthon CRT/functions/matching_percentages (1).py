'''
match percentage
calculate % match for each subject (based on character-wise comparison)
display results in the format:
ID: geneA | Match: 80% | Status: Good match
Match % >=80 -> "Good match"
50 <=% < 80 -> "Moderate match"
% < 50 -> "Poor match"
'''
db = {
    #key : value
  "ATGT": "geneA",
  "ATGC": "geneB",
  "TTAC": "geneC",
  "ATGG": "geneD",
}
#ID: geneA | Match: 80% | Status: Good match
def generate_report(dna,db):
    Count_C=0
    Count_G=0
    if dna in db:
        ID=db[dna]
    for i in dna:
        Count_G=dna.count(i)
        Count_C=dna.count(i)
    GC_Count=(Count_G + Count_C)/len(dna)*100
    if(GC_Count>=80):
        Status="Good Match"
    elif(GC_Count>=50 and GC_Count<80):
        Status="Moderate"
    else:
        Status="Poor Match"
    #ID: geneA | Match: 80% | Status: Good match
    print(f"ID:{ID}| Match:{GC_Count}%| Status:{Status}")
Sequence="ATGT"
generate_report(Sequence,db)