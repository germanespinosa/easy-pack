from src import EasyPackModule

easy_pack = EasyPackModule.read(".")

easy_pack.save()

print(easy_pack.build_module("python-build"))


