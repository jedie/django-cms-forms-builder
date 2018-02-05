#!/usr/bin/env bash

set -e

cd cms_forms_builder_test_project

while true
do
(
    clear
    echo "====================================================================="
    set +e
    (
        set -x
        ./manage.py run_test_project_dev_server $*
        sleep 2
    )
)
done