#! /bin/bash

##########################
# INIT
##########################

# First thing's first: start mysql daemon
echo "[run] starting MySQL"
service mysql start
mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost';"
mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';"
echo "[run] MySQL started and configured"

# the directory where the job stuff is
JOB_DIR='/grade/'
# the other directories
STUDENT_DIR=$JOB_DIR'student/'
AG_DIR=$JOB_DIR'serverFilesCourse/sql-grader/'
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



echo "[run] starting autograder"

cd $JOB_DIR'run/'

#bash -c 'python3 Dataset_Generator.py'
#
#if [ ! -s $TEST_DIR'/setup.sql' ]
#then
#  # Let's attempt to keep everything from dying completely
#  echo '{"succeeded": false, "score": 0.0, "message": "Catastrophic failure! Contact course staff and have them check the logs for this submission."}' > results.json
#fi


bash -c 'python3 grade.py'

if [ ! -s results.json ]
then
  # Let's attempt to keep everything from dying completely
  echo '{"succeeded": false, "score": 0.0, "message": "Catastrophic failure! Contact course staff and have them check the logs for this submission."}' > results.json
fi

echo "[run] autograder completed"

# get the results from the file
cp $MERGE_DIR/results.json '/grade/results/results.json'
echo "[run] copied results"
