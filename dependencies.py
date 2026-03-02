# IMPORT LIBRARIES

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import ConnectionPatch
import eelbrain
import mne
import re
from paths import *
from utils import *

# CONSTANTS

SUBJECTS = [path.name for path in EEG_DIR.iterdir() if re.match(r'S\d*', path.name)]
STIMULI = [str(i) for i in range(1, 13)]
LOW_FREQUENCY = 0.5
HIGH_FREQUENCY = 20
