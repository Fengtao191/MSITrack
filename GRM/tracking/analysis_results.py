import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [8, 8]

import _init_paths
from lib.test.analysis.plot_results import plot_results, print_results
from lib.test.evaluation import get_dataset, trackerlist

trackers = list()
trackers.extend(trackerlist(name='grm', parameter_name='baseline_hsitrack', dataset_name='NOTU',
                            run_ids=None, display_name='hsitrack'))

dataset = get_dataset('hsitrack')
print_results(trackers, dataset, 'hsitrack', merge_results=True, plot_types=('success', 'norm_prec', 'prec'), avist=False)
