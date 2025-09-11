from . import stats_utils

class Experiment:

    def __init__(self):
        self.parameter_dict = {'Sample Size': 20,

                               'Group1 Mean': 100,
                               'Group1 StDev': 10,

                               'Group2 Mean': 100,
                               'Group2 StDev': 10,
                               }

        self.group1_x = None
        self.group2_x = None
        self.group1_y = None
        self.group2_y = None


    def get_population_distributions(self):
        self.group1_x, self.group1_y = stats_utils.get_distribution_xys(self.parameter_dict['Group1 Mean'],
                                                                        self.parameter_dict['Group1 StDev'])
        self.group2_x, self.group2_y = stats_utils.get_distribution_xys(self.parameter_dict['Group2 Mean'],
                                                                        self.parameter_dict['Group2 StDev'])
