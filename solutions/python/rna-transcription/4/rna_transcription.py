def to_rna(dna_strand: str) -> str:
    return "".join({"G": "C", "C": "G", "T": "A", "A": "U"}[dna] for dna in dna_strand) if dna_strand else ""
