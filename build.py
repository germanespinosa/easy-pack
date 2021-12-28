#!/bin/python3
from src import EasyPackModule
easy_pack = EasyPackModule.read(".")
easy_pack.create_setup_files("../setup")
print(easy_pack.build_module("python-build"))

# save the increased build number
easy_pack.save(".")


