def to_rna(dna_strand: str) -> str:
    RNA_CHANGE = {"G": "C", "C": "G", "T": "A", "A": "U"}
    return "".join(RNA_CHANGE[dna] for dna in dna_strand) if dna_strand else ""
