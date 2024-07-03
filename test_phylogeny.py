import unittest
from phylo_converge.alignment import read_sequences, align_sequences
from phylo_converge.phylogeny import construct_phylogenetic_tree

class TestPhylogeny(unittest.TestCase):
    def test_construct_phylogenetic_tree(self):
        sequences = read_sequences("test_sequences.fasta")
        alignment = align_sequences(sequences)
        tree = construct_phylogenetic_tree(alignment)
        self.assertIsNotNone(tree)

if __name__=='__main__':
    unittest.main()


