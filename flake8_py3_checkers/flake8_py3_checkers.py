# -*- coding: utf-8 -*-
import ast
from ast import iter_child_nodes

__version__ = '0.0.1'


class UnicodeFunctionCallChecker(object):
    name = 'uccu'
    version = __version__

    def __init__(self, tree, filename):
        self._node = tree
        self.filename = filename

    def run(self):
        if self._node:
            return self.visit_tree(self._node)
        else:
            return ()

    def visit_tree(self, node):
        for error in self.visit_node(node):
            yield error
        for child in iter_child_nodes(node):
            for error in self.visit_tree(child):
                yield error

    def visit_node(self, node):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id == 'unicode':
                yield (
                    node.lineno,
                    node.col_offset,
                    '[PY3 Compat.] Found unicode function call',
                    type(self),
                )
