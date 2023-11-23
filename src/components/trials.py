from enum import IntEnum, auto

from pandas import DataFrame

from src.components.stimuli import stimuli
from src.components.targets import targets
from src.constants import (
    COUNTERBALANCING_ASCENDING,
    RANDOM_TRIAL_ORDER,
    SPECIES_COUNTERBALANCING,
    STIMULUS_ONSET_ASYNCS,
)


class Validity(IntEnum):
    VALID = auto()
    INVALID = auto()


class Response(IntEnum):
    SPACE = auto()
    H = auto()


def trials_init(participant_details: dict[str, int]) -> DataFrame:
    """
    Initialises the experimental trials.
    Parameters
    ----------
    participant_details: dict[str, int]
        Detials of the participant.
    Returns
    -------
    pandas.DataFrame
    """
    dataframe = DataFrame(
        columns=[
            "participant_number",
            "age",
            "gender",
            "culture",
            "stimulus_species",
            "stimulus_gaze_direction",
            "stimulus_number",
            "stimulus_image",
            "target_letter",
            "target_location",
            "target_image",
            "gaze_validity",
            "soa",
            "response",
            "response_accuracy",
            "reaction_time",
        ]
    )

    trial_number = 0
    for stimulus in stimuli:
        for target in targets:
            for soa in STIMULUS_ONSET_ASYNCS:
                trial = {
                    "soa": soa,
                    "response": 0,
                    "response_accuracy": 0,
                    "reaction_time": 0,
                }
                trial.update(participant_details)
                trial.update(stimulus)
                trial.update(target)
                trial["gaze_validity"] = int(
                    trial["stimulus_gaze_direction"] == trial["target_location"]
                )
                dataframe.loc[trial_number] = trial
                trial_number += 1

    if RANDOM_TRIAL_ORDER:
        dataframe = dataframe.sample(frac=1).reset_index(drop=True)

    if SPECIES_COUNTERBALANCING:
        dataframe = dataframe.sort_values(
            by=["stimulus_species"], ascending=COUNTERBALANCING_ASCENDING
        ).reset_index(drop=True)

    dataframe.index.name = "trial_number"

    return dataframe
