# TODOExplorer
An idea of a utility to crawl through code folders, find @TODO (or other key) comments in code and present them on an interactive interface

Developing this as a Python exercise and for own use :) - I write @TODO in commented lines in source code
where I've got something to complete, fix or pimp a little

key and path to root code catalogue will be passed through CLI arguments, and later through a GUI

Planned features:
[x] search for all the ToDos in code (pick a root folder with subcatalogues)
[x] collect all todos in a manipulate-able format like json
[x] each todo has file, line number and description
[x] program now runs on the current_working_directory
[ ] pass key and subject folder within command line arguments
[ ] develop a GUI
[ ] GUI can be used to open each file and scroll to the line where a particular @TODO exists
[ ] default editor can be selected or edit can take place in the GUI
