#!/bin/bash
echo "+++++++++++++++++++ CREATING TARGET ++++++++++++++++++++"
echo ""
for file in ./*.frag; do
    ../compiler467 -Tn "$file" > "$file".target 2>&1
done
