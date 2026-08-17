from __future__ import annotations

import ast
from pathlib import Path


ROOT = Path(__file__).parents[1]
PACKAGE = ROOT / 'plottool_ibeis'


def _tree(path):
    return ast.parse(path.read_text(), filename=str(path))


def _active_noinject_sites():
    sites = []
    for path in PACKAGE.rglob('*.py'):
        tree = _tree(path)
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == 'noinject'
            ):
                sites.append(str(path.relative_to(ROOT)))
    return sorted(sites)


def _imports_utool(path):
    for node in ast.walk(_tree(path)):
        if isinstance(node, ast.Import):
            if any(alias.name == 'utool' for alias in node.names):
                return True
        if isinstance(node, ast.ImportFrom) and node.module:
            if node.module == 'utool' or node.module.startswith('utool.'):
                return True
    return False


def test_obsolete_noinject_bookkeeping_is_retired():
    assert _active_noinject_sites() == []


def test_simple_render_modules_are_utool_free():
    relpaths = [
        'plottool_ibeis/draw_sv.py',
        'plottool_ibeis/mpl_sift.py',
        'plottool_ibeis/other.py',
        'plottool_ibeis/viz_image2.py',
    ]
    assert not [rel for rel in relpaths if _imports_utool(ROOT / rel)]


def test_runtime_requires_migrated_guitool():
    runtime_text = (ROOT / 'requirements/runtime.txt').read_text()
    assert 'guitool_ibeis >= 2.3.0' in runtime_text


def test_enabled_ci_lockfiles_exist():
    workflow_lines = (ROOT / '.github/workflows/tests.yml').read_text().splitlines()
    for index, line in enumerate(workflow_lines):
        if line.strip() == "use-lockfile: 'true'":
            nearby = workflow_lines[index + 1:index + 6]
            lock_lines = [
                item for item in nearby
                if item.strip().startswith('lock-requirements:')
            ]
            assert lock_lines, 'enabled lock row has no lock-requirements path'
            lock_relpath = lock_lines[0].split(':', 1)[1].strip()
            assert (ROOT / lock_relpath).is_file(), lock_relpath


def test_ci_quotes_setuptools_version_specifiers():
    workflow_text = (ROOT / '.github/workflows/tests.yml').read_text()
    unquoted = workflow_text.replace('"setuptools>=0.8"', '')
    assert 'setuptools>=0.8' not in unquoted
