#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3.6.7


import json, os, re
# re the most recent and the module-level matching functions are cached
# no need to compile

from base_grader import BaseGrader


__date__ = '13:00 Tuesday Nov 14 2023'
__doc__ = '''Task 14. DB design DDL translation grader
1. support tables setup, e.g., create a table to be referenced
2. support multiple solutions
3. support grading individual items
    e.g., table name, column name, column type, primary key or foreign key.
4. support ignoring cases
5. support verbose error message configuration
6. support partial credit configuration
'''
__version__ = '3.6.7 (default, Oct 22 2018, 11:32:17)'


# instructions are in ddl_config.json
CONFIG_PATH = '/grade/tests/ddl_config.json'
SETUP_PATH = '/grade/tests/ddl_setup.sql'
SOLUTION_DIR = '/grade/tests/'
STUDENT_DIR = '/grade/run/bin/'
STUDENT_FILE = 'query.sql'

KEY_COL = 'column'
KEY_FK = 'foreign_key'
KEY_PK = 'primary_key'


def grade(solutions, student):
    # compare
    best_score = 0
    for sol in solutions:
        cmp = CompareSchema(sol, student)
        if cmp.score > best_score:
            best_score = cmp.score
            best_cmp = cmp
    return best_score, best_cmp.message, best_cmp.grade_output


def parse_schema(schema):
    '''
    'CREATE TABLE `University` (\n  `id` int(11) NOT NULL,\n  `Address` varchar(255) DEFAULT NULL,\n  `Contact` varchar(16) DEFAULT NULL,\n  PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8')
    'CREATE TABLE `Department` (\n  `id` int(11) NOT NULL,\n  `address` varchar(255) DEFAULT NULL,\n  `Contact` varchar(16) DEFAULT NULL,\n  `University_id` int(11) NOT NULL,\n  PRIMARY KEY (`id`,`University_id`),\n  KEY `University_id` (`University_id`),\n  CONSTRAINT `Department_ibfk_1` FOREIGN KEY (`University_id`) REFERENCES `University` (`id`) ON DELETE CASCADE\n) ENGINE=InnoDB DEFAULT CHARSET=utf8')

    '''
    result = {
        KEY_COL: [],
        KEY_PK: [],
        KEY_FK: [],
    }
    subpattern = r'`(?P<col>\w*)`'
    for line in schema.replace('\'','').split('\n'):
        table_name = re.search(r'CREATE TABLE `(?P<table>\w*)` ', line)
        if table_name:
            table = table_name.group('table')
            continue
        col_type = re.search(r'`(.*)` (\w*)\(*(\w*)\)* (DEFAULT NULL|NOT NULL)', line)
        if col_type:
            result[KEY_COL].append(col_type.groups())
            continue
        primary_key = re.search(r'PRIMARY KEY \((?P<key>(`\w*`,* *)*)\)', line)
        if primary_key:
            key_1d = re.findall(subpattern, primary_key.group('key'))
            result[KEY_PK].extend(key_1d)
            continue
        foreign_key = re.search(r'FOREIGN KEY \((?P<col>(`\w*`,*)+)\) REFERENCES `(?P<table>\w*)` \((?P<table_col>(`\w*`,*)*)\)', line)
        if foreign_key:
            col_1d = tuple(re.findall(subpattern, foreign_key.group('col')))
            table_col = tuple([table, col_1d])
            fk_group = foreign_key.group('table_col')
            fk_col_1d = tuple(re.findall(subpattern, fk_group))
            fk_table_col = tuple([foreign_key.group('table'), fk_col_1d])
            result[KEY_FK].append(tuple([table_col, fk_table_col]))
            continue
    return result


class CompareSchema(object):
    COLUMN_FLAGS = '#column flags'
    GRADE = '#grade'
    TABLE_FLAGS = '#table flags'
    VERBOSE = '#verbose'
    WEIGHT = '#default weight'
    W_TABLE = 'table_name'
    W_COLUMN = 'column_name'
    W_TYPE_NAME = 'column_type_name' 
    W_TYPE_SIZE = 'column_type_size'
    W_PK = 'primary_key'
    W_FK = 'foreign_key'
    def __init__(self, solution, student):
        # to calculate score
        self.weight = 0
        self.max_weight = 0
        # to show error message 
        self.result = list()
        # method
        self._load_config()
        if 'syntax' in self.config[CompareSchema.GRADE]:
            # syntax check is processed outside. skip comparing schemas
            self.message = '\n'.join([
                'Pass syntax check.',
                'This question will be manually graded.',
                'Please ignore the score at the time of submission.',
            ])
            self.grade_output = 'Pending manual grading.'
            self.score = 1
            return
        self._check_table_count(solution, student)
        self._check_table_name(solution, student)
        self._check_table_detail(solution, student)
        self._summary()

    def _check_table_count(self, solution, student):
        # check the number of tables
        result = self.result
        verbose = int(self.config[CompareSchema.VERBOSE]) % 10
        if len(solution) == len(student):
            self.match_ratio = 1
            return
        if verbose <= 0:
            pass
        elif verbose <= 1:
            result.append('Errors in tables.')
        elif verbose <= 2:
            result.append('The number of tables is wrong.')
        elif verbose <= 8:
            if len(student) < len(solution):
                result.append('Expect more tables.')
            else:
                result.append('More tables than expected.')
        elif verbose >= 9:
            pattern = 'Expect %d tables. Actual %d tables.'
            result.append(pattern % (len(solution), len(student)))
        # partial credit
        diff = len(solution) - len(student)
        if diff < 0:
            diff = 0 - diff
        max_count = max(len(solution), len(student))
        self.match_ratio = max(0, 1 - diff / max_count)

    def _check_table_detail(self, solution, student):
        # there is no way to match relationship table name
        # therefore match by table column similarity ( the best score)
        def _check_column_count(table, solution, student):
            if len(solution) == len(student):
                return
            result = self.result
            verbose = int(self.config[CompareSchema.VERBOSE] / 100) % 10
            if verbose <= 0:
                pass
            elif verbose <= 1:
                result.append('Errors in columns.')
            elif verbose <= 2:
                result.append('The number of table columns is wrong.')
            elif verbose <= 3:
                if len(student) < len(solution):
                    result.append('Expect more columns.')
                else:
                    result.append('More columns than expected.')
            elif verbose <= 6:
                result.append('Errors in table `%s` columns.' % (table))
            elif verbose <= 7:
                pattern = 'The number of table `%s` columns is wrong.'
                result.append(pattern % (table))
            elif verbose <= 8:
                if len(student) < len(solution):
                    pattern = 'Errors in table `%s`. Expect more columns.'
                    result.append(pattern % (table))
                else:
                    pattern = 'Errors in table `%s`.'
                    pattern += ' More columns than expected.'
                    result.append(pattern % (table))
            elif verbose >= 9:
                pattern = 'Errors in table `%s`.'
                pattern += ' Expect %d columns. Actual %d columns.'
                result.append(pattern % (table, len(solution), len(student)))
        def _column_name(column_name):
            # change to lower case
            if self.config[CompareSchema.COLUMN_FLAGS] & re.I:
                return column_name.lower()
            else:
                return column_name
        def _column_name_1d(iterator):
            if self.config[CompareSchema.COLUMN_FLAGS] & re.I:
                result = list()
                for x in iterator:
                    result.add(_column_name(x))
                return result
            return list(iterator)
        def _diff_column(table, solution, student):
            # difference of table columns
            solution = solution[KEY_COL]
            student = student[KEY_COL]
            _check_column_count(table, solution, student)
            _diff_column_name(table, solution, student)
            _diff_column_type_name(table, solution, student)
            _diff_column_type_size(table, solution, student)
        def _diff_column_name(table, solution, student):
            w = self._get_weight(table)
            w_col_name = w[CompareSchema.W_COLUMN]
            if not w_col_name:
                return
            # check column name
            fewer_items = _diff_column_name_set(solution, student)
            more_items = _diff_column_name_set(student, solution)
            # calculate partial credit
            fewer = len(fewer_items)
            more = len(more_items)
            mismatch = (fewer + more) / len(solution)
            match_ratio = max(0, 1 - mismatch)
            self.weight += match_ratio * len(solution) * w_col_name
            self.max_weight += len(solution) * w_col_name
            _diff_column_name_error(table, fewer_items, more_items)
        def _diff_column_name_error(table, fewer_items, more_items):
            # update error message
            if not (fewer_items or more_items):
                return
            result = self.result
            verbose = int(self.config[CompareSchema.VERBOSE] / 1000) % 10
            if verbose <= 0:
                pass
            elif verbose <= 1:
                result.append('Errors in table columns.')
            elif verbose <= 2:
                result.append('Errors in table column names.')
            elif verbose <= 6:
                pattern = 'Errors in table `%s` columns.'
                result.append(pattern % (table))
            elif verbose <= 7:
                pattern = 'Errors in table `%s` column names.'
                result.append(pattern % (table))
            elif verbose <= 8:
                fewer = len(fewer_items)
                more = len(more_items)
                pattern = 'Errors in table `%s` column names.' % (table)
                if fewer:
                    pattern += (' Missing %d column(s).' % (fewer))
                if more:
                    pattern += (' Unnecessary %d column(s).' % (more))
                result.append(pattern)
            elif verbose >= 9:
                # this almost gives the solution
                fewer = '`,`'.join(fewer_items)
                more = '`,`'.join(more_items)
                pattern = 'Errors in table `%s` column names.' % (table)
                if fewer:
                    pattern += (' Missing `%s`.' % (fewer))
                if more:
                    pattern += (' Unnecessary `%s`.' % (more))
                result.append(pattern)
        def _diff_column_name_set(a, b):
            # note a, b are list of array, each array represents one column
            # array = (column name, column type name, column type size)
            b = set(_column_name_1d(array[0] for array in b))
            items = list()
            for array in a:
                key = array[0]
                if _column_name(key) not in b:
                    items.append(key)
            return items
        def _diff_column_type_name(table, solution, student):
            w = self._get_weight(table)
            w_col_type_name = w[CompareSchema.W_TYPE_NAME]
            if not w_col_type_name:
                return
            # check column type name
            mismatch_name = list()
            for array in solution:
                key = _column_name(array[0])
                for col in student:
                    if key == _column_name(col[0]):
                        index = 1
                        if (len(array) > index) and (len(col) > index):
                            if array[index] == col[index]:
                                self.weight += w_col_type_name
                            else:
                                mismatch_name.append(key)
                        break
                if len(array) > 1:
                    self.max_weight += w_col_type_name
            _diff_column_type_name_error(table, mismatch_name)
        def _diff_column_type_name_error(table, mismatch_name):
            if not mismatch_name:
                return
            result = self.result
            verbose = int(self.config[CompareSchema.VERBOSE] / 10000) % 10
            if verbose <= 0:
                pass
            elif verbose <= 1:
                result.append('Errors in table columns.')
            elif verbose <= 2:
                result.append('Errors in table column types.')
            elif verbose <= 3:
                result.append('Errors in table column type names.')
            elif verbose <= 6:
                pattern = 'Errors in table `%s` columns.'
                result.append(pattern % (table))
            elif verbose <= 7:
                pattern = 'Errors in table `%s` column types.'
                result.append(pattern % (table))
            elif verbose <= 8:
                pattern = 'Errors in table `%s` column type names.'
                result.append(pattern % (table))
            elif verbose >= 9:
                pattern = 'Errors in table `%s` column types.'
                pattern += ' Type names of `%s`.'
                name = '`,`'.join(mismatch_name)
                result.append(pattern % (table, name))
        def _diff_column_type_size(table, solution, student):
            w = self._get_weight(table)
            w_col_type_size = w[CompareSchema.W_TYPE_SIZE]
            if not w_col_type_size:
                return
            # check column type size
            mismatch_size = list()
            for array in solution:
                key = _column_name(array[0])
                for col in student:
                    if key == _column_name(col[0]):
                        index = 2
                        if (len(array) > index) and (len(col) > index):
                            if array[index] == col[index]:
                                self.weight += w_col_type_size
                            else:
                                mismatch_size.append(key)
                        break
                if len(array) > 2:
                    # some type might not have type size
                    self.max_weight += w_col_type_size
            _diff_column_type_size_error(table, mismatch_size)
        def _diff_column_type_size_error(table, mismatch_size):
            if not mismatch_size:
                return
            result = self.result
            verbose = int(self.config[CompareSchema.VERBOSE] / 100000) % 10
            if verbose <= 0:
                pass
            elif verbose <= 1:
                result.append('Errors in table columns.')
            elif verbose <= 2:
                result.append('Errors in table column types.')
            elif verbose <= 3:
                result.append('Errors in table column type sizes.')
            elif verbose <= 6:
                pattern = 'Errors in table `%s` columns.'
                result.append(pattern % (table))
            elif verbose <= 7:
                pattern = 'Errors in table `%s` column types.'
                result.append(pattern % (table))
            elif verbose <= 8:
                pattern = 'Errors in table `%s` column type sizes.'
                result.append(pattern % (table))
            elif verbose >= 9:
                pattern = 'Errors in table `%s` column types:'
                pattern += ' type sizes of `%s`.'
                size = '`,`'.join(mismatch_size)
                result.append(pattern % (table, size))
        def _diff_fk(table, solution, student):
            w = self._get_weight(table)[CompareSchema.W_FK]
            if not w:
                return
            solution = list(solution[KEY_FK])
            student = list(student[KEY_FK])
            # match by the best score
            fewer_items = list()
            mismatch = list()
            more_items = list()
            student_table = list() # record student table name
            weight = 0
            self.max_weight += max(len(solution), len(student)) * w
            for solution_pair in solution:
                ans, ans_fk = solution_pair
                ans_table = self._table_name(ans[0])
                ans_col_1d = _column_name_1d(ans[1])
                ans_fk_table = self._table_name(ans_fk[0])
                ans_fk_col_1d = _column_name_1d(ans_fk[1])
                ans_map = _fk_map(ans_col_1d, ans_fk_col_1d)
                best_score = 0
                best_index = 0
                index = 0
                for a, b in student:
                    a_table = self._table_name(a[0])
                    a_col_1d = _column_name_1d(a[1])
                    fk_table = self._table_name(b[0])
                    fk_col_1d = _column_name_1d(b[1])
                    student_table.append(a_table)
                    a_map = _fk_map(a_col_1d, fk_col_1d)
                    score = 0
                    if _match_table_name(ans_table, a_table):
                        score += 1
                    if _match_table_name(ans_fk_table, fk_table):
                        score += 1
                    score += _fk_match(ans_map, a_map)
                    if score > best_score:
                        best_score = score
                        best_index = index
                    index += 1
                if best_score:
                    # find something match
                    a, b = student.pop(best_index)
                    total_score = 2 + len(ans_col_1d)
                    self.weight += best_score / total_score * w
                    if best_score < total_score:
                        mismatch.append(tuple(b))
                else:
                    fewer_items.append(tuple(ans_fk))
            for a, b in student:
                student_table.append(a[0])
                more_items.append(tuple(b))
            if student_table:
                # set table name to student table if exists
                table = student_table[0]
            _diff_fk_error(table, fewer_items, mismatch, more_items)
        def _diff_fk_error(table, fewer_items, mismatch, more_items):
            if not (fewer_items or mismatch or more_items):
                return
            result = self.result
            verbose = int(self.config[CompareSchema.VERBOSE] / 10000000) % 10
            '''
            Note: due to greedy partial credits awarding, the same foreign key
            can be reported more than once if it
            partially matches the solution foreign key `X` and
            exactly matches the solution foreign key `Y`.
            The missing solution foreign key is `X` but cannot be identified.
            '''
            insufficient = set(fewer_items) & set(mismatch)
            fewer_items = _remove_item(fewer_items, insufficient)
            mismatch = _remove_item(mismatch, insufficient)
            if verbose <= 0:
                pass
            elif verbose <= 1:
                pattern = 'Errors in foreign keys.'
                result.append(pattern)
            elif verbose <= 4:
                pattern = 'Errors in foreign keys:'
                if fewer_items or insufficient:
                    pattern += (' Missing references.')
                if mismatch:
                    pattern += (' Mismatch references.')
                if more_items:
                    pattern += (' Unexpected references.')
            elif verbose <= 5:
                pattern = 'Errors in table `%s` foreign keys.' % (table)
                result.append(pattern)
            elif verbose <= 6:
                pattern = 'Errors in table `%s` foreign keys.' % (table)
                if fewer_items or insufficient:
                    pattern += (' Missing references.')
                if mismatch:
                    pattern += (' Mismatch references.')
                if more_items:
                    pattern += (' Unexpected references.')
                result.append(pattern)
            elif verbose <= 7:
                pattern = 'Errors in table `%s` foreign keys.' % (table)
                items = max(len(fewer_items), len(insufficient))
                if items:
                    pattern += (' Missing %d references.' % (items))
                items = len(mismatch)
                if items:
                    pattern += (' Mismatch %d references.' % (items))
                items = len(more_items)
                if items:
                    pattern += (' Unexpected %d references.' % (items))
                result.append(pattern)
                result.append(explanation)
            elif verbose <= 8:
                pattern = 'Errors in table `%s` foreign keys.' % (table)
                items = '`,`'.join(x[0] for x in fewer_items)
                if items:
                    pattern += (' Missing references to `%s`.' % (items))
                items = '`,`'.join(x[0] for x in mismatch)
                if items:
                    pattern += (' Mismatch references to `%s`.' % (items))
                items = '`,`'.join(x[0] for x in more_items)
                if items:
                    pattern += (' Unexpected references to `%s`.' % (items))
                if insufficient:
                    pattern += (' Expect more references.')
                result.append(pattern)
                result.append(explanation)
            elif verbose >= 9:
                pattern = 'Errors in table `%s` foreign keys.' % (table)
                fk = list()
                for x in fewer_items:
                    fk.append('`%s`(`%s`)' % (x[0], '`,`'.join(x[1])))
                items = ','.join(fk)
                if items:
                    pattern += (' Missing references to %s.' % (items))
                fk = list()
                for x in mismatch:
                    fk.append('`%s`(`%s`)' % (x[0], '`,`'.join(x[1])))
                items = ','.join(fk)
                if items:
                    pattern += (' Mismatch references to %s.' % (items))
                fk = list()
                for x in more_items:
                    fk.append('`%s`(`%s`)' % (x[0], '`,`'.join(x[1])))
                items = ','.join(fk)
                if items:
                    pattern += (' Unexpected references to %s.' % (items))
                if insufficient:
                    pattern += (' Expect more references.')
                result.append(pattern)
        def _diff_pk(table, solution, student):
            w = self._get_weight(table)[CompareSchema.W_PK]
            if not w:
                return
            solution_pk = set(_column_name_1d(solution[KEY_PK]))
            student_pk = set(_column_name_1d(student[KEY_PK]))
            fewer_items = list(x for x in solution_pk if x not in student_pk)
            more_items = list(x for x in student_pk if x not in solution_pk)
            # calculate partial credit
            count = len(solution_pk)
            if count:
                self.max_weight += count * w
                mismatch_ratio = (len(fewer_items) + len(more_items)) / count
            elif len(student_pk):
                self.max_weight += len(student_pk) * w
                mismatch_ratio = 1
            else:
                mismatch_ratio = 0
            match_ratio = max(0, 1 - mismatch_ratio)
            self.weight += (w * count * match_ratio)
            _diff_pk_error(table, fewer_items, more_items)
        def _diff_pk_error(table, fewer_items, more_items):
            # update error message
            if not (fewer_items or more_items):
                return
            result = self.result
            verbose = int(self.config[CompareSchema.VERBOSE] / 1000000) % 10
            if verbose <= 0:
                pass
            if verbose <= 1:
                result.append('Errors in table primary key.')
            elif verbose <= 7:
                pattern = 'Errors in table `%s` primary key.'
                result.append(pattern % (table))
            elif verbose <= 8:
                fewer = len(fewer_items)
                more = len(more_items)
                pattern = 'Errors in table `%s` primary key.' % (table)
                if fewer:
                    pattern += (' Missing %d column(s).' % (fewer))
                if more:
                    pattern += (' Unnecessary %d column(s).' % (more))
                result.append(pattern)
            elif verbose >= 9:
                fewer = '`,`'.join(fewer_items)
                more = '`,`'.join(more_items)
                pattern = 'Errors in table `%s` primary key.' % (table)
                if fewer:
                    pattern += (' Missing columns `%s`.' % (fewer))
                if more:
                    pattern += (' Unnecessary columns `%s`.' % (more))
                result.append(pattern)
        def _fk_map(col_1d, fk_col_1d):
            # perform name conversion
            w = self._get_weight(table)
            w_col_name = w[CompareSchema.W_COLUMN]
            result = dict()
            for index in range(len(col_1d)):
                if w_col_name:
                    key = _column_name(col_1d[index])
                    value = _column_name(fk_col_1d[index])
                else:
                    # column name is not graded, then change to lower
                    key = col_1d[index].lower()
                    value = fk_col_1d[index].lower()
                result[key] = value
            return result
        def _fk_match(solution, student):
            # return the number of match
            counter = 0
            for key, value in solution.items():
                if (key in student) and (value == student[key]):
                    counter += 1
            return counter
        def _get_match_table_name(table, student):
            for name in student:
                if _match_table_name(table, name):
                    return name
            return ''
        def _match_table_name(table, name):
            if self._ignore_table_name(table):
                if table.lower() == name.lower():
                    return name
            if self._table_name(table) == self._table_name(name):
                return name
            return ''
        def _match_schema(table, solution, student):
            # note solution, student are schema
            weight = self._get_weight(table)
            if not sum(weight.values()):
                return
            _diff_column(table, solution, student)
            _diff_pk(table, solution, student)
            _diff_fk(table, solution, student)
        def _remove_item(a, b):
            result = list()
            b = set(b)
            for item in a:
                if item not in b:
                    result.append(item)
            return result
        # make a copy because this delete keys to avoid double match
        solution = dict(solution)
        student = dict(student)
        # the first pass, check tables that match names
        for table in list(solution):
            student_key = _get_match_table_name(table, student)
            if student_key:
                solution_value = solution[table]
                del solution[table]
                student_value = student[student_key]
                del student[student_key]
                _match_schema(table, solution_value, student_value)
        # the second pass, by best score, greedy
        for table in list(solution):
            solution_value = solution[table]
            best_key = ''
            best_score = 0
            diff = list()
            result = list(self.result)
            for student_key, student_value in student.items():
                # record
                weight_before = self.weight
                max_weight_before = self.max_weight
                _match_schema(table, solution_value, student_value)
                weight_diff = self.weight - weight_before
                max_weight_diff = self.weight - max_weight_before
                # restore
                self.weight = weight_before
                self.max_weight = max_weight_before
                # find the best
                if max_weight_diff:
                    score =  weight_diff / max_weight_diff
                else:
                    score = 0
                if score > best_score:
                    best_key = student_key
                    best_score = score
                    diff = [weight_diff, max_weight_diff]
            # apply the best score
            if best_key:
                del student[best_key]
                self.weight += diff[0]
                self.max_weight += diff[1]
                self.result = result

    def _check_table_name(self, solution, student):
        if not len(solution):
            return
        verbose = (self.config[CompareSchema.VERBOSE] / 10) % 10
        def _diff(a, b):
            # difference of table names
            b = _table_name_set(b)
            items = list()
            for table in a:
                if self._ignore_table_name(table):
                    continue
                if self._table_name(table) not in b:
                    items.append(table)
            return items
        def _diff_error(fewer_items, more_items):
            if not (fewer_items or more_items):
                return
            # update error message
            if verbose <= 0:
                pass
            elif verbose <= 8:
                fewer = len(fewer_items)
                more = len(more_items)
                pattern = 'Missing %d table(s). Unnecessary %d table(s).'
                self.result.append(pattern % (fewer, more))
            elif verbose == 9:
                fewer = '`,`'.join(fewer_items)
                more = '`,`'.join(more_items)
                pattern = 'Missing tables `%s`. Unnecessary tables `%s`.'
                self.result.append(pattern % (fewer, more))
        def _table_name_set(iterator):
            if self.config[CompareSchema.TABLE_FLAGS] & re.I:
                result = set()
                for x in iterator:
                    result.add(self._table_name(x))
                return result
            return set(iterator)
        fewer_items = _diff(solution, student)
        more_items = _diff(student, solution)
        _diff_error(fewer_items, more_items)
        # calculate partial credit
        max_weight = 0
        weight = 0
        for table in solution:
            w = self._get_weight(table)[CompareSchema.W_TABLE]
            max_weight += w
            if table not in fewer_items:
                weight += w
        if not max_weight:
            max_weight = len(more_items)
        fewer = len(fewer_items)
        more = len(more_items)
        mismatch_ratio = (fewer + more) / len(solution)
        match_ratio = max(0, 1 - mismatch_ratio)
        self.weight += weight * match_ratio
        self.max_weight += max_weight

    def _get_weight(self, table):
        if table in self.config:
            return self.config[table]
        return self.config[CompareSchema.WEIGHT]

    def _ignore_table_name(self, table_name):
        # does not require table name match
        key = CompareSchema.W_TABLE
        if table_name in self.config:
            return self.config[table_name][key] == 0
        return self.config[CompareSchema.WEIGHT][key] == 0

    def _load_config(self):
        def _get_flag(flags):
            flag = 0
            for x in flags:
                flag |= eval(x)
            return flag
        # load configuration
        self.config = dict()
        if os.path.isfile(CONFIG_PATH):
            with open(CONFIG_PATH, 'r', encoding='utf-8') as r:
                self.config = json.load(r)
        # set default values
        for key in [CompareSchema.TABLE_FLAGS, CompareSchema.COLUMN_FLAGS]:
            if key not in self.config:
                self.config[key] = list()
            self.config[key] = _get_flag(self.config[key])
        if CompareSchema.WEIGHT not in self.config:
            self.config[CompareSchema.WEIGHT] = {
                CompareSchema.W_TABLE: 0,
                CompareSchema.W_COLUMN: 1,
                CompareSchema.W_TYPE_NAME: 0,
                CompareSchema.W_TYPE_SIZE: 0,
                CompareSchema.W_PK: 2,
                CompareSchema.W_FK: 2,
            }
        if CompareSchema.GRADE not in self.config:
            self.config[CompareSchema.GRADE] = ['syntax']
        if CompareSchema.VERBOSE in self.config:
            self.config[CompareSchema.VERBOSE] = int(self.config[CompareSchema.VERBOSE])
        else:
            self.config[CompareSchema.VERBOSE] = 0

    def _summary(self):
        # summarize grade result
        # message is general output message
        # grade_output for each test case if there are any errors.
        if self.max_weight:
            self.score = (self.weight / self.max_weight) * self.match_ratio
        else:
            self.score = 1
        if self.score == 1:
            self.message = BaseGrader.TEST_CORRECT_MESSAGE
            self.grade_output = ''
        else:
            self.message = ''
            if self.result:
                self.grade_output = '\n'.join(self.result)
            else:
                # default: hide error details
                self.grade_output = BaseGrader.TEST_INCORRECT_MESSAGE

    def _table_name(self, table_name):
        # change to lower case
        if self.config[CompareSchema.TABLE_FLAGS] & re.I:
            return table_name.lower()
        else:
            return table_name
