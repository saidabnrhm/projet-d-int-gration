import pytest
import subprocess

def test_script():
    # Test simple pour vérifier si ton script se lance sans erreur
    result = subprocess.run(['python', 'script_surveillance.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert result.returncode == 0  # Assure-toi que le code de sortie est 0 (sans erreur)
