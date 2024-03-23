
from rdkit import Chem

def generate_inchikey(smiles_list):
    """
    Generate InChIKey representation for a list of SMILES strings.

    Args:
    - smiles_list (list): List of SMILES strings.

    Returns:
    - inchikey_list (list): List of corresponding InChIKey representations.
    """
    inchikey_list = []
    for smiles in smiles_list:
        mol = Chem.MolFromSmiles(smiles)
        if mol is not None:
            inchikey = Chem.inchi.MolToInchiKey(mol)
            inchikey_list.append(inchikey)
        else:
            inchikey_list.append(None)
    return inchikey_list
