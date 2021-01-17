import pyinputplus as pyip
import pyfiglet

from SymmetricEncryption import SymmetricEncryption
from AsymmetricEncryption import AsymmetricEncryption
from Encoding import Encoding
from Hashing import Hashing


def menu():
    while(True):
        choice = pyip.inputMenu(['encoding','hashing','pwdCracker','symmetric-encrypt','asymmetric-encrypt','quit'])
        if(choice=='encoding'):
            Encoding.menu()
        elif(choice=='hashing'):
            Hashing.hash_menu()
        elif(choice=='pwdCracker'):
            Hashing.crack_menu()
        elif(choice=='symmetric-encrypt'):
            SymmetricEncryption.menu()
        elif(choice=='asymmetric-encrypt'):
            AsymmetricEncryption.menu()
        
        elif(choice=='quit'):
            return



menu()