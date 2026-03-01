from dependencies import *

def get_models():
    envelopes_log_8band = eelbrain.load.unpickle(PROCESSED_PREDICTOR_DIR / f'~processed_envelopes-log-8band.pickle')

    models = {
    #'envelope_log': [envelopes_log],
    # Compare different scales for the acoustic response
    'envelope_log_8band': [envelopes_log_8band],
    # The acoustic edge detection model
    #'envelope_log_onset': [envelopes_log, envelopes_onset],
    #'envelope_onset_8band': [envelopes_onset_8band],
    #'acoustic_8band': [envelopes_log_8band, envelopes_onset_8band],
    # Models with word-onsets and word-class
    #'words': [envelopes_words_onset],
    #'words+lexical': [envelopes_words_onset, envelopes_words_lexical, envelopes_words_nlexical],
    #'acoustic+words': [envelopes_log_8band, envelopes_onset_8band, envelopes_words_onset],
    #'acoustic+words+lexical': [envelopes_log_8band, envelopes_onset_8band, envelopes_words_onset, 
    #                           envelopes_words_lexical, envelopes_words_nlexical],
}
    return models

def get_durations(envelope):
    durations = [gt.time.tmax for stimulus, gt in zip(STIMULI, envelope)]
    return durations

def get_subject_model_predictors(models):
    subject_model_predictors = {}
    for subject in SUBJECTS:
        subject_model_predictors[subject] = {} 

        for model, predictors in models.items():
            # print(f"Concatenating: {subject} ~ {model} predictors")
            # Select and concetenate the predictors corresponding to the EEG trials
            predictors_concatenated = []
            for predictor in predictors:
                predictors_concatenated.append(eelbrain.concatenate([predictor[i] for i in trial_indexes]))
            subject_model_predictors[subject][model] = predictors_concatenated
    return subject_model_predictors