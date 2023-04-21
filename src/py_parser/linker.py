from collections import UserDict

from src.py_parser.tree import Folder, Module


class Linker(UserDict[str, dict]):
    """ Consists links between modules in the project:
        Imports, classes and functions
    """
    root: Folder

    def __init__(self, root, *args, **kwargs):
        super(Linker, self).__init__(*args, **kwargs)

        self.root = root
        self.libraries = set()

    def __repr__(self):
        return f'<Project {self.root}>'

    def get_module_by_import(self, abs_import) -> Module:
        return self[abs_import]['module']

    def gather_modules(self, folder: Folder = None):
        """ Extract all the modules into self dict object """
        folder = folder or self.root

        for module in folder.modules:
            self[module.abs_import] = {
                'module': module,
                'imports': []
            }

        for sub_folder in folder.sub_folders:
            self.gather_modules(sub_folder)

    def build_import_tree(self):
        for module_data in self.values():
            module = module_data['module']  # type: Module
            for import_ in module.imports:
                abs_import = import_.import_from

                try:
                    imported_module = self.get_module_by_import(abs_import)
                except KeyError:
                    # todo: check 'src.code_objs.line' module (bug)
                    self.libraries.add(abs_import)
                    self[module.abs_import]['imports'].append(import_)
                else:
                    self[module.abs_import]['imports'].append(imported_module)