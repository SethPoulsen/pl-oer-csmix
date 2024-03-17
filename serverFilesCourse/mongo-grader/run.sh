#! /bin/bash

##########################
# INIT
##########################


#pwd
#ls
#ls ../grade/serverFilesCourse/mongo-grader
#ls ../grade/serverFilesCourse/grader
#cd ../grade/serverFilesCourse/grader
#pwd
#cd -

# First thing's first: start Mongod daemon
echo "[run] starting Mongod"
#service mongod start
mongod --fork --logpath /var/log/mongodb.log --dbpath /data/db2 --noscripting
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
BASE_GRADER=$JOB_DIR'serverFilesCourse/grader/'  # MUST INCLUDE THIS TO PUT THE base_grader.py FILE INTO THE GRADING location!!
# FROM THE WIKI LINK:
# [All Questions’ info.json must include “grader/” in the list field of “serverFilesCourse” within the “externalGradingOptions” field
# in order to import the needed base_grader.py within all graders] (If the previous semesters’ want to incorporate such changes,
# THIS MUST BE DONE!!!! For the grader to include the base_grader.py into their respective location within the Docker containers!)


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
cp $BASE_GRADER* $MERGE_DIR  # MUST INCLUDE THIS TO PUT THE base_grader.py FILE INTO THE GRADING location!!

if [ ! -f query.js ]
then
    cp $JOB_DIR'student/query.js' $MERGE_DIR
fi

if [ ! -f query_sort.js ]
then
    cp $JOB_DIR'student/query_sort.js' $MERGE_DIR
fi

# we need this to include code as python modules
# There is already one in the /run directory, but we need one in the /run/bin directory as well
echo "" > $BIN_DIR/__init__.py


##########################
# RUN
##########################

cd $JOB_DIR'run/'

touch ~/.mongorc.js
echo 'DBQuery.shellBatchSize = 200;
      this.cat = this.cd = this.copyDbPath = this.getHostName = this.getMemInfo = this.hostname = 
      this.isInteractive = this.listFiles = this.load = this.ls = this.md5sumFile = this.mkdir = 
      this.pwd = /*this.quit =*/ this.removeFile = this.resetDbPath = this.sleep = this.setVerboseShell = 
      this.version = this._isWindows = this._rand = this.eval = this.printjson = function() {
        print("Trying to cheat, eh? This incident will be reported.");
        quit();
      }' > ~/.mongorc.js

echo "[run] starting autograder"

bash -c 'python3 -m mongodb_grader_main'

if [ ! -s results.json ]
then
  # Let's attempt to keep everything from dying completely
  echo '{"succeeded": false, "score": 0.0, "message": "Catastrophic failure! Contact course staff and have them check the logs for this submission."}' > results.json
fi

echo "[run] autograder completed"
echo "Generating results (results.json) in path: '/grade/results/results.json'"
# cp $MERGE_DIR/results.json '/grade/results/results.json'
# echo "[run] copied results, thanks Abdu!"

# cat "./setup-data-cbtf.js"