microexamples
=============

[microexamples.com](microexamples.com) is a site to learn code just by reading examples
It is hosted on Github pages.

##Requirements
* sconstruct
* python
* common lisp
* ghc
* tornado

The text files in the "code" folder have input code for examples. The output is generated automatically and compiled to static html pages.

##Markup
* For chapter names write <!--Chapter=Your Chapter Name-->
* For examples write <!--Exercise-->
* Markup should be on a separate line.
* Dont leave blank lines before or after the markup.

##Branch for Static pages
The gh-pages branch has the static pages for the site.

###To clean temporary files
scons -c

###To compile the examples
scons

###To run the server
python main.py
This will create a tordado server on localhost:8888

###To generate static pages
sh makestatic.sh
We use wget to save static pages and commit them to the gh-pages branch.



