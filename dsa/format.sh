#!/bin/bash
latest_py_file_changed=`find . -name "*.py"  -type f -print0 | xargs -0 stat -f "%m %N" | sort -rn | head -1 | cut -f2- -d" "`
vim -c "%s/\n\n/\r /g" -c "%s/^/#/g" -c "%s/#\(\w\)/# \1/g" -c wq $latest_py_file_changed