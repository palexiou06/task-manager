#!/bin/bash

HTML_FILE="index.html"

# Extract tasks and test data from the two input files
TODO_TASKS=$(awk '/^ToDo Tasks:/{f=1;next} /^Done Tasks:/{f=0} f && NF' "$1")
DONE_TASKS=$(awk '/^Done Tasks:/{f=1;next} f && NF' "$1")
UNIT_TEST_RESULTS=$(cat "$2")

# Replace the content of a <pre id="..."> block
update_pre() {
  PRE_ID="$1" CONTENT="$2" perl -0777 -i -pe \
    's{<pre id="\Q$ENV{PRE_ID}\E">.*?</pre>}{<pre id="$ENV{PRE_ID}">\n$ENV{CONTENT}\n</pre>}gs' "$3"
}

update_pre "pending" "$TODO_TASKS" "$HTML_FILE"
update_pre "completed" "$DONE_TASKS" "$HTML_FILE"
update_pre "unittest" "$UNIT_TEST_RESULTS" "$HTML_FILE"

git config --global user.name "github-actions"
git config --global user.email "github-actions@users.noreply.github.com"
git config --global --add safe.directory /app
git add "$HTML_FILE"
git commit -m "Update $HTML_FILE with new task and test data" || echo "No changes to commit"
git push origin HEAD:main
