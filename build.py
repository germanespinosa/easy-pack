from src import EasyPackModule

#EasyPackModule.scaffold("test")

easy_pack = EasyPackModule.read(".")

easy_pack.create_setup_files("../setup")

print(easy_pack.build_module("python-build"))

# save the increased build number
easy_pack.save(".")


