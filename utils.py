import dependencies

def get_models(exclude=[]):
    envelopes_log = dependencies.eelbrain.load.unpickle(dependencies.PROCESSED_PREDICTOR_DIR / f'~processed_envelopes-log.pickle')
    envelopes_onset = dependencies.eelbrain.load.unpickle(dependencies.PROCESSED_PREDICTOR_DIR / f'~processed_envelopes-onset.pickle')

    models = {
    'envelope_log': [envelopes_log],
    'envelope_onset': [envelopes_onset],
    # Compare different scales for the acoustic response
    #'envelope_log_8band': [envelopes_log_8band],
    # The acoustic edge detection model
    'envelope_log_onset': [envelopes_log, envelopes_onset],
    #'envelope_onset_8band': [envelopes_onset_8band],
    #'acoustic_8band': [envelopes_log_8band, envelopes_onset_8band],
    # Models with word-onsets and word-class
    #'words': [envelopes_words_onset],
    #'words+lexical': [envelopes_words_onset, envelopes_words_lexical, envelopes_words_nlexical],
    #'acoustic+words': [envelopes_log_8band, envelopes_onset_8band, envelopes_words_onset],
    #'acoustic+words+lexical': [envelopes_log_8band, envelopes_onset_8band, envelopes_words_onset, 
    #                           envelopes_words_lexical, envelopes_words_nlexical],
}
    if exclude != []:
        for exclution in exclude:
            models.pop(exclution)
    return models

def get_durations(envelope):
    durations = [gt.time.tmax for stimulus, gt in zip(dependencies.STIMULI, envelope)]
    return durations
