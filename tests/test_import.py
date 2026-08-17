def test_import():
    import plottool_ibeis as pt

    # Keep the graph-layout API used by IBEIS importable from the package root.
    assert callable(pt.get_nx_layout)
    assert callable(pt.nx_agraph_layout)

    # Keep legacy package-root helpers that static imports previously exposed.
    assert pt.qtensure is pt.plot_helpers.qtensure
    assert pt.quit_if_noshow is pt.draw_func2.quit_if_noshow
