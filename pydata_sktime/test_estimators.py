# -*- coding: utf-8 -*-
"""Simple test suite for estimators."""

import pytest

from sktime.utils.estimator_checks import check_estimator

from pydata_sktime.estimators import SimpleMovingAverage
from pydata_sktime.forecaster_with_extras import EasyMAWithUpdateAndProba

MY_ESTIMATORS = [SimpleMovingAverage, EasyMAWithUpdateAndProba]


@pytest.mark.parametrize("estimator_class", MY_ESTIMATORS)
def test_my_estimators(estimator_class):
    """Runs sktime check_estimator test suite on the estimator_class."""
    check_estimator(estimator_class, return_exceptions=False)
