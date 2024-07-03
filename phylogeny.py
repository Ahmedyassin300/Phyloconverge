from Bio.Phylo.TreeConstruction import DistanceTreeConstructor, DistanceCalculator

def construct_phylogenetic_tree(alignment):
    calculator = DistanceCalculator("identity")
    dm = calculator.get_distance(alignment)
    constructor = DistanceTreeConstructor()
    tree = constructor.nj(dm)
    return tree
