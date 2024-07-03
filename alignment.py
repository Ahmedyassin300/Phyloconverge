from Bio import SeqIO, AlignIO
from Bio.Align.Application import ClustalwCommandline
from Bio.Align import MultipleSeqAlignment

def read_sequences(file_paht):
    sequences = list(SeqIO.parse(file_paht, "fasta"))
    return sequences

def align_sequences(sequences, algner_path="clustalw2"):
    SeqIO.write(sequences, "temp_sequences.faste", "fasta")
    clustalw_cline = ClustalwCommandline(algner_path, infile="temp_sequences.fasta")
    clustalw_cline()
    alignment = MultipleSeqAlignment(AlignIO.parse("temp_sequences.aln", "clustal"))
    return alignment