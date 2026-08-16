# flake8: noqa
"""
Wrappers around matplotlib
"""
__version__ = '2.4.0'


# Hopefully this was imported sooner. TODO remove dependency
#from guitool_ibeis import __PYQT__
#import guitool_ibeis.__PYQT__ as __PYQT__
from plottool_ibeis import __MPL_INIT__
__MPL_INIT__.init_matplotlib()

import matplotlib as mpl
#mpl.use('Qt4Agg')

def __getattr__(key):
    # Lazy loading
    if key == 'plt':
        import matplotlib.pyplot as plt
        return plt
    else:
        raise AttributeError(key)

# import matplotlib.pyplot as plt

from plottool_ibeis import plot_helpers as ph
from plottool_ibeis import plot_helpers
from plottool_ibeis import mpl_keypoint
from plottool_ibeis import mpl_keypoint as mpl_kp
from plottool_ibeis import mpl_sift as mpl_sift
from plottool_ibeis import draw_func2
from plottool_ibeis import draw_func2 as df2
from plottool_ibeis import fig_presenter
from plottool_ibeis import custom_constants
from plottool_ibeis import custom_figure
from plottool_ibeis import draw_sv
from plottool_ibeis import viz_featrow
from plottool_ibeis import viz_keypoints
from plottool_ibeis import viz_image2
from plottool_ibeis import plots
from plottool_ibeis import interact_annotations
from plottool_ibeis import interact_keypoints
from plottool_ibeis import interact_multi_image
from plottool_ibeis import interactions
from plottool_ibeis import interact_impaint
from plottool_ibeis import color_funcs
#from plottool_ibeis import abstract_iteraction


# The other module shouldn't exist.
# Functions in it need to be organized
from plottool_ibeis.plots import draw_hist_subbin_maxima
#from plottool_ibeis.draw_func2 import *  # NOQA
from plottool_ibeis.mpl_keypoint import draw_keypoints
from plottool_ibeis.mpl_sift import draw_sifts, render_sift_on_patch
from plottool_ibeis import fig_presenter

# Explicit eager imports and public re-exports.
# <AUTOGEN_INIT>

from plottool_ibeis import plot_helpers
from plottool_ibeis import fig_presenter
from plottool_ibeis import custom_constants
from plottool_ibeis import custom_figure
from plottool_ibeis import plots
from plottool_ibeis import draw_func2
from plottool_ibeis import interact_impaint
from plottool_ibeis import interactions
from plottool_ibeis import interact_multi_image
from plottool_ibeis import interact_keypoints
from plottool_ibeis import interact_matches
from plottool_ibeis import nx_helpers
from plottool_ibeis.plot_helpers import (SIFT_OR_VECFIELD, del_plotdat, draw,
                                   ensureqt, get_bbox_centers,
                                   get_plotdat, get_plotdat_dict,
                                   get_square_row_cols, kp_info, qt4ensure,
                                   set_plotdat,)
from plottool_ibeis.fig_presenter import (SLEEP_TIME, VERBOSE,
                                    all_figures_bring_to_front,
                                    all_figures_show,
                                    all_figures_tight_layout,
                                    all_figures_tile, bring_to_front,
                                    close_all_figures, close_figure,
                                    get_all_figures, get_all_qt4_wins,
                                    get_all_windows,
                                    get_figure_window, get_geometry,
                                    get_main_win_base, iup, iupdate,
                                    present, register_qt4_win, reset,
                                    set_geometry, show, show_figure,
                                    unregister_qt4_win, update,)
from plottool_ibeis.custom_constants import (BLACK, BLUE, BRIGHT_GREEN,
                                       BRIGHT_PURPLE, DARK_BLUE,
                                       DARK_GREEN, DARK_ORANGE, DARK_RED,
                                       DARK_YELLOW, DEEP_PINK, DPI,
                                       FALSE_RED, FIGSIZE, FIGSIZE_BIGGER,
                                       FIGSIZE_GOLD, FIGSIZE_HUGE,
                                       FIGSIZE_MED, FIGSIZE_SQUARE, FONTS,
                                       FontProp, GRAY, GREEN, LARGE,
                                       LARGER, LIGHTGRAY, LIGHT_BLUE,
                                       LIGHT_GREEN, LIGHT_PINK,
                                       LIGHT_PURPLE, MED, NEUTRAL,
                                       NEUTRAL_BLUE, ORANGE, PHI,
                                       PHI_denom, PHI_numer, PINK, PURPLE,
                                       PURPLE2, RED, SMALL, SMALLER,
                                       SMALLEST, TRUE_BLUE, TRUE_GREEN,
                                       UNKNOWN_PURP, WHITE, YELLOW,
                                       golden_wh, golden_wh2,)
from plottool_ibeis.custom_figure import (cla, clf, customize_figure,
                                    customize_fontprop, figure, gca, gcf,
                                    get_ax, get_image_from_figure,
                                    prepare_figure_for_save,
                                    prepare_figure_fpath, sanitize_img_ext,
                                    sanitize_img_fname, save_figure,
                                    set_figtitle, set_ticks, set_title,
                                    set_xlabel, set_xticks, set_ylabel,
                                    set_yticks)
from plottool_ibeis.plots import (colorline, draw_histogram,
                            draw_time_distribution, draw_time_histogram,
                            draw_timedelta_pie, estimate_pdf,
                            get_good_logyscale_kwargs, interval_line_plot,
                            interval_stats_plot, is_default_dark_bg,
                            multi_plot, plot_densities,
                            plot_multiple_scores, plot_pdf,
                            plot_probabilities, plot_probs,
                            plot_rank_cumhist, plot_score_histograms,
                            plot_search_surface, plot_sorted_scores,
                            plot_stems, set_logyscale_from_data,
                            word_histogram2, wordcloud,
                            zoom_effect01,)
from plottool_ibeis.draw_func2 import (BASE_FNUM, DARKEN, DEBUG, DF2_DIVIDER_KEY,
                                 FALSE, LEGEND_LOCATION, OffsetImage2,
                                 RenderingContext, TAU,
                                 TMP_mevent, TRUE, absolute_lbl, add_alpha,
                                 adjust_subplots,
                                 append_phantom_legend_label,
                                 ax_absolute_text,
                                 axes_bottom_button_bar,
                                 cartoon_stacked_rects, color_orimag,
                                 color_orimag_colorbar, colorbar,
                                 customize_colormap, dark_background,
                                 distinct_colors, distinct_markers,
                                 draw_bbox, draw_border, draw_boxedX,
                                 draw_keypoint_gradient_orientations,
                                 draw_keypoint_patch, draw_kpts2,
                                 draw_line_segments, draw_line_segments2,
                                 draw_lines2, draw_patches_and_sifts,
                                 draw_stems, draw_text,
                                 draw_text_annotations, draw_vector_field,
                                 ensure_divider, ensure_fnum,
                                 execstr_global, extract_axes_extents,
                                 fig_relative_text, fnum_generator,
                                 get_all_markers, get_axis_bbox,
                                 get_axis_xy_width_height,
                                 get_binary_svm_cmap, get_num_rc,
                                 get_orientation_color, get_pnum_func,
                                 imshow, imshow_null,
                                 is_texmode, label_to_colors, legend,
                                 lighten_rgb, lowerright_text,
                                 make_axes_locatable, make_bbox,
                                 make_bbox_positioners, make_fnum_nextgen,
                                 make_ori_legend_img, make_pnum_nextgen,
                                 next_fnum, overlay_icon, pad_axes,
                                 param_plot_iterator, parse_fontkw, plot,
                                 plot2, plotWidget, plot_bars,
                                 plot_descriptor_signature, plot_fmatch,
                                 plot_func, plot_hist, plot_histpdf,
                                 plot_sift_signature, plot_surface3d,
                                 pnum_generator, postsetup_axes,
                                 presetup_axes, print_valid_cmaps,
                                 remove_patches, render_figure_to_image,
                                 reverse_colormap, rotate_plot,
                                 scores_to_cmap, scores_to_color,
                                 set_axis_extent, set_axis_limit,
                                 set_figsize, show_chipmatch2,
                                 show_histogram, show_if_requested,
                                 show_kpts, show_phantom_legend_labels,
                                 show_signature, show_was_requested,
                                 small_xticks, small_yticks, space_xticks,
                                 space_yticks, to_base255,
                                 udpate_adjust_subplots, unique_rows,
                                 update_figsize, upperleft_text,
                                 upperright_text, variation_trunctate,
                                 width_from,)
from plottool_ibeis.interact_impaint import (PAINTER_BASE, PaintInteraction,
                                       draw_demo, impaint_mask2,)
from plottool_ibeis.interactions import (ExpandableInteraction, PanEvents,
                                   check_if_subinteract, pan_factory,
                                   zoom_factory,)
from plottool_ibeis.interact_multi_image import (BASE_CLASS,
                                           MultiImageInteraction,)
from plottool_ibeis.interact_keypoints import (KeypointInteraction,
                                         ishow_keypoints,)
from plottool_ibeis.interact_matches import (MatchInteraction2,
                                       show_keypoint_gradient_orientations,)
from plottool_ibeis.nx_helpers import (GraphVizLayoutConfig, LARGE_GRAPH,
                                 apply_graph_layout_attrs, draw_network2,
                                 dump_nx_ondisk, ensure_nonhex_color,
                                 format_anode_pos, get_explicit_graph,
                                 get_nx_layout, make_agraph,
                                 netx_draw_images_at_positions,
                                 nx_agraph_layout,
                                 parse_aedge_layout_attrs,
                                 parse_anode_layout_attrs, parse_point,
                                 show_nx,)
# Runtime hot-reload scaffolding retired.
# </AUTOGEN_INIT>
