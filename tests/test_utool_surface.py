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
