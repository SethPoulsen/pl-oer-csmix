#! /bin/bash

##########################
# INIT
##########################

# First thing's first: start Mongod daemon
echo "[run] starting Neo4j"
#service mongod start
#mongod --fork --logpath /var/log/mongodb.log --dbpath /data/db2 --smallfiles
#RESULT=$(mongo --eval  'printjson(db.getMongo().getDBNames())')
#echo $RESULT
#./bin/neo4j start #-p 7474:7474 -p 7687:7687 -v '$HOME/neo4j/data:/data/db2'
service neo4j start
end="$((SECONDS+60))"
end="$((SECONDS+60))"
while true; do
    [[ "200" = "$(curl --silent --write-out %{http_code} --output /dev/null http://127.0.0.1:7474)" ]] && break
    [[ "${SECONDS}" -ge "${end}" ]] && exit 1
    sleep 1
done
test1=$(cat /var/log/neo4j/neo4j.log)
echo $test1

echo "[run] Neo4j started and configured"

# the directory where the job stuff is
JOB_DIR='/grade/'
# the other directories
STUDENT_DIR=$JOB_DIR'student/'
AG_DIR=$JOB_DIR'serverFilesCourse/neo4j-grader/'
TEST_DIR=$JOB_DIR'tests/'
OUT_DIR=$JOB_DIR'results/'

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

# we need this to include code as python modules
# There is already one in the /run directory, but we need one in the /run/bin directory as well
echo "" > $BIN_DIR/__init__.py


##########################
# RUN
##########################

cd $JOB_DIR'run/'

echo "[run] starting autograder"

bash -c 'python3 Dataset_Creation.py'
bash -c 'python3 grade.py'

if [ ! -s results.json ]
then
  # Let's attempt to keep everything from dying completely
  echo '{"succeeded": false, "score": 0.0, "message": "Catastrophic failure! Contact course staff and have them check the logs for this submission."}' > results.json
fi

echo "[run] autograder completed"

#get the results from the file
cp $MERGE_DIR/results.json '/grade/results/results.json'
#echo "{\"score\": 1, \"succeeded\": true}" > /grade/results/results.json
echo "[run] copied results, thanks Abdu!"
