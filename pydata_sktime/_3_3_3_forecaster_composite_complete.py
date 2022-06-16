# -*- coding: utf-8 -*-
# copyright: sktime developers, BSD-3-Clause License (see LICENSE file)
"""Pydata tutorial estimators: composite forecaster, final version."""
import warnings

import numpy as np
import pandas as pd
from sktime.forecasting.base import BaseForecaster


class CompositeMovingAverage(BaseForecaster):
    """Silly tutorial example: moving average after applying a transformation.

    Behaviour is same as SimpleMovingAverage, with the following additions.

    Estimator wraps a clone of `transformer` which:
    * is fitted to data seen in `fit`
    * is applied to forecast produced by `predict`, then returning transformed forecast

    Parameters
    ----------
    window_length : int, optional, default=1
        window length over which we compute the mean
    transformer : sktime transformer, optional, default=None
        if passed, transformer is applied before computing MA
    """

    # todo: fill out estimator tags here
    #  tags are inherited from parent class if they are not set
    # todo: define the forecaster scitype by setting the tags
    #  the "forecaster scitype" is determined by the tags
    #   scitype:y - the expected input scitype of y - univariate or multivariate or both
    # tag values are "safe defaults" which can usually be left as-is
    _tags = {
        "scitype:y": "univariate",  # which y are fine? univariate/multivariate/both
        "ignores-exogeneous-X": True,  # does estimator ignore the exogeneous X?
        "handles-missing-data": False,  # can estimator handle missing data?
        "y_inner_mtype": "pd.Series",  # which types do _fit, _predict, assume for y?
        "X_inner_mtype": "pd.DataFrame",  # which types do _fit, _predict, assume for X?
        "requires-fh-in-fit": False,  # is forecasting horizon already required in fit?
        "X-y-must-have-same-index": True,  # can estimator handle different X/y index?
        "enforce_index_type": None,  # index type that needs to be enforced in X/y
        "capability:pred_int": False,  # does forecaster implement predict_quantiles?
        # deprecated and likely to be removed in 0.12.0
    }

    def __init__(self, window_length: int = 1, transformer=None):

        self.window_length = window_length
        self.transformer = transformer
        # parameter copies should never be changed!

        # so, we make a clone that is going to be fitted etc
        if transformer is None:
            self.transformer_ = None
        else:
            self.transformer_ = transformer.clone()

        # todo: change "MyForecaster" to the name of the class
        super(CompositeMovingAverage, self).__init__()

    # todo: implement this, mandatory
    def _fit(self, y, X=None, fh=None):
        """Fit forecaster to training data.

        private _fit containing the core logic, called from fit

        Writes to self:
            Sets fitted model attributes ending in "_".

        Parameters
        ----------
        y : guaranteed to be pd.Series
        fh : guaranteed to be ForecastingHorizon or None, optional (default=None)
            The forecasting horizon with the steps ahead to to predict.
            Required (non-optional) here if self.get_tag("requires-fh-in-fit")==True
            Otherwise, if not passed in _fit, guaranteed to be passed in _predict.
            Ignored by this estimator.
        X : guaranteed to be pd.DataFrame, optional (default=None)
            Exogeneous time series to fit to.
            Ignored by this estimator.

        Returns
        -------
        self : reference to self
        """
        if self.transformer_ is not None:
            self.transformer_.fit(y)

        if len(y) < self.window_length:
            warnings.warn(
                "y has less time-steps than window_length, the full series will be used"
            )
            self._forecast_value = np.mean(y)
        else:
            self._forecast_value = np.mean(y.iloc[-self.window_length :])

        return self

    # todo: implement this, mandatory
    def _predict(self, fh, X=None):
        """Forecast time series at future horizon.

        private _predict containing the core logic, called from predict

        State required:
            Requires state to be "fitted".

        Accesses in self:
            Fitted model attributes ending in "_"
            self.cutoff

        Parameters
        ----------
        fh : guaranteed to be ForecastingHorizon or None, optional (default=None)
            The forecasting horizon with the steps ahead to to predict.
            If not passed in _fit, guaranteed to be passed here
        X : guaranteed to be pd.DataFrame, optional (default=None)
            Exogenous time series
            Ignored by this estimator.

        Returns
        -------
        y_pred : pd.Series
            Point predictions
        """
        index = fh.to_absolute(self.cutoff)
        y_pred = pd.Series(self._forecast_value, index=index)
        if self.transformer_ is not None:
            y_pred = self.transformer_.transform(y_pred)
        return y_pred

    # todo: implement this if this is an estimator contributed to sktime
    #   or to run local automated unit and integration testing of estimator
    #   method should return default parameters, so that a test instance can be created
    @classmethod
    def get_test_params(cls, parameter_set="default"):
        """Return testing parameter settings for the estimator.

        Parameters
        ----------
        parameter_set : str, default="default"
            Name of the set of test parameters to return, for use in tests. If no
            special parameters are defined for a value, will return `"default"` set.
            There are currently no reserved values for forecasters.

        Returns
        -------
        params : dict or list of dict, default = {}
            Parameters to create testing instances of the class
            Each dict are parameters to construct an "interesting" test instance, i.e.,
            `MyClass(**params)` or `MyClass(**params[i])` creates a valid test instance.
            `create_test_instance` uses the first (or only) dictionary in `params`
        """
        from sktime.transformations.series.exponent import ExponentTransformer

        params = [
            {"window_length": 1},
            {"window_length": 5, "transformer": ExponentTransformer(3)},
            {"window_length": 100},
        ]
        return params
