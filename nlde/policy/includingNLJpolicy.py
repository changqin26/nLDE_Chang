"""
Created on Nov 24, 2011

@author: Maribel Acosta
"""
import random
from policy import Policy
from multiprocessing import Manager

class IncludingNLJ(Policy):
    """

    """

    def __init__(self):
        self.priority_table = {}

    def initialize_priorities(self, plan_order):
        self.priority_table = {operator: 0 for operator in plan_order}
        #Create a new dictionary self.priority_table where the keys are the operators in the plan_order dictionary, and the values are initialized to 0.

    def select_operator(self, operators, operators_desc, tup=None, operators_vars=None, operators_not_sym=[]):
        # Removing NLJ operators in the query plan.
        #candidates = list(set(operators) - set(operators_not_sym))

        #For NLJNotEnd policy, we want all operators at the beginning of the routing policy.
        candidates = list(set(operators))

        # List of selectable operators contain non-cartesian product routes.
        operators_selectable = []
        for o in candidates:
            if set(tup.sources) & set(operators_desc[o].keys()):
                operators_selectable.append(o)

        # The next operators is a dependent operator.
        #if len(operators_selectable) == 0:
            #return operators[0]


        # Choose the operator with the least output so far
        selected_op = operators_selectable[0]
        min_output = self.priority_table[selected_op]
        for operator in operators_selectable:
            if self.priority_table[operator] < min_output:
                selected_op = operator
                min_output = self.priority_table[operator]

        return selected_op

    def update_priorities(self, tup, queue=-1):
        #Track the number of tuples produced by each operator in the query plan
        if tup.from_operator is not None:
            self.priority_table[tup.from_operator] += 1
