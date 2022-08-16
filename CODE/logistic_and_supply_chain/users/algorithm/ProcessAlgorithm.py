from ast import Break, Continue, Param
from django.conf import settings
from matplotlib import pyplot as plt
import pandas as pd
from statsmodels.tsa.arima_model import ARMA


class Algorithms:
    data = ""

    def __init__(self):
        path = settings.MEDIA_ROOT + "\\" + "SeriesReport-Not Seasonally Sales.csv"
        self.data = pd.read_csv(path)

    def stat_predation(self):
        import datetime

        data = self.data[['Period', 'Value']]

        data['Period'] = pd.to_datetime(data['Period'])

        dp = pd.to_datetime(data['Period'])
        data = data.groupby(dp)['Value'].sum().reset_index()
        data = data.set_index('Period')
        data.index
        y = data['Value'].resample('MS').mean()
        y['2019':]
        import itertools
        p = d = q = range(0, 2)
        pdq = list(itertools.product(p, d, q))
        seasonal_pdq = [(x[0], x[1], x[2], 12)
                        for x in list(itertools.product(p, d, q))]
        print('Examples of parameter combinations for Seasonal ARIMA...')
        print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
        print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
        print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
        print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

        import statsmodels.api as sm
        import itertools
        for param in pdq:
            for param_seasonal in seasonal_pdq:
                try:
                    mod = sm.tsa.statespace.SARIMAX(y,
                                                    order=param,
                                                    seasonal_order=param_seasonal,
                                                    enforce_stationarity=False,
                                                    enforce_invertibility=False)
                    results = mod.fit()
                # print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
                except Exception as ex:
                    print("Exception is ", str(ex))
                    continue

        import statsmodels.api as sm
        mod = sm.tsa.statespace.SARIMAX(y,
                                        order=(1, 1, 1),
                                        seasonal_order=(1, 1, 0, 12),
                                        enforce_stationarity=False,
                                        enforce_invertibility=False)
        results = mod.fit()

        pred_uc = results.get_forecast(steps=100)
        pred_ci = pred_uc.conf_int()

        import matplotlib.pyplot as plt
        import seaborn as sns

        sns.set()
        ax = data.hist(figsize=(15, 12), bins=20, color="#007959AA")
        plt.title("Future Forecast")
        plt.show()

        return pred_ci, ax
