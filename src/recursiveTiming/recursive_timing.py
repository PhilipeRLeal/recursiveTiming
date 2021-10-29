from datetime import datetime
import numpy as np


class RecursiveTimer():
    def __init__(self):
        self.NewTime = {}
        self.reference = {}

    def verbose(self):
        if self.reference == {}:
            pass
        else:
            NewTimeKey = list(self.NewTime.keys())[0]
            RefereceKey = list(self.reference.keys())[0]
            SpeedUp = (self.NewTime[NewTimeKey] /
                       self.reference[RefereceKey]
                       )

            print('Reference Time: ', self.reference)
            print('New Time: ', self.NewTime)
            print(
                'Speed gain (new/old) {0}/{1}: {2:.2f}'.format(NewTimeKey,
                                                               RefereceKey,
                                                               SpeedUp
                                                               )
            )
            print('New-Time is faster Reference-time: ',
                  self.NewTime[NewTimeKey] < self.reference[RefereceKey])

    def __call__(self, *args, **kwargs):

        Results = self.decorator_factory(*args, **kwargs)

        return Results

    def decorator_factory(
            self,
            argument='CPU',
            function=callable,
            *args,
            **kwargs):
        self.argument = argument
        runs = kwargs.pop('runs', 5)
        print('N° Runs: ', runs)
        print(argument + ' Processing')

        def decorator(function):
            def wrapper():
                dts = np.zeros((runs)).ravel()
                std, average = np.empty((2))
                for i in range(runs):
                    t0 = datetime.now()
                    _ = function(*args, **kwargs)
                    t1 = datetime.now()
                    dt = t1 - t0
                    dts[i] = dt.microseconds

                std, average = dts.std(), dts.mean()
                self.std = std
                self.NewTime = {argument: average}
                print(
                    "Average time: {0:.2f}ms Std {1:.2f}ms".format(
                        average, std))
                self.verbose()
                self.reference = self.NewTime
                return None
            return wrapper

        return decorator
