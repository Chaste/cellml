This project contains highly annotated CellML versions of a large number of
cardiac electrophysiology cell-level models, for use with Chaste.  They were
originally incorporated in the FunctionalCuration project (see
https://chaste.cs.ox.ac.uk/trac/wiki/FunctionalCuration). 
However, since they are of more general utility they have now been collected
into their own location.

We have included most of the cardiac electrophysiology models that are available
at http://models.cellml.org/electrophysiology

these are then categorised into three categories.
 1. Working models are in the subfolder 'cellml' (not all reproduce original paper, but they don't crash solvers!)
 2. Models that convert to C++ but tend to crash solvers are in 'dont_solve'.
 3. Models that fail the conversion process are in 'dont_convert'.

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
  NB You can do the same thing for individual files by doing e.g.
  cd Chaste/projects/MyProject/src
  svn propedit svn:externals .
  
  This will open a text editor for you to edit the svn property in a temporary file,
  and specify the externals to pull into this folder. If you put in the lines:
  
  noble_model_1962.cellml https://chaste.cs.ox.ac.uk/svn/chaste/projects/cellml/cellml/noble_model_1962.cellml
  noble_model_1962.out https://chaste.cs.ox.ac.uk/svn/chaste/projects/cellml/cellml/noble_model_1962.out
  
  Then save the file and exit the editor, now if you do
  
  svn up
  
  it should pull in just the files you specified. You can put as many files as you want.
]

IMPORTANT NOTE: If you pull in files as above, then whatever version of your repository 
you load, it will always pull in the current revision of the cellml files 
in the cellml project. We tend to just add metadata to existing models, 
and perhaps add tweaks to prevent hitting divide by zeros, we try to leave the maths unchanged.
So it may be a good idea to keep it up to date, and this is the suggested route.
BUT, when releasing part of your project for a paper or suchlike, it would make 
sense to pull in a specific revision of the cellml project, for reproducibility purposes. 
Luckily you can do this by setting an svn property like this instead:
"cellml -r19716 https://chaste.cs.ox.ac.uk/svn/chaste/projects/cellml/cellml"
you can alter the existing externals line accordingly by using 
svn propedit  svn:externals .
as above.

Models which did not convert properly for some reason when they were last
checked are in the "dont_convert" folder (which isn't checked out by the above command).
They have not necessarily been tried with the latest code version.

The CellML files originated from Alan Garny/Penny Noble/Gary Mirams's
repository as of r72 of that repository.  They are mostly the excitable
models that are packaged with COR, with additional models from the CellML
electrophysiology models repository as of around January 2011.

USEFUL NOTE:
If you want to add options to the ConvertCellModels.py script (for example to
provide access to all of the metadata tagged variables in all the models) 
then you can now (as of r15865) include lines like this in your project
'SConscript' file:

# Change some flags just for this project
env = SConsTools.CloneEnv(env)
env['PYCML_EXTRA_ARGS'] = ['--expose-annotated-variables']

This must come before the DoProjectSConscript() call. 

IMPORTANT NOTE:
If for any reason the mathematics of the CellML file changes, you will need to
regenerate the .out file if one is associated with the model, to update
the analytic jacobian to match the new mathematics.
A couple of python scripts are in this folder that may help with this process.

See https://chaste.cs.ox.ac.uk/trac/wiki/ChasteGuides/CodeGenerationFromCellML 
for more details of working with CellML.

