#! /bin/bash

##########################
# INIT
##########################

# First thing's first: start Mongod daemon
echo "[run] ~-= MCW TEST UNDERWAY 0001 =-~"
neo4j status
service neo4j status
echo "[run] ~-= MCW TEST =-~"
ls /var/lib/neo4j/import/
ls /var/lib/neo4j/
echo "[run] starting Neo4j"

#./bin/neo4j start #-p 7474:7474 -p 7687:7687 -v '$HOME/neo4j/data:/data/db2'
#start=`date +%s`
service neo4j start
end="$((SECONDS+60))"

while true; do
	#[[ "200" = "$(curl --silent --write-out %{http_code} --output /dev/null http://127.0.0.1:7474)" ]] && break # 14 seconds.
	[[ "400" = "$(curl --silent --write-out %{http_code} --output /dev/null http://127.0.0.1:7687)" ]] && break # 8 seconds.
	curl --silent --write-out %{http_code} --output /dev/null http://127.0.0.1:7687 # 8 seconds.
	#[[ "0" = "$(service neo4j status | grep -c not)" ]] && break
	echo "[run] Time: $SECONDS"
	[[ "${SECONDS}" -ge "${end}" ]] && exit 1
    sleep 1
done

#test1=$(cat /var/log/neo4j/neo4j.log)
#echo $test1
#end=`date +%s`
#runtime=$((end-start))
#echo "[neo4j server run] Time to START service: "$runtime
echo "[run] Neo4j started and configured"

# the directory where the job stuff is
JOB_DIR='/grade/'
# the other directories
STUDENT_DIR=$JOB_DIR'student/'
AG_DIR=$JOB_DIR'serverFilesCourse/neo4j-grader-test/'
TEST_DIR=$JOB_DIR'tests/'
OUT_DIR=$JOB_DIR'results/'
BASE_GRADER=$JOB_DIR'serverFilesCourse/grader/'  # MUST INCLUDE THIS TO PUT THE base_grader.py FILE INTO THE GRADING location!!

# where we will copy everything
MERGE_DIR=$JOB_DIR'run/'
# where we will put the actual student code- this depends on what the autograder expects, etc
BIN_DIR=$MERGE_DIR'bin/'

# now set up the stuff so that our run.sh can work
mkdir $MERGE_DIR
mkdir $BIN_DIR
mkdir $OUT_DIR

cp $STUDENT_DIR* $BIN_DIR
cp $AG_DIR* $MERGE_DIR
cp $TEST_DIR* $MERGE_DIR
cp $BASE_GRADER* $MERGE_DIR  # MUST INCLUDE THIS TO PUT THE base_grader.py FILE INTO THE GRADING location!!

# we need this to include code as python modules
# There is already one in the /run directory, but we need one in the /run/bin directory as well
echo "" > $BIN_DIR/__init__.py


##########################
# RUN
##########################

cd $JOB_DIR'run/'

echo "[run] starting autograder. Time: $SECONDS" # Time: 15 (http) | 

## Old version that uses py2neo which results in each data creation taking as long as 20 seconds
#bash -c 'python3 -m neo4j_grader_main'

## Making data injection and creation faster through Cypher using HTTP protocol! (Apart from the first try, all data generation takes about 1.5 seconds)
bash -c 'python3 -m neo4j_grader_cypher_main'
# The HTTP protocol is probably the issue here.
#bash -c 'python3 Dataset_Creation.py'
# bash -c 'python3 -m neo4j_dataset_generator'
#bash -c 'python3 grade.py'
# bash -c 'python3 -m neo4j_grader'

echo "[run] autograder completed. Time: $SECONDS" # Time: 31 (http) | 
#end=`date +%s`
#runtime=$((end-start))
#echo "[Neo4j Autograder Finished] Autograder Total Runtime: "$runtime
echo "[run] Generating results (results.json) in path: '/grade/results/results.json'"

