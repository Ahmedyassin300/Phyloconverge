from Bio import Phylo
import matplotlib.pyplot as plt

def draw_phylogenetic_tree(tree):
    Phylo.draw(tree)
    plt.show()