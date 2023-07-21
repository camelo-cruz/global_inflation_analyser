#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pandas as pd
from analysis import Analyser


# Here, a test for the initialization of the Analyser class is defined.
# It checks if the attributes `data_folder` and `files` were set correctly.
def test_analyser_initialization():
    analyser = Analyser()
    assert analyser.data_folder == "data/"
    assert analyser.files == [os.path.join(analyser.data_folder, file)
                              for file in os.listdir(analyser.data_folder)]


# Here, a test for the `set_datafile` method is defined.
# It checks if the method returns the expected data and sets the class attributes correctly.
def test_set_datafile():
    analyser = Analyser()
    product = "example_product"
    country_list = ["country1", "country2"]
    start_time = "2022-01-01"
    stop_time = "2022-12-31"

    # The `set_datafile` method is called, and the result is stored in `data`.
    data = analyser.set_datafile(product, country_list, start_time, stop_time)

    # Here are some assertions to ensure that the result is correct.
    assert isinstance(data, pd.DataFrame)  # Checks if the result is a DataFrame.
    assert data.shape[0] > 0  # Checks if the DataFrame contains data (number of rows > 0).

    # More assertions can be added to test specific behavior.

    # Here, the attributes of the `analyser` instance are checked to ensure they were set correctly.
    assert analyser.product == product
    assert analyser.country_list == country_list
    assert analyser.start_time == start_time
    assert analyser.stop_time == stop_time

