import csv
import json
import pprint
import random
import re
# import rstr


class Constraint:
    """
        Class for constraints object.
        Each constraintLine is list: (entity, attribute, operator, value, aggregation:optional)
    """
    def __init__(self, constraintLine):
        self.entity = constraintLine[0].strip()
        self.attribute = constraintLine[1].strip()
        self.operator = constraintLine[2].strip()
        reg = re.compile('([\]\[])')
        self.value = [val.strip() for val in reg.sub(r'', constraintLine[3].strip()).split(';')]
        if len(constraintLine) > 4:
            self.aggregation = constraintLine[4].strip()


class DataConstraintGenerator:
    """
        Class for generating data given contraints.
    """
    DATA_CONSTRAINT_FILE_NAME = "data_constraints.csv"  # The naming needs to be fixed!

    def __init__(self):
        # If the "data_constraints.csv" is not provided make it an empty list since it's not mandatory
        self.constraints = self.loadConstraints(DataConstraintGenerator.DATA_CONSTRAINT_FILE_NAME)

        self.num_of_fields = 100
        # Two layer of nested dictionary with Entity name as first layer key & attribute name as second key.
        # Value is generated (specified values) data list
        self.constraint_map = {}
        try:
                self.setup_constraint_map()
        except Exception as e:
            print("Exception in data constraint generator! Please check the codebase or the CSV file to see if it conforms to the data schema!\n Error: ", e)

    def loadConstraints(self, constraintFile):
        """
            Reads the constraints from the given csv file.
            Input: csv file name
            Return: list of Constraint objects
        """
        constraints = list()
        try:
            with open(constraintFile, 'r') as file:
                for constraint_line in csv.reader(file, delimiter=','):
                    if not constraint_line:
                        # If there exists empty lines in the csv file. Ignore that line (TA's should not be responsible
                        # to make sure there are no empty lines in the csv file...
                        continue
                    constraints.append(Constraint(list(constraint_line)))
        except FileNotFoundError:
            # If the "data_constraints.csv" is not provided make it an empty list since it's not mandatory
            pass
            
        return constraints

    @staticmethod
    def isInt(obj):
        """
            Checks if the input is integer or not.
            Input: object
            Return: True if integer, otherwise false.
        """
        try: 
            obj = int(obj)
            return True
        except ValueError:
            return False

    def random_sample(self, minVal = 0, maxVal = 100):
        """
            Generates random list of values by sampling.
            Input: minimum value and maximum value.
            Return: list of random values between min and max values.
        """
        return random.sample(range(minVal, maxVal), random.randint(0,maxVal-minVal) % 20)

    def random_sample_with_ranges(self, minVal=0, maxVal=100, no_of_samples_range=list()):
        """
            Generates random list of values by sampling.
            Input: minimum value, maximum value and range of samples to be drawn.
            Return: list of random values between min and max values.
        """
        res = list()
        if len(no_of_samples_range) == 0:
            return res
        elif len(no_of_samples_range) == 1:
            return random.sample(range(minVal, maxVal), no_of_samples_range[0])
        elif len(no_of_samples_range) == 2:
            rangeA = no_of_samples_range[0]
            rangeB = no_of_samples_range[1]
            return random.sample(range(minVal, maxVal), random.randint(rangeA, rangeB))

        return res

    def op_eq(self, val):
        """
            Generates random list with the given value.
            Input: target value (list with single element).
            Return: list of values.
        """
        res = list()
        if DataConstraintGenerator.isInt(val[0]):
            res.extend([int(val[0])] * random.randint(5, 10))
        else:
            res.extend([val[0]] * random.randint(5, 10))
        return res

    def op_gt(self, val):
        """
            Generates random list with elements having value greater than the specified value.
            Input: target value (list with single element).
            Return: list of values.
        """
        val = int(val[0])
        res = [val+1]
        res.extend(self.random_sample(val + 1, val + 25))
        return res

    def op_gte(self, val):
        """
            Generates random list with elements having value greater than or equal to the specifed value.
            Input: target value (list with single element).
            Return: list of values.
        """
        val = int(val[0])
        res = [val]
        res.extend(self.random_sample(val, val + 25))
        return res

    def op_lt(self, val):
        """
            Generates random list with elements having value less than the specified value.
            Input: target value (list with single element).
            Return: list of values.
        """
        val = int(val[0])
        res = [val-1]
        res.extend(self.random_sample(max(0, val-25), val))
        return res

    def op_lte(self, val):
        """
            Generates random list with elements having vlaue less than or equal to the specified value.
            Input: target value (list with single element).
            Return: list of values.
        """
        val = int(val[0])
        res = [val]
        res.extend(self.random_sample(max(0, val-25), val))
        return res
    
    def op_like(self, val):
        """
            Generates random list of strings that are generated by the given regex pattern.
            Input: regex pattern (list with single element).
            Return: list of generated strings.
        """
        # # Uncomment the below after having docker install rstr module!!
        # res = [rstr.xeger(val[0]) for _ in range(random.randint(0, 10))]
        # return res
        return val

    def op_in(self, val):
        """
            Returns a list of values for the IN operator based on the data type. If all elements could be integers,
            it returns a list of integers, else the list data would be of string type. (Users/TA's would need to
            put QUOTES around integer/numbers if they wish the values would be treated by the system as String type
            instead of integers/numbers).
            Input: list of values.
            Return: list of values.
        """
        # res = random.choices(val, k=random.randint(1, 10))
        if all(map(self.isInt, val)):
            return [int(value) for value in val]

        def peel_nested_quotes(value):
            """
            Used to peel string values that are surrounded by extra quotes (If TA's input integers with quotes to
            indicate they should be treated as strings).
            """
            if not value:
                return ''

            if value[0] == '\'' or value[0] == '\"':
                return value[1:-1]
            else:
                return value

        return [peel_nested_quotes(value) for value in val]

    def op_not_in(self, val):
        """
            Generates random list of values that are not in the given elements.
            Input: list of values for sampling.
            Return: empty list as it satisfies the "Not In".
        """
        res = list()
        return res

    def op_between(self, val):
        """
            Generates random list of values from the given two elements.
            Input: list of two values.
            Return: list of values between the given two elements.
        """
        return self.op_in(val)

    def aggregation_count(self, operator, val):
        """
            Generates random list of values with the specified count.
            Input: comparision operator and target count(list with single element).
            Return: specified number of random elements according to the corresponding comparision operator.
                    For example, input is (">", [10]) then result list will have more than 10 elements.
        """
        res = list()
        val = int(val[0])
        if operator == "=":
            res.extend(self.random_sample_with_ranges(0, 1000, [val]))
        elif operator == ">":
            res.extend(self.random_sample_with_ranges(0, 1000, [val + 1, val + 100]))
        elif operator == ">=":
            res.extend(self.random_sample_with_ranges(0, 1000, [val, val + 100]))
        elif operator == "<":
            res.extend(self.random_sample_with_ranges(0, 1000, [0, val - 1]))
        elif operator == "<=":
            res.extend(self.random_sample_with_ranges(0, 1000, [0, val - 1]))
        
        return res

    def aggregation_avg(self, operator, val):
        """
            Generates random list of values with the given mean.
            Input: comparision operator and specified mean(list with single element).
            Return: list of values with the given mean and corresponding comparision operator. 
                    For example, input is (">", [10.5]) then result list will be containing values 
                    with mean greater than 10.5.
        """
        res = list()
        mean = float(val[0])
        n = random.randint(1, 20)
        desired_sum = mean * n
        variance = int(0.25 * mean)

        min_v = mean - variance
        max_v = mean + variance
        list_with_fixed_mean = [min_v] * n

        diff = desired_sum - min_v * n
        while diff > 0:
            a = random.randint(0, n - 1)
            if list_with_fixed_mean[a] >= max_v:
                continue
            list_with_fixed_mean[a] += 1
            diff -= 1

        if operator == "=":
            res.extend(list_with_fixed_mean)
        elif operator == ">":
            rand_index = random.randint(1, len(list_with_fixed_mean) - 1)
            list_with_fixed_mean[rand_index] += rand_index
            res.extend(list_with_fixed_mean)
        elif operator == ">=":
            if random.random() < 0.5:
                rand_index = random.randint(1, len(list_with_fixed_mean) - 1)
                list_with_fixed_mean[rand_index] += rand_index
            res.extend(list_with_fixed_mean)
        elif operator == "<":
            rand_index = random.randint(1, len(list_with_fixed_mean) - 1)
            list_with_fixed_mean[rand_index] -= rand_index
            list_with_fixed_mean[rand_index] = max(0, list_with_fixed_mean[rand_index])
            res.extend(list_with_fixed_mean)
        elif operator == "<=":
            if random.random() < 0.5:
                rand_index = random.randint(1, len(list_with_fixed_mean) - 1)
                list_with_fixed_mean[rand_index] -= rand_index
                list_with_fixed_mean[rand_index] = max(0, list_with_fixed_mean[rand_index])
            res.extend(list_with_fixed_mean)
        
        # print(sum(res)/len(res))
        return res

    def aggregation_max_min(self, operator, val):
        """
            Generates random list of values such that max and min operations always results 
            the specified value for corresponding comparision operator.
            Input: comparision operator and specified target value(list with single element)
            Return: list of generated random values.
                    For example, input is (">=", [10]) then the result list will have values greater
                    than or equal to 10, such that max/min operation always results the value greater than
                    given input 10.
        """
        res = list()
        val = float(val[0])
        if operator == "=":
            res.extend([val]*random.randint(1,10))
        elif operator == ">":
            res.extend(self.random_sample(int(val + 1), int(val + 100)))
        elif operator == ">=":
            res.extend(self.random_sample(int(val), int(val + 100)))
        elif operator == "<":
            res.extend(self.random_sample(1, int(val)))
        elif operator == "<=":
            res.extend(self.random_sample(1, int(val + 1)))
        
        return res

    def generateValues(self, operator:str, val:list):
        """
            Generates random list of values according to the comparision operator and specified value(s).
            Input: comparision operator and value(s)
            Return: list of values.
        """

        # Map for comparision/logical operators and their corresponding functions.
        op_func = {
            '=': self.op_eq,
            '>': self.op_gt,
            '>=': self.op_gte,
            '<': self.op_lt,
            '<=': self.op_lte,
            'like': self.op_like,
            'in': self.op_in,
            'not in': self.op_not_in,
            'between': self.op_between,
            }

        # Gets the function for the corresponding comparision operator
        func = op_func.get(operator.lower(), lambda: "Invalid Operator")
        res = func(val)
        # print("The generated values for operator: {} and value: {} is : {}".format(operator, val,res))
        return res

    def generateValuesForAggregations(self, aggregation:str, operator:str, val:list):
        """
            Generates random list of values for the aggregation methods.
            Input: aggregation method, comparision operator and specified value.
            Return: list of generated values.
        """

        # Map for aggregation methods and corresponding functions.
        aggregation_func = {
            'count': self.aggregation_count,
            'avg': self.aggregation_avg,
            'max': self.aggregation_max_min,
            'min': self.aggregation_max_min
            }

        # Gets the function for the corresponding aggregated method.
        func = aggregation_func.get(aggregation.lower(), lambda: "Invalid aggregation")
        res = func(operator, val)
        # print(res)
        return res

    def setup_constraint_map(self):
        for constraint_obj in self.constraints:
            entity = constraint_obj.entity
            attr = constraint_obj.attribute
            operator = constraint_obj.operator
            value_list = constraint_obj.value
            aggregation = constraint_obj.aggregation if hasattr(constraint_obj, 'aggregation') else None

            # Generate value list
            if aggregation:
                data_values = self.generateValuesForAggregations(aggregation, operator, value_list)
            else:
                data_values = self.generateValues(operator, value_list)

            # Construct constraint map
            # Check for entity
            if entity not in self.constraint_map:
                self.constraint_map[entity] = {}

            # Check for entity attribute as key and if data list exists
            if attr not in self.constraint_map[entity]:
                self.constraint_map[entity][attr] = data_values
            else:
                self.constraint_map[entity][attr].extend(data_values)

        # After all data are documented, shuffle all lists of data to create some randomness!!
        for entity_name in self.constraint_map:
            for attr_name in self.constraint_map[entity_name]:
                if self.constraint_map[entity_name][attr_name]:
                    random.shuffle(self.constraint_map[entity_name][attr_name])

        # print("Data Map: ", self.constraint_map)

    def longest_entity_attr_value_list_len(self, entity):
        """
        Returns the longest attribute value length of an entity from self.constrain_map for round robin combination
        data generation on all list of values in the entity
        """
        if not self.entity_in_constrain_map(entity):
            return 0

        if not self.entity_attribute_exists(entity):
            return 0

        longest_len = 0
        for attr_key in self.constraint_map[entity]:
            longest_len = max(longest_len, len(self.constraint_map[entity][attr_key]))

        return longest_len

    def generate_data_instances(self, entity):
        """
        [{attribute_name: value}. {attribute_name2: value}, ...]
        Returns a list of dicts to map attribute and constraint value of each data instance generated for
        the designated entity in a round robin fashion based on the longest constraint attribute values
        """
        data_list = []
        longest_len = self.longest_entity_attr_value_list_len(entity)
        # Generate constraint values on each run for designated attributes of the entity
        for i in range(longest_len):
            constraint_data_dict = {}
            for attr in self.constraint_map[entity]:
                attr_value_list_len = len(self.constraint_map[entity][attr])
                constraint_data_dict[attr] = self.constraint_map[entity][attr][i % attr_value_list_len]
            data_list.append(constraint_data_dict)

        # print("Generated Constraint Data: ", data_list)
        return data_list

    def entity_in_constrain_map(self, entity):
        if not self.constraint_map:
            return False

        return entity in self.constraint_map

    def entity_attribute_exists(self, entity):
        if self.entity_in_constrain_map(entity):
            return len(self.constraint_map[entity]) != 0
        else:
            return False


if __name__ == "__main__":
    dg = DataConstraintGenerator()
    # dg.setup_constraint_map()
    pretty_print = pprint.PrettyPrinter(indent=2)
    pretty_print.pprint(dg.constraint_map)
    print(json.dumps(dg.constraint_map, indent=3))
    # print(dg.constraint_map['Company']['rankings'][4])
    print(dg.generate_data_instances('Company'))

