''' 
generate_report -function name 
calculates %match for each subject(based on character-wise comparison)
Display results in format:
ID: geneA | Match: 80% | Status: Good match
Match%>= 80 -> "Good Match"
50 <= % <80 -> "Moderate Match"
% <50 -> "Poor match"
'''
db = {
  "ATGT": "geneA",  # 3/4 = 75%
  "ATGC": "geneB",  # 4/4 = 100%
  "TTAC": "geneC",  # 1/4 = 25%
  "ATGG": "geneD",  # 3/4 = 75%
  "ATCC": "geneE",  # 3/4 = 75%
  "AGGC": "geneF",  # 2/4 = 50%
  "GTGC": "geneG",  # 3/4 = 75%
  "TTGC": "geneH",  # 3/4 = 75%
  "GGGG": "geneI",  # 0/4 = 0%
  "ATGA": "geneJ"  # 3/4 = 75%
}
def generate_report(dna,db):
    Count_G=0
    Count_C=0
    if dna in db:
        ID=db[dna]
    for i in dna:
        Count_G=dna.count(i)
        Count_C=dna.count(i)
    GC_Count=(Count_G+Count_C)/len(dna)*100
    if(GC_Count>=80):
        Status="Good Match"
    elif(GC_Count>=50 and GC_Count<80):
        Status="Poor Match"
    #ID: geneA | Match: 80% | Status: Good match
    print(f"ID:{ID}| Match:{GC_Count}%| Status:{Status}")
Sequence="ATGT"
generate_report(Sequence,db)