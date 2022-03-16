#! /bin/sh -eu

#python -m pip install virtualenv
#vitualenv venv
#source venv/bivn/activate

#### Print usage --help
print_usage() {
  echo "Usage:";
  echo "-m <test_tags> [test groups] (default is all) [possible values: login_prac_test, login_heroku_test]";
  echo "-b <browser> [browser] (default is chrome) [possible values: firefox, edge]";
  echo "-h <help> [display help]"
}

# Default values
TEST_TAGS="sanity_test"
BROWSER="chrome"
ALLURE_TEMP_DIR="./tmp/pytest_allure_results"

while getopts 'm:b:h:' flag; do
  case "${flag}" in
    m) TEST_TAGS="${OPTARG}" ;;
    b) BROWSER="${OPTARG}" ;;
    h | *) # Display help.
      print_usage
      exit 0
      ;;
  esac
done


SCRIPT_PATH="$(pwd)/$(dirname "$(which $0)")"
echo "SCRIPT_PATH=$SCRIPT_PATH"
REPO_PATH="${SCRIPT_PATH}/../.."
echo "REPO_PATH=${REPO_PATH}"

rm -rf ${ALLURE_TEMP_DIR} || true
npm install
python -m pip install -r requirements.txt
pytest -n 2 --browser ${BROWSER} -m ${TEST_TAGS} --alluredir=${ALLURE_TEMP_DIR} || true
npx allure serve ${ALLURE_TEMP_DIR}