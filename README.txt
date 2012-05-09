This project contains highly annotated CellML versions of a large number of
cardiac electrophysiology cell-level models, for use with Chaste.  They were
originally incorporated in the FunctionalCuration project (see
https://chaste.cs.ox.ac.uk/cgi-bin/trac.cgi/wiki/FunctionalCuration). 
However, since they are of more general utility they have now been collected
into their own location.

To use these files within your code, you may just check out the project. 
However, you can also make use of the Subversion svn:externals functionality
(see http://svnbook.red-bean.com/en/1.7/svn.advanced.externals.html) to make
the cellml folder appear to be within your own project too.  From the
command line, the relevant incantation will look something like:

cd Chaste/projects/MyProject 
(or cd Chaste/projects/MyProject/src if you want them all converting automatically)
svn propset svn:externals "cellml https://chaste.cs.ox.ac.uk/svn/chaste/projects/cellml/cellml" .
svn up

(Note the "." at the end of the svn propset line - this is important!)

Models which did not convert properly for some reason when they were last
checked are in the "dont_convert" folder (which isn't checked out by the above command).
They have not necessarily been tried with the latest code version.

The CellML files originated from Alan Garny/Penny Noble/Gary Mirams's
repository as of r72 of that repository.  They are mostly the excitable
models that are packaged with COR, with additional models from the CellML
electrophysiology models repository as of around January 2011.
