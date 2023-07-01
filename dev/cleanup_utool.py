"""
Helper to check what the current usage of utool in the project is as we slowly
remove it.

SeeAlso:
    ~/code/ubelt/dev/oneoff/remove_ancient_constructs.py
"""
import xdev
import plottool_ibeis
import ubelt as ub
mod_dpath = ub.Path(plottool_ibeis.__file__).parent

grep_results = xdev.grep('\\but\\.\\w*\\b', dpath=mod_dpath)

instances = []

for result in grep_results:
    for line in result.found_lines:
        for match in result.pattern.pattern.findall(line):
            instances.append(match)
            ...

current_utool_usage = ub.udict(ub.dict_hist(instances)).sorted_values()
print('current_utool_usage = {}'.format(ub.urepr(current_utool_usage, nl=1)))
