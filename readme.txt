Setup
---------------------------------------------------------------------------------------------------------------------

venv (skip if you already have set up)
- create directory for project to live in
- cd into project directory
- run "python3 -m virtualenv env" to set up new virtual env in project directory
- run "source ./env/bin/activate" to activate the virtual env
- run "pip3 install nltk" to get that dependency

running the program
- make sure you have all files in the project directory, there should be 4
    * SearchEngine.py
    * BooleanQueryEvaluator.py
    * InvertedIndexConstructor.py
    * documents.txt
- run "SearchEngine.py"
- there won't be any output, but you should now see two additional files
    * Inverted_Index.txt
    * Results_File.txt
- inverted index and search results should now be in their respective files
