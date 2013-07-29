This project contains highly annotated CellML versions of a large number of
cardiac electrophysiology cell-level models, for use with Chaste.  They were
originally incorporated in the FunctionalCuration project (see
https://chaste.cs.ox.ac.uk/trac/wiki/FunctionalCuration). 
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

[
  NB You can do the same thing for a single file by doing e.g.
  cd Chaste/projects/MyProject/src
  svn propset svn:externals "noble_model_1962.cellml https://chaste.cs.ox.ac.uk/svn/chaste/projects/cellml/cellml/noble_model_1962.cellml" .
  svn up

  BUT - you only seem to be able to have one external per folder, 
  and so you need separate folders (all added to svn) for separate 
  cellml files. Although if you just want a handful of them this can 
  still save time and be tidier than converting all of them.
]

Models which did not convert properly for some reason when they were last
checked are in the "dont_convert" folder (which isn't checked out by the above command).
They have not necessarily been tried with the latest code version.

The CellML files originated from Alan Garny/Penny Noble/Gary Mirams's
repository as of r72 of that repository.  They are mostly the excitable
models that are packaged with COR, with additional models from the CellML
electrophysiology models repository as of around January 2011.

If you want to add options to the ConvertCellModels.py script (for example to
provide access to all of the metadata tagged variables in all the models) 
then you can now (as of r15865) include lines like this in your project
'SConscript' file:

# Change some flags just for this project
env = SConsTools.CloneEnv(env)
env['PYCML_EXTRA_ARGS'] = ['--expose-annotated-variables']

This must come before the DoProjectSConscript() call. 

If for any reason you need to (re)generate a .out file for analytic jacobians,
a couple of python scripts are in this folder that may help with this process.
