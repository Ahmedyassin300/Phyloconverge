import unittest
from phylo_converge.alignment import read_sequences, align_sequences

class TestAlignment(unittest.TestCase):
    def test_read_sequences(self):
        sequences = read_sequences("test_sequences.fasta")
        self.assertGreater(len(sequences), 0)

    def test_align_sequences(self):
        sequences = read_sequences("test_sequences.fasta")
        alignment = align_sequences(sequences)
        self.assertGreater(len(alignment), 0)

if __name__ == '__main__':
    unittest.main()