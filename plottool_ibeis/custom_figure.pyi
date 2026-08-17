import matplotlib as mpl
import matplotlib.axes
import matplotlib.figure
from typing import Any
from _typeshed import Incomplete


def customize_figure(fig, docla):
    ...


def gcf():
    ...


def gca():
    ...


def cla():
    ...


def clf():
    ...


def get_fig(fnum: Incomplete | None = ...):
    ...


def ensure_fig(fnum: Incomplete | None = ...):
    ...


def get_ax(fnum: Incomplete | None = ..., pnum: Incomplete | None = ...):
    ...


def figure(fnum: int | None = None,
           pnum: int | str | tuple[int, int, int] | None = None,
           docla: bool = False,
           title: str | None = None,
           figtitle: Any | None = None,
           doclf: bool = False,
           projection: Any | None = None,
           **kwargs) -> mpl.figure.Figure:
    ...


def prepare_figure_for_save(fnum,
                            dpi: Incomplete | None = ...,
                            figsize: Incomplete | None = ...,
                            fig: Incomplete | None = ...):
    ...


def sanitize_img_fname(fname):
    ...


def sanitize_img_ext(ext, defaultext: Incomplete | None = ...):
    ...


def prepare_figure_fpath(fig,
                         fpath,
                         fnum,
                         usetitle,
                         defaultext,
                         verbose,
                         dpath: Incomplete | None = ...):
    ...


def get_image_from_figure(fig):
    ...


def save_figure(fnum: int | None = None,
                fpath: str | None = None,
                fpath_strict: str | None = None,
                usetitle: bool = False,
                overwrite: bool = True,
                defaultext: str | None = None,
                verbose: int = 1,
                dpi: int | None = None,
                figsize: tuple[int, int] | None = None,
                saveax: bool | mpl.axes.Axes | None = None,
                fig: Incomplete | None = ...,
                dpath: Incomplete | None = ...):
    ...


def set_ticks(xticks, yticks) -> None:
    ...


def set_xticks(tick_set) -> None:
    ...


def set_yticks(tick_set) -> None:
    ...


def customize_fontprop(font_prop, **fontkw):
    ...


def set_title(title: str = ..., ax: Incomplete | None = ..., **fontkw) -> None:
    ...


def set_xlabel(lbl: Any, ax: None = None, **kwargs) -> None:
    ...


def set_ylabel(lbl, ax: Incomplete | None = ..., **kwargs) -> None:
    ...


def set_figtitle(figtitle: Any,
                 subtitle: str = '',
                 forcefignum: bool = True,
                 incanvas: bool = True,
                 size: Any | None = None,
                 fontfamily: Any | None = None,
                 fontweight: Any | None = None,
                 fig: Any | None = None,
                 font: Incomplete | None = ...) -> None:
    ...
