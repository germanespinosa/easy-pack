class EasyPackModule:

    def __init__(self,
                 major=0,
                 minor=0,
                 build_number=0,
                 name="module_name",
                 package_name="package_name",
                 author="author",
                 author_email="author@email",
                 description="",
                 install_requires="",
                 licence="",
                 url="",
                 licence_file="",
                 readme_file="",
                 files=None,
                 setup_py="",
                 setup_cfg="",
                 folder=""):
        self.major = 0
        self.minor = 0
        self.build_number = build_number
        self.name = name
        self.package_name = package_name
        self.author = author
        self.author_email = author_email
        self.description = description
        if install_requires is None:
            self.install_requires = []
        else:
            self.install_requires = install_requires
        self.licence = licence
        self.url = url
        self.licence_file = licence_file
        self.readme_file = readme_file
        if files is None:
            self.files = []
        else:
            self.files = files
        self.setup_py = setup_py
        self.setup_cfg = setup_cfg
        self.root_folder = folder

    def version_string(self):
        return str(self.major) + "." + str(self.minor) + "." + str(self.build_number)

    def module_file(self):
        return self.name + "-" + self.version_string()

    def get_module_info_file(self):
        module_info_script = ""
        module_info_script += "def __module_version__():\n"
        module_info_script += "\treturn " + str(self.major) + ", " + str(self.minor) + ", " + str(self.build_number) + " \n\n\n"
        module_info_script += "def __module_name__():\n"
        module_info_script += "\treturn '" + self.name + "' \n\n\n"
        module_info_script += "def __author__():\n"
        module_info_script += "\treturn '" + self.author + "' \n\n\n"
        module_info_script += "def __author_email__():\n"
        module_info_script += "\treturn '" + self.author_email + "' \n\n\n"
        module_info_script += "def __package_description__():\n"
        module_info_script += "\treturn '" + self.description + "' \n\n\n"
        module_info_script += "def __install_requires__():\n"
        module_info_script += "\treturn " + str(self.install_requires) + " \n\n\n"
        module_info_script += "def __url__():\n"
        module_info_script += "\treturn '" + self.url + "' \n\n\n"
        module_info_script += "def __licence__():\n"
        module_info_script += "\treturn '" + self.licence + "' \n\n\n"
        module_info_script += "def __licence_file__():\n"
        module_info_script += "\treturn '" + self.licence_file + "' \n\n\n"
        module_info_script += "def __readme_file__():\n"
        module_info_script += "\treturn '" + self.readme_file + "' \n\n\n"
        module_info_script += "def __package_name__():\n"
        module_info_script += "\treturn '" + self.package_name + "' \n\n\n"
        module_info_script += "def __files__():\n"
        module_info_script += "\treturn " + str(self.files) + " \n\n\n"
        module_info_script += "def __setup_py__():\n"
        module_info_script += "\treturn '" + self.setup_py + "' \n\n\n"
        module_info_script += "def __setup_cfg__():\n"
        module_info_script += "\treturn '" + self.setup_cfg + "' \n\n\n"
        module_info_script += "def __root_folder__():\n"
        module_info_script += "\treturn '" + self.root_folder + "' \n\n\n"
        module_info_script += "def __description__():\n"
        module_info_script += "\treturn '" + self.description + "' \n\n\n"
        return module_info_script

    def save(self, folder=None):
        if folder is None:
            folder = self.root_folder
        else:
            self.root_folder = folder
        if folder is None:
            return False
        with open(self.root_folder + "/__info__.py", "w") as v:
            v.write(self.get_module_info_file())
        return True

    @staticmethod
    def read(folder):
        import os
        import sys
        if os.path.exists(folder + "/__info__.py"):
            must_remove = False
            if folder not in sys.path:
                sys.path.append(folder)
                must_remove = True
            import __info__ as info
            content = vars(info)
            module_info = EasyPackModule()
            if "__module_version__" in content:
                module_info.major, module_info.minor, module_info.build_number = info.__module_version__()
            if "__module_name__" in content:
                module_info.module_name = info.__module_name__()
            if "__package_name__" in content:
                module_info.package_name = info.__package_name__()
            if "__author__" in content:
                module_info.author = info.__author__()
            if "__description__" in content:
                module_info.description = info.__description__()
            if "__install_requires__" in content:
                module_info.install_requires = info.__install_requires__()
            if "__licence__" in content:
                module_info.licence = info.__licence__()
            if "__author_email__" in content:
                module_info.author_email = info.__author_email__()
            if "__licence_file__" in content:
                module_info.licence_file = info.__licence_file__()
            if "__readme_file__" in content:
                module_info.readme_file = info.__readme_file__()
            if "__setup_py__" in content:
                module_info.setup_py = info.__setup_py__()
            if "__files__" in content:
                module_info.files = info.__files__()
            if "__setup_cfg__" in content:
                module_info.setup_cfg = info.__setup_cfg__()
            if "__root_folder__" in content:
                module_info.root_folder = info.__root_folder__()
            if must_remove:
                sys.path.remove(folder)
            return module_info
        else:
            return None

    def get_setup(self):
        setup_py = "from setuptools import setup\n\n"
        setup_py += "setup(name='" + self.name + "'"
        if self.description:
            setup_py += ",description='" + self.description + "'"
        if self.url:
            setup_py += ",url='" + self.url + "'"
        if self.author:
            setup_py += ",author='" + self.author + "'"
        if self.author_email:
            setup_py += ",author_email='" + self.author_email + "'"
        if self.package_name:
            setup_py += ",packages=['" + self.package_name + "']"
        if self.install_requires:
            setup_py += ",install_requires=" + str(self.install_requires)
        if self.licence:
            setup_py += ",licence='" + self.licence + "'"
        setup_py += ",zip_safe=False)\n"

        setup_cfg = "[metadata]\n"
        setup_cfg += "name = " + self.name + "\n"
        setup_cfg += "version = " + self.version_string() + "\n"
        if self.author:
            setup_cfg += "author = " + self.author + "\n"
        if self.description:
            setup_cfg += "description = " + self.description + "\n"
        if self.readme_file:
            setup_cfg += "description-file = " + self.readme_file.split("/")[-1] + "\n"

        return setup_py, setup_cfg

    def create_setup_files(self, dst=""):
        if dst:
            dst += "/"
        setup_py, setup_cfg = self.get_setup()
        self.setup_py = dst + "setup.py"
        with open(self.root_folder + "/" + self.setup_py, "w") as m:
            m.writelines([setup_py])
        self.setup_cfg = dst + "setup.cfg"
        with open(self.root_folder + "/" + self.setup_cfg, "w") as m:
            m.writelines([setup_cfg])

    def build_module(self, dst):
        import os

        if not os.path.exists(self.root_folder + "/__init__.py"):
            return False

        if not self.setup_py:
            return False

        if not self.setup_cfg:
            return False

        self.build_number += 1
        self.save()

        if not os.path.exists(dst):
            os.mkdir(dst)

        destination = dst + "/" + self.module_file()
        if not os.path.exists(destination):
            os.mkdir(destination)

        from shutil import copy
        copy(self.root_folder + "/" + self.setup_py, destination)

        module_folder = destination + "/" + self.package_name
        os.mkdir(module_folder)

        copy(self.root_folder + "/" + self.setup_cfg, module_folder)

        copy(self.root_folder + "/__init__.py", module_folder)

        for f in self.files:
            copy(self.root_folder + "/" + f, module_folder)

        if self.readme_file:
            copy(self.root_folder + "/" + self.readme_file, module_folder)

        if self.licence_file:
            copy(self.root_folder + "/" + self.licence_file, module_folder)

        import tarfile
        with tarfile.open(destination + ".tar.gz", "w:gz") as tar:
            tar.add(destination, arcname=os.path.basename(destination))
