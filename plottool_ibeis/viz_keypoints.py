import utool
import plottool_ibeis.draw_func2 as df2
import numpy as np
from plottool_ibeis import plot_helpers as ph
utool.noinject(__name__, '[viz_keypoints]')


def testdata_kpts():
    import utool as ut
    import vtool_ibeis as vt
    import pyhesaff
    img_fpath = ut.grab_test_imgpath(ut.get_argval('--fname', default='star.png'))
    kwargs = ut.parse_dict_from_argv(pyhesaff.get_hesaff_default_params())
    (kpts, vecs) = pyhesaff.detect_feats(img_fpath, **kwargs)
    imgBGR = vt.imread(img_fpath)
    return kpts, vecs, imgBGR


def show_keypoints(chip, kpts, fnum=0, pnum=None, **kwargs):
    r"""
    Args:
        chip (ndarray):  annotation image data [uint8_t, ndim=2]
        kpts (ndarray):  keypoints [float32_t, ndim=2]
        fnum (int):  figure number(default = 0)
        pnum (tuple | None | Any):  plot number(default = None)

    Kwargs:
        ddd, title, figtitle, interpolation, cmap, heatmap, data_colorbar,
        darken, update, redraw_image, docla, doclf, projection, sel_fx

    CommandLine:
        python -m plottool_ibeis.viz_keypoints --exec-show_keypoints

    Example:
        >>> # DISABLE_DOCTEST
        >>> from plottool_ibeis.viz_keypoints import *  # NOQA
        >>> import vtool_ibeis as vt
        >>> kpts, vecs, chip = testdata_kpts()
        >>> fnum = 0
        >>> pnum = None
        >>> result = show_keypoints(chip, kpts, fnum, pnum)
        >>> print(result)
        >>> import utool as ut
        >>> ut.show_if_requested()
    """
    #printDBG('[df2.show_kpts] %r' % (kwargs.keys(),))
    fig, ax = df2.imshow(chip, fnum=fnum, pnum=pnum, **kwargs)
    _annotate_kpts(kpts, **kwargs)
    ph.set_plotdat(ax, 'viztype', 'keypoints')
    ph.set_plotdat(ax, 'kpts', kpts)
    if kwargs.get('ddd', False):
        ph.draw()


def _annotate_kpts(kpts_, sel_fx=None, **kwargs):
    r"""
    Args:
        kpts_ (ndarray): keypoints
        sel_fx (None | Any):

    Keywords:
        color:  3/4-tuple, ndarray, or str

    Example:
        >>> from plottool_ibeis.viz_keypoints import _annotate_kpts
        >>> sel_fx = None
        >>> kpts = np.array([[  92.9246,   17.5453,    7.8103,   -3.4594,   10.8566,    0.    ],
        ...                  [  76.8585,   24.7918,   11.4412,   -3.2634,    9.6287,    0.    ],
        ...                  [ 140.6303,   24.9027,   10.4051,  -10.9452, 10.5991,    0.    ],])
        >>> _annotate_kpts(kpts)
        >>> import utool as ut
        >>> ut.show_if_requested()

    """
    if len(kpts_) == 0:
        print('len(kpts_) == 0...')
        return
    #color = kwargs.get('color', 'distinct' if sel_fx is None else df2.ORANGE)
    color = kwargs.get('color', 'scale' if sel_fx is None else df2.ORANGE)
    if isinstance(color, str):
        if color == 'distinct':
            # hack for distinct colors
            color = df2.distinct_colors(len(kpts_))  # , randomize=True)
        elif color == 'scale':
            # hack for distinct colors
            import vtool_ibeis as vt
            #color = df2.scores_to_color(vt.get_scales(kpts_), cmap_='inferno', score_range=(0, 50))
            color = df2.scores_to_color(vt.get_scales(kpts_), cmap_='viridis', score_range=(5, 30), cmap_range=None)
            #df2.distinct_colors(len(kpts_))  # , randomize=True)
    # Keypoint drawing kwargs
    drawkpts_kw = {
        'ell': True,
        'pts': False,
        'ell_alpha': .4,
        'ell_linewidth': 2,
        'ell_color': color,
    }
    drawkpts_kw.update(kwargs)

    # draw all keypoints
    if sel_fx is None:
        df2.draw_kpts2(kpts_, **drawkpts_kw)
    else:
        # dont draw the selected keypoint in this batch
        nonsel_kpts_ = np.vstack((kpts_[0:sel_fx], kpts_[sel_fx + 1:]))
        # Draw selected keypoint
        sel_kpts = kpts_[sel_fx:sel_fx + 1]
        import ubelt as ub
        if ub.iterable(color) and ub.iterable(color[0]):
            # hack for distinct colors
            drawkpts_kw['ell_color'] = color[0:sel_fx] + color[sel_fx + 1:]
        drawkpts_kw
        drawkpts_kw2 = drawkpts_kw.copy()
        drawkpts_kw2.update({
            'ell_color': df2.BLUE,
            'eig':  True,
            'rect': True,
            'ori':  True,
        })
        df2.draw_kpts2(nonsel_kpts_, **drawkpts_kw)
        df2.draw_kpts2(sel_kpts, **drawkpts_kw2)
