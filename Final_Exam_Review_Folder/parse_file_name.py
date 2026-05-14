import re

def parse_file_name(Al.Fm-3m.GGA-PBE.volumes_energies):

    name_without_ext = filename.split('.')[0]
    
    parts = re.split(r'[_.-]', name_without_ext)
    
    chemical_symbol = parts[0]
    crystal_symmetry = parts[1]
    xc_approximation = parts[2]
    
    return chemical_symbol, crystal_symmetry, xc_approximation
