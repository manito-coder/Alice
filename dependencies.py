# IMPORT LIBRARIES

from pathlib import Path
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch, Patch
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.gridspec import GridSpecFromSubplotSpec
import eelbrain
import mne
import re
from paths import *
from utils import *
from scipy.stats import ttest_rel, pearsonr, ttest_1samp, zscore


# CONSTANTS

SUBJECTS = [path.name for path in EEG_DIR.iterdir() if re.match(r'S\d*', path.name)]
STIMULI = [str(i) for i in range(1, 13)]
LOW_FREQUENCY = 0.5
HIGH_FREQUENCY = 20
