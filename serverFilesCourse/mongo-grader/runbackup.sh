#! /bin/bash

##########################
# INIT
##########################

# First thing's first: start Mongod daemon
echo "[run] starting Mongod"
#service mongod start
mongod --fork --logpath /var/log/mongodb.log --dbpath /data/db2 --smallfiles
#RESULT=$(mongo --eval  'printjson(db.getMongo().getDBNames())')
#echo $RESULT
echo "[run] Mongo started and configured"

# the directory where the job stuff is
JOB_DIR='/grade/'
# the other directories
STUDENT_DIR=$JOB_DIR'student/'
AG_DIR=$JOB_DIR'serverFilesCourse/mongo-grader/'
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
cp -r $AG_DIR* $MERGE_DIR
cp $TEST_DIR* $MERGE_DIR

# we need this to include code as python modules
# There is already one in the /run directory, but we need one in the /run/bin directory as well
echo "" > $BIN_DIR/__init__.py


##########################
# RUN
##########################

cd $JOB_DIR'run/'

echo "[run] starting autograder"

# mongo < $JOB_DIR'tests/solution.js' | tee -a sol_res.json
#
# sed -i '1,5d;$d;' sol_res.json
# sed -i '$d;' sol_res.json
# cp sol_res.json $JOB_DIR'tests/sol_qry_res.json'
#
#
#
# mongo < $JOB_DIR'student/query.js' | tee -a res.json
#
# sed -i '1,5d;$d;' res.json
# sed -i '$d;' res.json
# cp res.json $JOB_DIR'/student/std_qry_res.json'

touch ~/.mongorc.js
echo 'DBQuery.shellBatchSize = 100;' > ~/.mongorc.js
# add one more line to always prettyprint the ouput
#echo 'DBQuery.prototype._prettyShell = true; ' >> ~/.mongorc.js
bash -c 'python3 parse.py'

echo
if [ -s parse.json ]
then
  cp $MERGE_DIR/parse.json '/grade/results/results.json'
  echo "[run] autograder completed"
  cp $MERGE_DIR/results.json '/grade/results/results.json'
  echo "[run] copied results, thanks Abdu!"
  exit 0
fi

# Let's attempt to keep everything from dying completely
#
mongo --quiet < $JOB_DIR'tests/solution.js' > sol_res.json
cp sol_res.json $JOB_DIR'tests/sol_qry_res.json'

mongo --quiet < $JOB_DIR'student/query.js' > res.json
cp res.json $JOB_DIR'/student/std_qry_res.json'

bash -c 'python3 grade.py'

if [ ! -s results.json ]
then
  # Let's attempt to keep everything from dying completely
  echo '{"succeeded": false, "score": 0.0, "message": "Catastrophic failure! Contact course staff and have them check the logs for this submission."}' > results.json
fi

echo "[run] autograder completed"
cp $MERGE_DIR/results.json '/grade/results/results.json'
#echo "{\"score\": 1, \"succeeded\": true}" > /grade/results/results.json
echo "[run] copied results, thanks Abdu!"
