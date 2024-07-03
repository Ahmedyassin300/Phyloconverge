import unittest
from phylo_converge.alignment import read_sequences, align_sequences
from phylo_converge.phylogeny import construct_phylogenetic_tree
from phylo_converge.visualization import draw_phylogenetic_tree

class TestVisualization(unittest.TestCase):
    def test_draw_phylogentic_tree(self):
        sequences = read_sequences("test_sequences.fasta")
        alignment = align_sequences(sequences)
        tree = construct_phylogenetic_tree(alignment)
        try:
            draw_phylogenetic_tree(tree)
        except Exception as e:
            self.fail(f"draw_phylogentic_tree raised an exception: {e}")

if __name__=='__main__':
    unittest.main()