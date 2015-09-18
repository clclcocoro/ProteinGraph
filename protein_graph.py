#!/usr/bin/env python

"""Construct Protein Graph


Usage:
  protein_graph.py <pdb_file>
  runSVM.py (-h | --help)
  runSVM.py --version

Options:
  -h --help       Show this screen.
  --version       Show version.

"""

import re


class Atom(object):

    def __init__(self, atom_number, atom_type, x, y, z):
        self.atom_number = atom_number
        self.atom_type   = atom_type
        self.x           = x
        self.y           = y
        self.z           = z


class Residue(object):
    
    def __init__(self, amino_acid_type, alternate_location_indicator, chain, residue_number, insertion, occupancy, atoms):
        self.amino_acid_type              = amino_acid_type
        self.alternate_location_indicator = alternate_location_indicator
        self.chain                        = chain
        self.residue_number               = residue_number
        self.insertion                    = insertion
        self.occupancy                    = occupancy
        self.atoms                        = atoms

    def add_atom(self, atom):
        self.atoms.append(atom)


class Protein(object):

    def __init__(self, proteinid, residues):
        self.proteinid = proteinid
        self.residues  = residues

    def add_residue(self, residue):
        self.residues.append(residue)


def parse_pdb_file(pdb_filepath):
    proteinid = os.basename(pdb_filepath)
    protein = Protein(proteinid, [])
    with open(pdb_filepath) as fp:
        prev_residue_number = float('-inf')
        for line in fp:
            if re.match('TER', line):
                protein.add_residue(residue)
                break
            if not re.match('ATOM', line):
                continue
            atom_number     = line[6:10].strip()
            atom_type       = line[12:16].strip()
            alternate_location_indicator = line[16]
            amino_acid_type = line[17:20].strip()
            chain           = line[21]
            residue_number  = int(line[22:25].strip())
            insertion       = line[26]
            x               = float(line[30:38])
            y               = float(line[38:46])
            z               = float(line[46:55])
            occupancy       = float(line[54:61])
            if residue_number != prev_residue_number:
                protein.add_residue(residue)
                residue = Residue(amino_acid_type, alternate_location_indicator, chain, residue_number, insertion, occupancy, [])
            atom = Atom(atom_number, atom_type, x, y, z)
            residue.add_atom(atom)
            prev_residue_number = residue_number
    return protein


def construct_protein_graph(protein):
    return protein_graph

if __name__ == "__main__":

