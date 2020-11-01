import openpifpaf

from . import datamodule

def register():
    print("Registering Nightowls plugin...")
    openpifpaf.DATAMODULES['nightowls'] = datamodule.Nightowls
