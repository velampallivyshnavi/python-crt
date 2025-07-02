'''
Your task is to simulate a basic BLAST-like match using substring matching logic.
-Write a function find_matches(query: str, db: dict) -> list that:
-Takes a query DNA string and a dictionary of sequence IDs and sequences.
-Returns a list of sequence IDs where the query is found as a substring
'''
def find_matches(query:str,db,list):
    match=[seq_id for seq_id,seq in db.items() if query in seq]
    return match
db = {
  "seq001": "ATGCGGAATT",
  "seq002": "CGTACGTAGC",
  "seq003": "TTATGCATTA",
  "seq004": "GGAATCCGTA",
  "seq005": "CATGCCGTAGC",
  "seq006": "GGGCGTGCAT",
  "seq007": "AATGCTAGCTA",
  "seq008": "CGCGATGCGC",
  "seq009": "TATATATATA",
  "seq010": "ATGCGGATGCA"
}
query="ATGC"
match_seq=find_matches(query,db,list)
print(match_seq)