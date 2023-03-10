#!/bin/bash
latest_py_file_changed=`find . -name "*.py"  -type f -print0 | xargs -0 stat -f "%m %N" | sort -rn | head -1 | cut -f2- -d" "`
python3 $latest_py_file_changed < input.txt