from itertools import takewhile

PROTEIN = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
}


def proteins(strand):
    return [
        PROTEIN.get(protein)
        for protein in takewhile(
            lambda protein: protein not in ("UAA", "UAG", "UGA"),
            [strand[i : i + 3] for i in range(0, len(strand), 3)],
        )
    ]
