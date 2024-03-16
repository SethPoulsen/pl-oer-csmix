import random
from itertools import combinations
import math

# size of joined tables
# T(R)T(S)/(product of max's of shared attributes)

# cost = sum of sizes of intermediates


class Table:
    def __init__(self, name, size, cost, uniques, plan=""):
        self.name = name
        self.size = size
        self.cost = cost
        self.uniques = uniques
        if plan == "":
            self.plan = self.name
        else:
            self.plan = plan

    def __str__(self) -> str:
        return self.name + " " + str(self.size) + " " + str(self.cost) + " " + str(self.uniques) + " " + self.plan

def join_tables(a,b):
        table = {}
        interset = set(a.uniques.keys()).intersection(b.uniques.keys())
        for x in a.uniques.keys()-interset:
            table[x]=a.uniques[x]
        for x in b.uniques.keys()-interset:
            table[x]=b.uniques[x]
        size = a.size*b.size
        for x in interset:
            size/=max(a.uniques[x],b.uniques[x])
            table[x]=min(a.uniques[x],b.uniques[x])
        return Table(f"{a.name}{b.name}",size,a.size+b.size+a.cost+b.cost,table,joined=(a,b))


attributes = "wxyz"
tables = {'A': Table("A", random.randint(1000, 10000), 0, {'w': random.randint(30, 100), 'y': random.randint(20, 100), 'z': random.randint(20, 100)}),
          'B': Table("B", random.randint(1000, 10000), 0, {'w': random.randint(20, 100), 'x': random.randint(20, 100)}),
          'C': Table("C", random.randint(1000, 10000), 0, {'w': random.randint(20, 100), 'x': random.randint(20, 100), 'z': random.randint(20, 100)}),
          'D': Table("D", random.randint(1000, 10000), 0, {'w': random.randint(20, 100), 'x': random.randint(20, 100), 'y': random.randint(20, 100), 'z': random.randint(20, 100)}),
          }

def join_tables(a: Table, b: Table, begin):
    table = {}
    intersect = set(a.uniques.keys()).intersection(b.uniques.keys())
    for x in a.uniques.keys() - intersect:
        table[x] = a.uniques[x]
    for x in b.uniques.keys() - intersect:
        table[x] = b.uniques[x]
    size = a.size * b.size
    for x in intersect:
        size /= max(a.uniques[x], b.uniques[x])
        table[x] = min(a.uniques[x], b.uniques[x])
    if len(begin) == 2:
        return Table(begin, size, 0, table, plan=f"{a.plan}{b.plan}")
    else:
        aSize = 0 if len(a.name) == 1 else a.size
        bSize = 0 if len(b.name) == 1 else b.size
        return Table(begin, size, aSize + bSize + a.cost + b.cost, table, plan=f"{a.plan}{b.plan}")

def generate(data):
    tablehtml = "<table border=\"1\"><tr>"   # Generate table HTML
    for x in tables:
        tablehtml += f"<th>{x}({','.join(tables[x].uniques)})</th>"
    tablehtml += "</tr><tr>"
    for x in tables:
        tablehtml += f"<td style=\"border: 1px solid black;\">T({x})={tables[x].size}</td>"
    tablehtml += "</tr>"
    for x in attributes:
        tablehtml += "<tr>"
        for y in tables:
            if x in tables[y].uniques:
                tablehtml += f"<td style=\"border: 1px solid black;\">V({y},{x})={tables[y].uniques[x]}</td>"
            else:
                tablehtml += "<td></td>"
        tablehtml += "</tr>"
    tablehtml += "</table>"
    data["params"]["table"] = tablehtml


    # Iterate through all intermediate joins
    intermediate_joins = ['AB', 'AC', 'AD', 'BC', 'BD', 'CD']
    for join in intermediate_joins:
        if (tables[join[0]].size <= tables[join[1]].size):
            acc = join_tables(tables[join[0]], tables[join[1]], join)
        else:
            acc = join_tables(tables[join[1]], tables[join[0]], join)
        acc.size = math.ceil(acc.size)
        tables[join] = acc


    for join in intermediate_joins:
        data["correct_answers"]["size_{}".format(join)]=str(tables[join].size)
        #data["correct_answers"]["cost_{}".format(join)]=str(answer[0])
        #data["correct_answers"]["joinorder_{}".format(join)]="".join(answer[1].name)
    
    intermediate_joins = ['ABC', 'ABD', 'ACD', 'BCD']
    temp_t = []
    for join in intermediate_joins:
        smallest_cost = float("inf")
        optimal_plan = None
        
        t1 = join_tables(tables[join[:2]], tables[join[-1]], join)
        t1.size = math.ceil(t1.size)
        if t1.cost < smallest_cost:
            smallest_cost = t1.cost
            optimal_plan = t1
        
        t2 = join_tables(tables[join[1:]], tables[join[0]], join)
        t2.size = math.ceil(t2.size)
        if t2.cost < smallest_cost:
            smallest_cost = t2.cost
            optimal_plan = t2
        
        t3 = join_tables(tables[join[0] + join[2]], tables[join[1]], join)
        t3.size = math.ceil(t3.size)
        if t3.cost < smallest_cost:
            smallest_cost = t3.cost
            optimal_plan = t3
        
        tables[join] = optimal_plan
        temp_t.append(optimal_plan)

    for join in intermediate_joins:
        data["correct_answers"]["size_{}".format(join)]=str(tables[join].size)
        data["correct_answers"]["cost_{}".format(join)]=str(tables[join].cost)
    
    for t in temp_t:
        name = t.name 
        plan = t.plan
        data["correct_answers"]["plan_{}".format(name)]=plan
        
    
    final_joins = ['D', 'C', 'B', 'A']
    min_cost = float("inf")
    answer = None
    for i in range(len(intermediate_joins)):
        t = join_tables(tables[intermediate_joins[i]], tables[final_joins[i]], 'ABCD')
        t.size = math.ceil(t.size)
        if t.cost < min_cost:
            min_cost = t.cost
            answer = t
    
    data["correct_answers"]["size"]=str(answer.size)
    data["correct_answers"]["cost"]=str(answer.cost)
    data["correct_answers"]["joinorder"]="".join(answer.plan)


