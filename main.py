from ctypes import cdll, c_double, byref
import pathlib
import os

this_file_path = pathlib.Path(__file__)
this_file_directory = this_file_path.parent.absolute()

dll_path = this_file_directory / 'refprop.dll'
ref_file_path = os.chdir('/Subdirect1')
so_path = ref_file_path / Subdirect1 / 'libFakeRefProp.so'

# so_path = this_file_directory / Subdirect1 / 'libFakeRefProp.so'


api = cdll.LoadLibrary(str(so_path))
arg_1 = c_double(1.0)
arg_2 = c_double(2.0)
arg_3 = c_double(0.0)
api.MLTH20dll(byref(arg_1), byref(arg_2), byref(arg_3))
print(f"Arg 3 should be 3, it is: {arg_3.value}")
