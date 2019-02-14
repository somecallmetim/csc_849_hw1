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
---------------------------------------------------------------------------------------------------------------------

NOTE
---------------------------------------------------------------------------------------------------------------------
iLearn only allows for 5 files to be uploaded and my project is split into 3 separate python files. I'm out of time,
so a refactor isn't in the cards. I'm going to put my Search Results into the Inverted_Index.txt file on top of
the actual inverted index. My apologies for any inconvenience, I'm happy to fix if you don't mind waiting until
tomorrow.
