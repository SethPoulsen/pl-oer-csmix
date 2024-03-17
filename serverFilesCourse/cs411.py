import itertools
import functools
import random
import math
import collections

def generate_fds(n,entities,cardinality):
	"""
	n: how many unique, random functional dependencies to make
	entities: set of things we can interrelate
	cardinality: how many hypotheses the fd's have.
	"""
	
	if (cardinality>=len(entities)):
		raise ValueError("will not generate a functional dependency that depends on as many things as there are.")
	
	# prairielearn uses python 3.6.9, which doesn't have math.comb. awkward.
	#tot_combs = math.comb(len(entities),cardinality)
	
	# i know, it would be more efficient to do this in a loop than using the math-factorial function.
	# but this looks nice.
	tot_combs = math.factorial(len(entities))//(math.factorial(len(entities)-cardinality)*math.factorial(cardinality))
	
	
	indices = sorted(random.sample(range(tot_combs),n))
	fds = {}
	for i,c in enumerate(itertools.combinations(entities,cardinality)):
		if (i==indices[0]):
			indices = indices[1:]
			fds[c] = [random.choice(list(set(entities)-set(c)))]
			if (len(indices)==0):
				break
	return fds


def get_closure(fds,known):
	"""
	given a dictionary of functional dependencies, generate the closure based on which we have already found.
	"""
	known = set(known) # let's not overwrite the list we were given, also make it a set if we weren't passed one. two birds one stone.
	worked = True
	while worked:
		worked = False
		for fd in fds:
			if (all([x in known for x in fd])):
				t = len(known)
				known.update(fds[fd])
				if (len(known)!=t): # we learned something!
					worked = True
	return known




def get_candidate_keys(alphabet,fds):
	""" finds all candidate keys """
	return set(get_candidate_keys_helper(set(alphabet),fds,sorted(alphabet)))

def get_candidate_keys_helper(alphabet,fds,candidate):
	"""
	the recursive portion of the candidate key generator
	
	We start with the trivial key, the entire relation.
	Then we try removing parts of it and checking if it's still a key.
	If it is, recurse. If no part of it can be removed, then it's a candidate key.
	"""
	simplest = True
	for x in range(len(candidate)):
		k = candidate[:x]+candidate[x+1:]
		if (get_closure(fds,k)==alphabet):
			simplest = False
			yield from get_candidate_keys_helper(alphabet,fds,k)
	if (simplest):
		yield "".join(sorted(candidate))



def fds_to_singletons(fds):
	for fd in fds:
		for x in fds[fd]:
			yield [fd,x]

def singletons_to_fds(sing):
	fds = {}
	for s in sing:
		if s[0] in fds:
			fds[s[0]]=list(set(fds[s[0]]).union(s[1]))
		else:
			fds[s[0]]=s[1]
	return fds

""" MINIMAL BASIS STUFF"""

def minimize_lhs(relation,fds):
	""" one shot left hand side minimization """
	fdlist = list(fds_to_singletons(fds))
	checker = fd_equivalence_checker(relation,fds)
	return singletons_to_fds(minimize_lhs_helper(checker,fdlist))

def minimize_lhs_helper(checker,fdlist): # TODO: this is not very efficient, but it runs very rarely due to length condition!
	for fd in fdlist:
		if (len(fd[0])>1):
			for x in range(len(fd[0])):
				tmp = fdlist.copy()
				tmp.remove(fd)
				tmp.append([fd[0][:x]+fd[0][x+1:],fd[1]])
				if (checker(singletons_to_fds(tmp))):
					return minimize_lhs_helper(checker,tmp)
	return fdlist

def minimize_helper(relation,fds,checker): # one-shot version of minimal_bases, very fast.
	""" one shot rhs minimizer """
	for fd in fds:
		for x in range(len(fds[fd])):
			tmp = fds.copy()
			tmp[fd]=fds[fd][:x]+fds[fd][x+1:]
			if (len(tmp[fd])==0):
				del tmp[fd]
			if (checker(tmp)):
				return minimize_helper(relation,tmp,checker)
	return fds

def minimize(relation,fds):
	""" one shot full minimization"""
	checker = fd_equivalence_checker(relation,fds)
	fds = minimize_lhs(relation,fds) # minimize left hand side
	return minimize_helper(relation,fds,checker) # minimize right hand side

def is_minimal_lhs(relation,fds):
	""" are the left hand sides minimal? """
	fdlist = list(fds_to_singletons(fds))
	checker = fd_equivalence_checker(relation,fds)
	return is_minimal_lhs_helper(checker,fdlist)

def is_minimal_lhs_helper(checker,fdlist): # TODO: this is not very efficient, but it runs very rarely due to length condition!
	for fd in fdlist:
		if (len(fd[0])>1):
			for x in range(len(fd[0])):
				tmp = fdlist.copy()
				tmp.remove(fd)
				tmp.append([fd[0][:x]+fd[0][x+1:],fd[1]])
				if (checker(singletons_to_fds(tmp))):
					return False
	return True

def is_minimal_rhs(relation,fds):
	""" are the right hand sides minimal? """
	checker = fd_equivalence_checker(relation,fds)
	for fd in fds:
		for x in range(len(fds[fd])):
			tmp = fds.copy()
			tmp[fd]=fds[fd][:x]+fds[fd][x+1:]
			if (checker(tmp)):
				return False
	return True

def is_minimal(relation,fds):
	return is_minimal_lhs(relation,fds) and is_minimal_rhs(relation,fds)


def minimal_bases_lhs(relation,fds):
	""" one shot left hand side minimization """
	fdlist = list(fds_to_singletons(fds))
	checker = fd_equivalence_checker(relation,fds)
	yield from minimal_bases_lhs_helper(checker,fdlist)

def minimal_bases_lhs_helper(checker,fdlist): # TODO: this is not very efficient, but it runs very rarely due to length condition!
	yielded = False
	for fd in fdlist:
		if (len(fd[0])>1):
			for x in range(len(fd[0])):
				tmp = fdlist.copy()
				tmp.remove(fd)
				tmp.append([fd[0][:x]+fd[0][x+1:],fd[1]])
				if (checker(singletons_to_fds(tmp))):
					yielded = True
					yield from minimal_bases_lhs_helper(checker,tmp)
	if (not yielded):
		yield singletons_to_fds(fdlist)
	

def minimal_bases_rhs(relation,fds,maxdep=None): 
	""" expensive algorithm that attempts to find ALL minimal bases that can be found by further minimizing the right hand sides of what you have entered. """
	fdlist = []
	for fd in fds:
		for x in fds[fd]:
			fdlist.append((fd,x))
	checker = fd_equivalence_checker(relation,fds)
	yield from minimal_bases_rhs_helper(relation,fdlist,set(),[],checker,maxdep)

# redo
def minimal_bases_rhs_helper(relation,fdlist,baddies,candidate,checker,maxdep):
	myindex = sum(2**c for c in candidate)
	if (myindex in baddies):
		return
	fds = {}
	for fd in candidate:
		fds[fdlist[fd][0]] = fds.get(fdlist[fd][0],"") + fdlist[fd][1]
	if (not is_minimal(relation,fds)):
		baddies.add(myindex)
		return
	if (checker(fds)):
		# got one
		yield fds
		baddies.add(myindex)
		return
	else:
		# recursive case
		
		for addition in set(range(len(fdlist)))-set(candidate):
			tmp = candidate.copy()
			tmp.append(addition)
			yield from minimal_bases_rhs_helper(relation,fdlist,baddies,tmp,checker,maxdep)


# TODO: scrub lim from the entirety of this project. it was a bad design choice!
def minimal_bases(relation,fds,lim=None):
	""" takes a relation and fds, produces a generator of all minimal basis that can be produced by further minimization of the initial fds. """
	lhmins = minimal_bases_lhs(relation,fds)
	for x in lhmins:
		yield from minimal_bases_rhs(relation,x,lim)

def project(relation,fds):
	""" takes some fds, and projects them down to a smaller relation. returns a minimal basis."""
	newfds = {}
	for l in range(len(relation)):
		 for x in itertools.combinations(relation,l):
		 	x = set(x)
		 	c = set([e for e in get_closure(fds,x) if (not e in x) and e in relation])
		 	if (len(c)>0): # possible non-trivial fd
		 		newfds[tuple(sorted(x))] = sorted(c)
	return minimize(relation,newfds)

def print_fds(fds):
	"""takes a dictionary of fds and parses them to a string, which is always ordered the same regardless of the internal ordering of the data structure"""
	return ";".join(sorted(["".join(sorted(x))+"->"+"".join(sorted(fds[x])) for x in fds]))

def parse_fds(fds):
	""" parses user provided fds (a string)"""
	if (fds[-1]==";"): # remove trailing ';'.
		fds = fds[:-1]
	acc = {}
	for l in fds.split(";"):
		l = l.replace(" ","")
		l = l.split("->")
		if (len(l)!=2):
			raise ValueError("Malformed fds, check your syntax!") # you should catch this if you ever run this function on user provided fd's
		key = tuple(sorted(l[0]))
		if (key in acc):
			# need to merge entries
			acc[key] = sorted(set(acc[key]).union(set(sorted(l[1]))))
		else:
			acc[key] = sorted(l[1])
	return acc


def nontrivial_fds(relation,fds,lim=None):
	""" turns a set of fds into a list of all nontrivial fds implied by that set, useful for checking if two sets of fds are equivalent (imply each other).
        """
	if (lim is None):
        	lim = len(relation)
	newfds = {}
	for l in range(lim):
		 for x in itertools.combinations(relation,l):
		 	x = set(x)
		 	c = set([e for e in get_closure(fds,x) if (not e in x) and e in relation])
		 	if (len(c)>0):
		 		newfds[tuple(sorted(x))] = sorted(c)
	return newfds


def fd_equivalence_checker(relation,fds1): # a much faster way to compare sets of fds than ALL NONTRIVIALS.
	nontrivials = nontrivial_fds(relation,fds1)
	def inner(fds2):
		lim = 1+max(len(x) for x in itertools.chain(fds1.keys(),fds2.keys()))
		for l in range(lim):
			for x in itertools.combinations(relation,l):
				c = set([e for e in get_closure(fds2,x) if (not e in x) and e in relation])
				if (len(c)>0):
					if (not x in nontrivials.keys()):
						return False
					if (set(nontrivials[x])!=c):
						return False
				else:
					if (x in nontrivials.keys()):
						return False
		return True
	return inner

def is_bcnf(relation,fds):
	for fd in fds:
		if (set(get_closure(fds,fd))!=set(relation)):
			# a nontrivial fd? whose determinant isn't a candidate key? illegal.
			return False
	return True



def parse_relations(rels):
	if (rels[-1]==";"):
		rels = rels[:-1] # i make this mistake a lot, students might too.
	rels = rels.replace(" ","").split(";")
	acc = {}
	for r in rels:
		name = r[0]
		r = r[2:-1] # rip names and parentheses
		acc[name]="".join(r.split(","))
	return acc


def bcnf_decompose(relation,fds,lim=None):
	cache = {}
	out = list(set([tuple(x) for x in bcnf_decompose_helper(relation,fds,cache,lim,top=True)]))
	return out

def bcnf_decompose_helper(relation,raw_fds,cache,lim=None,top=False): # a potentially suboptimal bcnf implementation
	relation = "".join(sorted(relation))
	if (relation in cache):
		yield from cache[relation]
		return
	else:
		#print("thinking about", relation)
		pass
	oneway = True
	for fds in ([raw_fds] if top else minimal_bases(relation,nontrivial_fds(relation,raw_fds,lim),lim)):
		for fd in fds:
			closure = set(get_closure(fds,fd))
			if (closure!=set(relation)):
				way = list()
				# a nontrivial fd? whose determinant isn't a key? time to split
				R = list((set(relation)-closure).union(fd))
				S = list(closure)
				Sfds = project(S,fds)
				Rfds = project(R,fds)
				#print(fd,R,S)
				if (is_bcnf(S,Sfds)):
					RS = ["".join(S)]
				else:
					RS = bcnf_decompose_helper(S,Sfds,cache)
				if (is_bcnf(R,Rfds)):
					RR = ["".join(R)]
				else:
					RR = bcnf_decompose_helper(R,Rfds,cache)
				#print("**run**")
				#print("destructed tables:",R,S)
				#print(RR,RS)
				out = itertools.product(RS,RR)
				for x in out:
					acc = []
					for i in x:
						if (type(i)==list):
							acc=acc+list(i)
						else:
							acc.append(i)
					if (relation in cache):
						cache[relation].append(acc)
					else:
						cache[relation]=[acc]
					yield acc
				oneway=False
	if (oneway):
		cache[relation]= ["".join(relation)]
		yield ["".join(relation)]


def decompose_3nf(relation,fds,lim=None): # returns all possible decomps, may return some duplicate decomps
	for mfds in minimal_bases(relation,fds,lim): 
		tables = set()
		for fd in mfds:
			tables.add("".join(sorted(set(mfds[fd]).union(set(fd)))))
		tables = list(tables) # output expects a table
		# ok, but is one of our tables a superkey?
		candidates = get_candidate_keys(relation,fds)
		for check in itertools.product(tables,candidates):
			if (set(check[1]).issubset(set(check[0]))):
				yield tables
				break
		else:
			# we get a different decomp depending on which candidate we pick
			# so yield em all
			for x in candidates:
				yield tables+[x]

if __name__=="__main__":
	# tests !
	
	alphabet = set("ABCDEF")
	fds = {("A",):("B",),("B",):("C",),("C","B"):("E","F","D")}
	
	# test get_closure
	
	assert(get_closure(fds,"A")==alphabet)
	assert(get_closure(fds,"F")==set("F"))
	assert(get_closure(fds,"B")==set("BCEFD"))
	
	# test candidate keying
	assert(get_candidate_keys(alphabet,fds)==set(["A"]))
	
	fds = {("A",):("B",),("B",):("A",)}
	
	assert(get_candidate_keys("AB",fds)==set(["A","B"]))
	
	assert(get_candidate_keys("ABCD",{})==set(["ABCD"]))

	# test fds_equivalent
	a = {("A",):("B","C"),("C",):("A",),("B",):("A",)}
	b = {("A",):("B",),("B",):("C",),("C",):("A",)}
	assert(nontrivial_fds("ABC",a)==nontrivial_fds("ABC",b))
	
	c = {("A",):("B",),("B",):("C",)}
	
	assert(nontrivial_fds("ABC",a)!=nontrivial_fds("ABC",c))
	assert(nontrivial_fds("ABC",c)!=nontrivial_fds("ABC",b))
	
	assert(parse_relations("S(A,B,C)")=={"S":"ABC"})
	assert(parse_relations("A(A,B,C);B(D,F,G)")=={"A":"ABC","B":"DFG"})

	# test is_bcnf
	assert(not is_bcnf("ABC",{"A":"B","B":"C"}))
	assert(is_bcnf("ABC",{}))
	assert(is_bcnf("ABC",{"AB":"C"}))
	assert(is_bcnf("ABC",{"A":"BC"}))
	assert(not is_bcnf("ABCD",parse_fds("ABC->D;BCD->A;A->D")))
	print("passed basic FD sanity checks")
	import sys
	# advanced sanity tests
	for x in range(50):
		sys.stdout.write(".")
		sys.stdout.flush()
		relation = "ABCDEF"
		fds = generate_fds(3,relation,1)
		fds.update(generate_fds(2,relation,2))
		checker = fd_equivalence_checker(relation,fds)
		assert(checker(singletons_to_fds(fds_to_singletons(fds)))) # should be lossless
		mfds = list(minimal_bases(relation,fds))
		mfd = minimize(relation,fds)
		assert(print_fds(mfd) in [print_fds(x) for x in mfds])
		for x in mfds:
			assert(nontrivial_fds(relation,x)==nontrivial_fds(relation,fds))
			assert(is_minimal(relation,x))
	print("passed advanced FD sanity checks")

""" TRANSACTION STUFF """

# cheap, fast, easy enums
READ = 0
WRITE = 1
UNLOCKED = 2
SLOCK = 3
XLOCK = 4
RELEASE = 5
COMMIT = 6
DENIED = 7
WAIT = 8
ABORT = 9

READ_UNCOMMITTED = 0
READ_COMMITTED = 1
REPEATABLE_READ = 2
TWO_PHASE = 3
STRICT_TWO_PHASE = 2 # s2pl is just repeatable read, isn't it...

# read uncommitted allows queries in the transaction to read data without acquiring any lock, but threads in read uncommitted CANNOT WRITE
# read committed required a read-lock, but releases lock right after read. exclusive locks must be obtained for updates and held to the end of transaction.
# repeatable read places shared locks on tuples retrieved by queries, holds them until the end of the transaction. holds write locks until end of transactions, too.
# serializable is repeatable but also locks the indiex.

class action():
	__slots__ = ["attribute","thread","type"]
	def __init__(self,thread,t,attribute=None):
		self.thread=thread
		self.type=t
		self.attribute=attribute
	def __repr__(self):
		funcs = {SLOCK:"S",XLOCK:"X",WRITE:"W",READ:"R",RELEASE:"REL",COMMIT:"COMMIT",WAIT:"WAIT",DENIED:"DENIED",ABORT:"ABORT"}
		return f"{funcs[self.type]}{self.thread}({','.join(sorted(self.attribute))})"

def generate_schedule(relation,transactions,length):
	schedule = []
	for x in range(length):
		schedule.append(action(random.randint(1,transactions),random.choice((READ,WRITE)),random.choice(relation)))
	return schedule

# rules for conflict serializability swapping
# 1. can't swap two actions with same thread
# 2. can't swap read/write, write/read, write/write to same attributes

# precedence graph has no cycles

def read_uncommitted_scheduler(relation,schedule,thread):
	yield from schedule # we never make or release locks...

def read_committed_scheduler(relation,schedule,thread):
	locks = {k:UNLOCKED for k in relation}
	accumulator = []
	for a in schedule:
		if (len(accumulator)>0):
			yield accumulator
			accumulator = []
		if (a.type==READ):
			if (locks[a.attribute]==UNLOCKED):
				accumulator = [action(thread,SLOCK,a.attribute),a,action(thread,RELEASE,a.attribute)]
			else: # ok, so we already have an exclusive lock
				accumulator = [a]
		elif (a.type==WRITE):
			accumulator = []
			if (locks[a.attribute]==UNLOCKED):
				accumulator.append(action(thread,XLOCK,a.attribute))
			accumulator.append(a)
			locks[a.attribute]=XLOCK
	# ok now we can release our xlocks
	torelease = []
	for x in relation:
		if (locks[x]==XLOCK):
			accumulator.append(action(thread,RELEASE,x))
	yield accumulator

def repeatable_read_scheduler(relation,schedule,thread):
	locks = {k:UNLOCKED for k in relation}
	accumulator = []
	for a in schedule:
		if (len(accumulator)>0):
			yield accumulator
			accumulator = []
		if (a.type==READ):
			if (locks[a.attribute]!=UNLOCKED):
				accumulator = [a]
			else:
				accumulator = [action(thread,SLOCK,a.attribute),a]
				locks[a.attribute]=SLOCK
		elif (a.type==WRITE):
			if (locks[a.attribute]==XLOCK):
				accumulator = [a]
			else:
				accumulator = [action(thread,XLOCK,a.attribute),a]
				locks[a.attribute]=XLOCK
	for x in relation:
		if (locks[x] != UNLOCKED):
			accumulator.append(action(thread,RELEASE,x))
	yield accumulator

def two_phase_locking_scheduler(relation,schedule,thread,downgrade=True):
	locks = {k:UNLOCKED for k in relation}
	accumulator = []
	for a in range(len(schedule)):
				
		# copy pasted from repeatable_read, just acquires all locks and upgrades them when applicable
		if (schedule[a].type==READ):
			if (locks[schedule[a].attribute]!=UNLOCKED):
				accumulator = [schedule[a]]
			else:
				accumulator = [action(thread,SLOCK,schedule[a].attribute),schedule[a]]
				locks[schedule[a].attribute]=SLOCK
		elif (schedule[a].type==WRITE):
			if (locks[schedule[a].attribute]==XLOCK):
				accumulator = [schedule[a]]
			else:
				accumulator = [action(thread,XLOCK,schedule[a].attribute),schedule[a]]
				locks[schedule[a].attribute]=XLOCK

		neededlocks = {k:UNLOCKED for k in relation}
		for x in schedule[a+1:]:
			if (x.type==READ):
				if (neededlocks[x.attribute]!=XLOCK):
					neededlocks[x.attribute]=SLOCK
			elif(x.type==WRITE):
				neededlocks[x.attribute] = XLOCK
		shrink = True
		for x in neededlocks:
			if (neededlocks[x]>locks[x]):
				shrink = False
		downgradeacc = []
		releaseacc = []
		if (shrink):
			# we're in shrinking phase, release any locks we don't need
			for x in locks:
				if (locks[x]>neededlocks[x]):
					if (neededlocks[x]==UNLOCKED):
						# release
						releaseacc.append(action(thread,RELEASE,x))
						locks[x]=UNLOCKED
					elif(neededlocks[x]==SLOCK and downgrade):
						downgradeacc.append(action(thread,SLOCK,x))
						locks[x]=SLOCK
		# release THEN downgrade
		accumulator = accumulator + (releaseacc + downgradeacc)
		if (len(accumulator)>0):
			yield accumulator

def eager_two_phase_locking_scheduler(relation,schedule,thread,downgrade=True):
	locks = {k:UNLOCKED for k in relation}
	accumulator = []
	for a in range(len(schedule)):
				
		# copy pasted from repeatable_read, just acquires all locks and upgrades them when applicable
		if (schedule[a].type==READ):
			if (locks[schedule[a].attribute]!=UNLOCKED):
				accumulator = [schedule[a]]
			else:
				accumulator = [action(thread,SLOCK,schedule[a].attribute),schedule[a]]
				locks[schedule[a].attribute]=SLOCK
		elif (schedule[a].type==WRITE):
			if (locks[schedule[a].attribute]==XLOCK):
				accumulator = [schedule[a]]
			else:
				accumulator = [action(thread,XLOCK,schedule[a].attribute),schedule[a]]
				locks[schedule[a].attribute]=XLOCK

		neededlocks = {k:UNLOCKED for k in relation}
		for x in schedule[a+1:]:
			if (x.type==READ):
				if (neededlocks[x.attribute]!=XLOCK):
					neededlocks[x.attribute]=SLOCK
			elif(x.type==WRITE):
				neededlocks[x.attribute] = XLOCK
		shrink = True
		for x in neededlocks:
			if (neededlocks[x]>locks[x]):
				shrink = False
		if (shrink):
			# we're in shrinking phase, release any locks we don't need
			for x in locks:
				if (locks[x]>neededlocks[x]):
					if (neededlocks[x]==UNLOCKED):
						# release
						accumulator.append(action(thread,RELEASE,x))
						locks[x]=UNLOCKED
					elif(neededlocks[x]==SLOCK and downgrade):
						accumulator.append(action(thread,SLOCK,x))
						locks[x]=SLOCK
		if (len(accumulator)>0):
			yield accumulator
			
two_phase_locking_downgrade_scheduler = lambda x,y,z: two_phase_locking_scheduler(x,y,z,downgrade=True)

def match_schedules(a,b):
	# grades schedules but allows the student to rearrange locks that can pass each other in their answer...
	raise NotImplementedError("augh")


def parse_schedule(a):
	""" parses a schedule. this will absolutely vomit errors if it isn't formatted correctly, but only if it's not formatted correctly. catch them and react!"""
	if (a[-1]==";"):
		a = a[:-1]
	a = a.replace(" ","").upper().split(";")
	sched = []
	funcs = {"S":SLOCK,"X":XLOCK,"W":WRITE,"R":READ,"REL":RELEASE,"COMMIT":COMMIT,"WAIT":WAIT,"DENIED":DENIED,"ABORT":ABORT}
	for x in a:
		p1 = x.index("(")
		p2 = x.index(")")
		assert(p2==len(x)-1)
		assert(p1>1)
		assert(p1<p2)
		funcname = x[0:p1-1]
		thread = int(x[p1-1])
		assert(funcname in funcs)
		contents = x[p1+1:p2].split(",")
		assert(all(len(x)==1 for x in contents))
		contents = "".join(contents)
		assert(len(contents)>0 or funcs[funcname] in [COMMIT,ABORT])
		sched.append(action(thread,funcs[funcname],contents))
	return sched




def print_schedule(sched): # just reuse the repr code i wrote
	return ";".join(repr(x) for x in combine_actions(combine_actions(sched,RELEASE),SLOCK))


def combine_actions(sched,t):
	""" normalization step, combine adjacent actions """
	acc = []
	prior = None
	for x in sched:
		if (x.type==t):
			if (prior is None):
				prior = x
			else:
				if (prior.thread==x.thread):
					prior = action(prior.thread,prior.type,prior.attribute+x.attribute)
				else:
					# incompatible, priorswap
					acc.append(prior)
					prior = x
		else:
			if (not (prior is None)):
				acc.append(prior)
				prior = None
			acc.append(x)
	if (not (prior is None)):
		acc.append(prior)
	return acc

def combine_releases(sched):
	# for backwards compatibility
	return combine_actions(sched,RELEASE)

def place_locks(schedule,isolations,relation):
	""" takes some schedule generators and merges their schedules, puts out a DENIED and stops if there's a lock conflict. 
	    the asserts in this function are things that should NEVER happen, since every schedule generator should be correct relative to itself!
	"""
	threads = len(isolations)
	# i apologize for this next line
	generators = [x[1][0](relation,x[1][1],x[0]+1) for x in enumerate(zip(isolations,[[a for a in schedule if a.thread==x+1] for x in range(threads)]))]
	acc = []
	slocks = {k:list() for k in relation}
	xlocks = {k:None for k in relation}
	for x in schedule:
		chunk = next(generators[x.thread-1])
		# ok now we just have to add this chunk
		for a in chunk:
			if (a.type==READ):
				assert(a.thread in slocks[a.attribute] or a.thread==xlocks[a.attribute])
				acc.append(a)
			elif (a.type==WRITE):
				assert(a.thread==xlocks[a.attribute])
				acc.append(a)
			elif (a.type==RELEASE):
				if (a.thread in slocks[a.attribute]):
					slocks[a.attribute].remove(a.thread)
				else:
					assert(xlocks[a.attribute]==a.thread)
					xlocks[a.attribute] = None
				acc.append(a)
			elif (a.type==SLOCK):
				if (not (xlocks[a.attribute] in [None,a.thread])):
					# uh oh, this is a genuine conflict!
					acc.append(a)
					acc.append(action(a.thread,DENIED,a.attribute))
					return acc
				xlocks[a.attribute]=None # in case it was a downgrade, otherwise do nothing
				slocks[a.attribute].append(a.thread)
				acc.append(a)
			elif (a.type==XLOCK):
				if (not ((len(slocks[a.attribute])==0 or slocks[a.attribute]==[a.thread]) and xlocks[a.attribute]==None)):
					# xlock conflict
					acc.append(a)
					acc.append(action(a.thread,DENIED,a.attribute))
					return acc
				slocks[a.attribute]=[] # clear slock if lock upgrade, otherwise do nothing
				xlocks[a.attribute]=a.thread
				acc.append(a)
	return acc

class GeneratorPeek:
	def __init__(self,i):
		self.i=iter(i)
		self.cache=[]
	def peek(self):
		if (len(self.cache)>0):
			return self.cache[0]
		else:
			self.cache.append(next(self.i))
			return self.cache[0]
	def next(self):
		if (len(self.cache)>0):
			t = self.cache[0]
			self.cache = self.cache[1:]
			return t
		else:
			return next(self.i)

def place_locks_and_wait(schedule,isolations,relation):
	""" takes some schedule generators and merges their schedules, waits on conflict.
	    the asserts in this function are things that should NEVER happen, since every schedule generator should be correct relative to itself!
	"""
	schedule = schedule.copy() # yeah we're gonna call remove, which removes in-place.
	threads = len(isolations)
	# i apologize for this next line
	generators = [GeneratorPeek(x[1][0](relation,x[1][1],x[0]+1)) for x in enumerate(zip(isolations,[[a for a in schedule if a.thread==x+1] for x in range(threads)]))]
	acc = []
	slocks = {k:list() for k in relation}
	xlocks = {k:None for k in relation}
	waiting = dict()
	while (len(schedule)>0):
		for x in schedule:
			if (x.thread in waiting and waiting[x.thread]!=x):
				continue
			tmpacc = []
			chunk = generators[x.thread-1].peek()
			# ok now we just have to add this chunk
			for a in chunk:
				if (a.type==READ):
					assert(a.thread in slocks[a.attribute] or a.thread==xlocks[a.attribute])
					tmpacc.append(a)
				elif (a.type==WRITE):
					assert(a.thread==xlocks[a.attribute])
					tmpacc.append(a)
				elif (a.type==RELEASE):
					if (a.thread in slocks[a.attribute]):
						slocks[a.attribute].remove(a.thread)
					else:
						assert(xlocks[a.attribute]==a.thread)
						xlocks[a.attribute] = None
					tmpacc.append(a)
				elif (a.type==SLOCK):
					if (not (xlocks[a.attribute] in [None,a.thread])):
						# uh oh, this is a genuine conflict!
						if (not (a.thread in waiting)):
							# hacky time
							acc.append(a)
							acc.append(action(a.thread,WAIT,a.attribute))
						waiting[a.thread]=x
						break
					xlocks[a.attribute]=None # in case it was a downgrade, otherwise do nothing
					slocks[a.attribute].append(a.thread)
					tmpacc.append(a)
				elif (a.type==XLOCK):
					if (not ((len(slocks[a.attribute])==0 or slocks[a.attribute]==[a.thread]) and xlocks[a.attribute]==None)):
						# xlock conflict
						if (not (a.thread in waiting)):
							acc.append(a)
							acc.append(action(a.thread,WAIT,a.attribute))
						waiting[a.thread]=x
						break
					slocks[a.attribute]=[] # clear slock if lock upgrade, otherwise do nothing
					xlocks[a.attribute]=a.thread
					tmpacc.append(a)
			else:
				generators[x.thread-1].next()
				acc = acc + tmpacc
				schedule.remove(x)
				if (x.thread in waiting):
					del waiting[x.thread]
				break # one finished
		else:
			# uhh, we're deadlocking.
			return acc
	return acc


# Check transaction schedulers' behaviors based mostly on examples done in pre-lectures, etc.
def transaction_scheduler_tests():
	
	transaction_lookup = {"repeatable read":repeatable_read_scheduler,"read committed":read_committed_scheduler,"Two Phase Locking (2PL)":two_phase_locking_downgrade_scheduler, "Strict Two Phase Locking (S2PL)":repeatable_read_scheduler}
	
	trxn_tests = [
		# ISOLATION LEVELS
		# Isolation level arise
		{
			"transactions": ["read committed", "read committed"],
			"schedule": "R1(A);R2(C);R2(A);W2(A);R1(B);W1(B);W1(C)",
			# "answer": "S1(A);R1(A);REL1(A);S2(C);R2(C);REL2(C);S2(A);R2(A);X2(A);W2(A);REL2(A);S1(B);R1(B);X1(B);W1(B);X1(C);W1(C);REL1(B,C)", 	# with lock upgrades (ideally)
			"answer": "S1(A);R1(A);REL1(A);S2(C);R2(C);REL2(C);S2(A);R2(A);REL2(A);X2(A);W2(A);REL2(A);S1(B);R1(B);REL1(B);X1(B);W1(B);X1(C);W1(C);REL1(B,C)", # without lock upgrades
			"wait": False,
		}, # TODO: For isolation level activities, add a NOTE that lock upgrades aren't supported OR add support for lock upgrades
		# Isolation level arise
		{
			"transactions": ["repeatable read", "read committed"],
			"schedule": "R1(A);R2(C);R2(A);R1(B);W1(B);W1(C);W2(A)",
			"answer": "S1(A);R1(A);S2(C);R2(C);REL2(C);S2(A);R2(A);REL2(A);S1(B);R1(B);X1(B);W1(B);X1(C);W1(C);REL1(A,B,C);X2(A);W2(A);REL2(A)",
		    "wait": False,
		},


		# TWO PHASE LOCKING (2PL)
		# PRE-LECTURES:
		# 2PL arise - no ("Theory of Serializability" slide 23)
		{
			"transactions": ["Two Phase Locking (2PL)", "Two Phase Locking (2PL)"],
			"schedule": "R1(A);W1(A);R2(A);W2(A);R1(B);W1(B);R2(B);W2(B)",
			"answer": "S1(A);R1(A);X1(A);W1(A);S2(A);DENIED2(A)",
			"wait": False,
		},
		# 2PL enforce ("Theory of Serializability" slide 23)
		{
			"transactions": ["Two Phase Locking (2PL)", "Two Phase Locking (2PL)", "Two Phase Locking (2PL)"],
			"schedule": "R1(A);W1(A);R2(A);W2(A);R1(B);W1(B);R2(B);W2(B)",
			# "answer": "S1(A);R1(A);X1(A);W1(A);S2(A);WAIT2(A);S1(B);R1(B);X1(B);W1(B);REL1(A,B);R2(A);X2(A);W2(A);S2(B);R2(B);X2(B);W2(B);REL2(A,B)", # doesn't indicate lock granted
			"answer": "S1(A);R1(A);X1(A);W1(A);S2(A);WAIT2(A);S1(B);R1(B);X1(B);W1(B);REL1(A,B);S2(A);R2(A);X2(A);W2(A);S2(B);R2(B);X2(B);W2(B);REL2(A,B)",
			"wait": True,
		},	# NOTE: When a lock that was waiting is granted, show it by Ri(A) or Xi(A) respectively
		# 2PL enforce ("Theory of Serializability" slide 24)
		{
			"transactions": ["Two Phase Locking (2PL)", "Two Phase Locking (2PL)", "Two Phase Locking (2PL)"],
			"schedule": "R1(A);R2(B);R3(A);W2(C);R1(C);R2(B);W1(B);R3(B)",
			"answer": "S1(A);R1(A);S2(B);R2(B);S3(A);R3(A);X2(C);W2(C);REL2(C);S1(C);R1(C);R2(B);REL2(B);X1(B);W1(B);REL1(A,B,C);S3(B);R3(B);REL3(A,B)",
			"wait": True,
		},
		# 2PL enforce ("Theory of Serializability" slide 24) - demos downgrades
		{ 
			"transactions": ["Two Phase Locking (2PL)", "Two Phase Locking (2PL)", "Two Phase Locking (2PL)"],
			"schedule": "R1(A);R2(B);R3(A);W2(C);R2(C);R1(C);R2(B);W1(B);R3(B)",
			"answer": "S1(A);R1(A);S2(B);R2(B);S3(A);R3(A);X2(C);W2(C);S2(C);R2(C);REL2(C);S1(C);R1(C);R2(B);REL2(B);X1(B);W1(B);REL1(A,B,C);S3(B);R3(B);REL3(A,B)",
			"wait": True,
		},
		
		# EXTRA EXAMPLES (https://mediaspace.illinois.edu/media/t/1_l02q592i)
		# 2PL arise - no (video 2PL a)
		{
			"transactions": ["Two Phase Locking (2PL)", "Two Phase Locking (2PL)", "Two Phase Locking (2PL)"],
			"schedule": "W3(C);W1(A);R2(A);R1(A);W2(C);R1(B);W2(B);R3(C)",
			"answer": "X3(C);W3(C);S3(C);X1(A);W1(A);S2(A);DENIED2(A)",
			"wait": False,
		},
		# 2PL arise - yes (video 2PL b)
		{
			"transactions": ["Two Phase Locking (2PL)", "Two Phase Locking (2PL)", "Two Phase Locking (2PL)"],
			"schedule": "W2(A);W3(B);R1(C);W2(A);R1(A);W1(C);R3(B)",
			"answer": "X2(A);W2(A);X3(B);W3(B);S3(B);S1(C);R1(C);W2(A);REL2(A);S1(A);R1(A);X1(C);W1(C);REL1(A,C);R3(B);REL3(B)",
			"wait": False,
		},
		# 2PL arise - yes (video 2PL c)
		{
			"transactions": ["Two Phase Locking (2PL)", "Two Phase Locking (2PL)", "Two Phase Locking (2PL)"],
			"schedule": "W1(B);W2(A);R1(B);R2(B);W3(C);R3(C);R2(A)",
			"answer": "X1(B);W1(B);S1(B);X2(A);W2(A);R1(B);REL1(B);S2(B);R2(B);REL2(B);S2(A);X3(C);W3(C);S3(C);R3(C);REL3(C);R2(A);REL2(A)",
			"wait": False,
		}, # NOTE: Releases before downgrades (for grading)
		# 2PL arise - no (video 2PL d)
		{
			"transactions": ["Two Phase Locking (2PL)", "Two Phase Locking (2PL)", "Two Phase Locking (2PL)"],
			"schedule": "R1(A);W3(C);W3(B);R1(B);W2(B);W2(A);R3(C);W2(A)",
			# "answer": "S1(A);R1(A);X3(C);W3(C);X3(B);W3(B);S1(B);DENIED1(B)",		# incorrect
			"answer": "S1(A);R1(A);X3(C);W3(C);X3(B);W3(B);REL3(B);S3(C);S1(B);R1(B);REL1(A,B);X2(B);W2(B);X2(A);W2(A);REL2(B);R3(C);REL3(C);W2(A);REL2(A)",
			"wait": False,
		},	# NOTE: Use downgrades: E.g. X3(C);W3(C);S3(C);...;R3(C)
		

		# STRICT TWO PHASE LOCKING
		# PRE-LECTURES
		# S2PL enforce ("Theory of Serializability" slide 28)
		{
			"transactions": ["Strict Two Phase Locking (S2PL)","Strict Two Phase Locking (S2PL)","Strict Two Phase Locking (S2PL)"],
			"schedule": "R1(A);R2(B);R3(A);W2(C);R1(C);R2(B);W1(B);R3(B)",
			"answer": "S1(A);R1(A);S2(B);R2(B);S3(A);R3(A);X2(C);W2(C);S1(C);WAIT1(C);R2(B);REL2(B,C);S1(C);R1(C);X1(B);W1(B);REL1(A,B,C);S3(B);R3(B);REL3(A,B)",
			"wait": True,
		}, # NOTE: Answers shoudln't add COMMIT actions
		
		# S2PL EXTRA EXAMPLES : https://mediaspace.illinois.edu/media/t/1_l02q592i
		# S2PL arise - no (video S2PL a)
		{
			"transactions": ["Strict Two Phase Locking (S2PL)","Strict Two Phase Locking (S2PL)","Strict Two Phase Locking (S2PL)"],
			"schedule": "W3(C);R1(B);W2(A);R2(B);W3(B);R1(A);W2(A)",
			"answer": "X3(C);W3(C);S1(B);R1(B);X2(A);W2(A);S2(B);R2(B);X3(B);DENIED3(B)",
			"wait": False,
		},
		# S2PL arise - no (video S2PL b)
		{
			"transactions": ["Strict Two Phase Locking (S2PL)","Strict Two Phase Locking (S2PL)","Strict Two Phase Locking (S2PL)"],
			"schedule": "R3(A);W2(B);R1(C);W3(A);R2(C);W3(B);R1(B)",
			# "answer": "S3(A);R3(A);X2(B);W2(B);S1(C);R1(C);X3(A);W3(A);S2(C);REL2(B,C);X3(B);W3(B);REL3(A,B);S1(B);R1(B);REL1(B,C)", 	# forgot R2(C)
			"answer": "S3(A);R3(A);X2(B);W2(B);S1(C);R1(C);X3(A);W3(A);S2(C);R2(C);REL2(B,C);X3(B);W3(B);REL3(A,B);S1(B);R1(B);REL1(B,C)",
			"wait": False,
		},
		# S2PL arise - yes (video S2PL c)
		{
			"transactions": ["Strict Two Phase Locking (S2PL)","Strict Two Phase Locking (S2PL)","Strict Two Phase Locking (S2PL)"],
			"schedule": "W2(B);R3(C);R1(A);R2(C);W1(A);W2(A);W3(A)",
			"answer": "X2(B);W2(B);S3(C);R3(C);S1(A);R1(A);S2(C);R2(C);X1(A);W1(A);REL1(A);X2(A);W2(A);REL2(A,B,C);X3(A);W3(A);REL3(A,C)",
			"wait": False,
		},
		# S2PL arise - yes (video S2PL d)
		{
			"transactions": ["Strict Two Phase Locking (S2PL)","Strict Two Phase Locking (S2PL)","Strict Two Phase Locking (S2PL)"],
			"schedule": "W1(A);W3(C);W2(B);W1(A);R2(B);R3(C);R1(A)",
			"answer": "X1(A);W1(A);X3(C);W3(C);X2(B);W2(B);W1(A);R2(B);REL2(B);R3(C);REL3(C);R1(A);REL1(A)",
			"wait": False,
		},
		

		# LECTURE EXAMPLES (DURING GA18)
		{
			"transactions": ["Two Phase Locking (2PL)", "Two Phase Locking (2PL)"],
			"schedule": "W2(A);R1(C);R1(B);R1(B);W1(B);W2(C);W1(A);",
			"answer": "X2(A);W2(A);S1(C);R1(C);S1(B);R1(B);R1(B);X1(B);W1(B);X2(C);WAIT2(C);X1(A);WAIT1(A)",
			"wait": True,
		},
		{
			"transactions": ["Strict Two Phase Locking (S2PL)","Strict Two Phase Locking (S2PL)"],
			"schedule": "R2(C);R2(A);W1(A);R2(A);W2(B);R2(C);W1(B)",
			"answer": "S2(C);R2(C);S2(A);R2(A);X1(A);WAIT1(A);R2(A);X2(B);W2(B);R2(C);REL2(A,B,C);X1(A);W1(A);X1(B);W1(B);REL1(A,B)",
			"wait": True,
		},
		{
			"transactions": ["Strict Two Phase Locking (S2PL)","Strict Two Phase Locking (S2PL)"],
			"schedule": "R2(C);R2(A);R1(A);R2(A);W2(B);R2(C);W1(B)",
			"answer": "S2(C);R2(C);S2(A);R2(A);S1(A);R1(A);R2(A);X2(B);W2(B);R2(C);REL2(A,B,C);X1(B);W1(B);REL1(A,B)",
			"wait": True,
		},


		# MISC. TESTS: not from the course materials
		{
			"transactions": ["Two Phase Locking (2PL)", "Two Phase Locking (2PL)"],
			"schedule": "R1(A);W1(A)",
			"answer": "S1(A);R1(A);X1(A);W1(A);REL1(A)",
			"wait": False,
		}, # NOTE: that lock upgrades allowed in 2PL and S2PL (skip release)
		{
			"transactions": ["Two Phase Locking (2PL)", "Two Phase Locking (2PL)"],
			"schedule": "W1(A);W2(B);W1(B);W2(A)",
			"answer": "X1(A);W1(A);X2(B);W2(B);X1(B);WAIT1(B);X2(A);WAIT2(A)",
			"wait": True,
		}, # Deadlock in 2PL and S2PL
	]

	for j, trxn_test in enumerate(trxn_tests):
		correct_answer = print_schedule(parse_schedule(trxn_test["answer"]))

		sched = parse_schedule(trxn_test["schedule"])
		transactions = [transaction_lookup[x] for x in trxn_test["transactions"]]
		relations = ''.join(list(set([a.attribute for a in sched])))
		if (trxn_test["wait"]):
			our_answer = print_schedule(place_locks_and_wait(sched, transactions, relations))
		else:
			our_answer = print_schedule(place_locks(sched, transactions, relations))

		try:
			assert (our_answer == correct_answer)
		except Exception:
			print("FAILED test", j)
			print(f"\tTRXNS:\t\t{', '.join(trxn_test['transactions'])}")
			print(f"\tENFORCE:\t{trxn_test['wait']}")
			print(f"\tSCHEDULE:\t{trxn_test['schedule']}")
			print(f"\tEXPECTED:\t{correct_answer}")
			print(f"\tACTUAL:\t\t{our_answer}")

if (__name__=="__main__"):
	# sanity checks on schedulers
	for x in range(1000):
		sched = generate_schedule("ABCDEFGH",2,60)
		# add all relevant combinations of isolation levels.
		# the top-level-scheduelrs (place_locks_and_wait and place_locks) are FULL of asserts.
		# these asserts will tell you if anything does anything obviously bad--
		# - failing to release locks by termination
		# - writing without getting an exclusive lock
		# - reading withoug getting shared lock
		# - releasing on things you have no lock on
		# etc. 
		place_locks_and_wait(sched,[two_phase_locking_scheduler,two_phase_locking_scheduler],"ABCDEFGH")
		place_locks_and_wait(sched,[two_phase_locking_scheduler,two_phase_locking_scheduler],"ABCDEFGH")
		place_locks_and_wait(sched,[repeatable_read_scheduler,repeatable_read_scheduler],"ABCDEFGH")
		place_locks_and_wait(sched,[read_committed_scheduler,repeatable_read_scheduler],"ABCDEFGH")
		place_locks(sched,[two_phase_locking_scheduler,two_phase_locking_scheduler],"ABCDEFGH")
		place_locks(sched,[repeatable_read_scheduler,repeatable_read_scheduler],"ABCDEFGH")
		place_locks(sched,[read_committed_scheduler,repeatable_read_scheduler],"ABCDEFGH")
	print("passed automatic transaction scheduler tests")
	# test 2pl basics
	assert(print_schedule(place_locks_and_wait(parse_schedule("R1(A);W1(A);R1(A)"),[two_phase_locking_scheduler],"A"))=="S1(A);R1(A);X1(A);W1(A);S1(A);R1(A);REL1(A)")
	# test 2pl release THEN downgrade
	assert(print_schedule(place_locks_and_wait(parse_schedule("R1(B);W1(A);W1(B);R1(B)"),[two_phase_locking_scheduler],"AB"))=="S1(B);R1(B);X1(A);W1(A);X1(B);W1(B);REL1(A);S1(B);R1(B);REL1(B)")
	# test resume behavior
	assert(print_schedule(place_locks_and_wait(parse_schedule("W1(A);R2(A);W1(A);R1(A)"),[two_phase_locking_scheduler,two_phase_locking_scheduler],"A"))=="X1(A);W1(A);S2(A);WAIT2(A);W1(A);S1(A);S2(A);R2(A);REL2(A);R1(A);REL1(A)")
	# TODO: more tests for other things
	transaction_scheduler_tests()
	print("passed hand-written transaction scheduler tests")


# templates for pregeneration (and also used for benchmarking)
"""
if (__name__=="__main__"):
	# an example of how question pregeneration might work
	resp = input("pregenerate questions? [Y/n]:")
	if (resp.startswith("n")):
		exit()
	with open("questions_tmp.py","w") as f:
		relation = "ABCDEF"
		f.write("3nf_medium = ")
		tnf = []
		for x in range(1000):
			fds = generate_fds(3,relation,1)
			fds.update(generate_fds(2,relation,2))
			tnf.append((fds,list(decompose_3nf(relation,fds))))
			print(print_fds(tnf[-1][0]),tnf[-1][1])
		f.write(repr(tnf))
		f.write("\n")
"""
"""
		bcnfrelation = "ABCDE"
		f.write("bcnf_test = ")
		bcnf = []
		for x in range(1000):
			fds = generate_fds(2,bcnfrelation,1)
			fds.update(generate_fds(2,bcnfrelation,2))
			print(print_fds(fds))
			bcnf.append((fds,list(bcnf_decompose(bcnfrelation,fds,3))))
			print(bcnf[-1][1])
		f.write(repr(bcnf))
"""
"""
		f.write("\n")
		bcnfrelation = "ABCDEF"
		f.write("bcnf_hard = ")
		bcnf = []
		for x in range(1000):
			fds = generate_fds(3,bcnfrelation,1)
			fds.update(generate_fds(3,bcnfrelation,2))
			bcnf.append((fds,list(bcnf_decompose(bcnfrelation,fds,3))))
			print(print_fds(bcnf[-1][0]),bcnf[-1][1])
		f.write(repr(bcnf))
		f.write("\n")
"""
