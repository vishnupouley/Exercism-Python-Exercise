def to_rna(dna_strand: str) -> str:
    return ''.join('C' if dna == 'G' else 'G' if dna == 'C' else 'A' if dna == 'T' else 'U' for dna in list(dna_strand)) if dna_strand else ""
