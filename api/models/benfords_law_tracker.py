import math

class BenfordsLawTracker(object):
    EXPECTED_PERCENTAGE = 'expected_percentage'
    ACTUAL_PERCENTAGE = 'actual_percentage'
    OCCURRENCES = 'occurrences'

    def __init__(self):
        self._total_rows = 0
        self._counters = self._build_counters

    def _benfords_law(self, number):
        if number == 0:
            return

        return (math.log10(number +1) - math.log10(number)) * 100

    def _set_percentage(self, digit):
        return self._counters[digit][self.OCCURRENCES] / (self._total_rows / 100)

    @property
    def _build_counters(self):
        return [{self.EXPECTED_PERCENTAGE: self._benfords_law(index),
                 self.ACTUAL_PERCENTAGE: 0,
                 self.OCCURRENCES: 0}
                for index in range(0,10)]

    @property
    def counters(self):
        return self._counters

    def increase_row_count(self):
        self._total_rows +=1

    def increase_digit_counter(self, digit):
        self._counters[digit][self.OCCURRENCES] += 1
        self._counters[digit][self.ACTUAL_PERCENTAGE] = self._set_percentage(digit)
