"""
This file implements module's main logic.
Data processing should happen here.

Edit this file to implement your module.
"""

import joblib
import os
import numpy as np
from logging import getLogger

log = getLogger("module")

ORDERED_LABELS = [label.strip() for label in os.getenv("ORDERED_LABELS", "").split(',')]
OUTPUT_LABEL = os.getenv("OUTPUT_LABEL", "")

log.info("Loading the model ...")
if os.getenv("MODEL_DOWNLOAD_URL"):
    log.debug("Loading the model downloaded into the docker container: model/downloaded_model.sav ...")
    MODEL = joblib.load("model/downloaded_model.sav")
else:
    log.debug(f"Loading the model mounted by volume to the docker container: {os.getenv('MODEL_FILEPATH')} ...")
    MODEL = joblib.load(os.getenv('MODEL_FILEPATH'))
log.info("Model loaded successfully.")

def module_main(received_data: any) -> [any, str]:
    """
    Process received data by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        any: Processed data that are ready to be sent to the next module or None if error occurs.
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Processing ...")

    try:
        if type(received_data) == list:
            X = np.array([[data[label] for label in ORDERED_LABELS] for data in received_data])
            y_hat = MODEL.predict(X)
            processed_data = [{OUTPUT_LABEL: y} for y in y_hat]
        else:
            X = np.array([received_data[label] for label in ORDERED_LABELS]).reshape(1,-1)
            processed_data = {OUTPUT_LABEL: MODEL.predict(X)[0]}

        return processed_data, None

    except Exception as e:
        return None, f"Exception in the module business logic: {e}"
