#!/bin/bash
export GEMINI_API_KEY="AIzaSyANbCmV5VLxlHGLu34_Lfq-XN_DVK-m9qY"
# Default to current directory's python or specfic anaconda python
PYTHON_EXEC="/opt/anaconda3/bin/python"

echo "Starting Book Content Generation..."
echo "Using Gemini API."

$PYTHON_EXEC book_gen/gen_workflow.py "$@"
