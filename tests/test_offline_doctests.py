from __future__ import annotations

import ast
from pathlib import Path


ROOT = Path(__file__).parents[1]
PACKAGE = ROOT / 'plottool_ibeis'
NETWORK_FIXTURE_PATTERNS = (
    'grab_zipped_url(',
    'grab_test_imgpath(',
    'grab_file_url(',
    'ub.grabdata(',
    'requests.get(',
    'urlretrieve(',
)


def _iter_docstrings(tree):
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            doc = ast.get_docstring(node, clean=False)
            if doc is not None:
                yield node, doc


def test_enabled_doctests_are_offline():
    offenders = []
    for path in PACKAGE.rglob('*.py'):
        text = path.read_text()
        tree = ast.parse(text, filename=str(path))
        for node, doc in _iter_docstrings(tree):
            if '# ENABLE_DOCTEST' not in doc:
                continue
            for pattern in NETWORK_FIXTURE_PATTERNS:
                if pattern in doc:
                    offenders.append(
                        (str(path.relative_to(ROOT)), getattr(node, 'name', '<module>'), pattern)
                    )
    assert offenders == []


def test_package_test_helpers_are_offline():
    offenders = []
    for path in PACKAGE.rglob('*.py'):
        text = path.read_text()
        tree = ast.parse(text, filename=str(path))
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if not node.name.startswith('test_'):
                continue
            source = ast.get_source_segment(text, node) or ''
            for pattern in NETWORK_FIXTURE_PATTERNS:
                if pattern in source:
                    offenders.append(
                        (str(path.relative_to(ROOT)), node.name, pattern)
                    )
    assert offenders == []
