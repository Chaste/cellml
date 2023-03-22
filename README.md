# Chaste CellML Project
This project contains highly-annotated CellML versions of a large number of
cardiac electrophysiology cell-level models, for use with Chaste.  

They were originally incorporated in the [Functional Curation] project.
However, since they are of more general utility they have now been collected
into their own location.

We have included most of the cardiac electrophysiology models that were available
at <http://models.cellml.org/electrophysiology> as of around January 2011, and added a few others as they have been released.

The models were then categorised into three categories:
 1. Working models are in the subfolder 'cellml' (not all reproduce original papers, but they don't crash solvers!)

These are included in the `master` branch. To use these files within your code, you may just clone this repository. 

 2. Models that convert to C++ but tend to crash solvers are in 'dont_solve'.
 3. Models that fail the conversion process are in 'dont_convert'.

These are both included in the `notworking` branch.

## Pulling in cellml files
*Please note:* the CellMl files needed are (automatically) pulled in via cmake at cmake configure time (an internet connection is required). 
These are places in `<ApPredict>/src/cellml` *do not* place any other code or cellml files in this location.
Additional CellML files can be places in `<ApPredict>/src/extra_models`.

## USEFUL NOTE:
If you are using these in a [Chaste user project] and want to add options to the ConvertCellModels.py script (for example to provide access to all of the metadata tagged variables in all the models) then follow the relevant instructions below depending on whether it is a cmake or scons project:

### CMake

Add this to your project's ```CMakeLists.txt``` file:

```cmake
# Here we add extra arguments to force PyCML to use this extra argument (make Get and Set methods for 
# all metadata annotated variables).  
set(Chaste_CODEGEN_EXTRA_ARGS "--expose-annotated-variables")
```
Or for pre 2021 Releases (using PyCml)
```
set(Chaste_PYCML_EXTRA_ARGS "--expose-annotated-variables")
```

### Scons
Scons is no longer supported by Chaste, but can be used for older versions.
For older ```scons``` rather than ```cmake``` projects, include lines like this in your project
'SConscript' file:

```python
# Change some flags just for this project
env = SConsTools.CloneEnv(env)
env['Chaste_CODEGEN_EXTRA_ARGS'] = ['--expose-annotated-variables']
```
Or for pre 2021 Releases (using PyCml)
```
env['PYCML_EXTRA_ARGS'] = ['--expose-annotated-variables']
```

This must come before the ```DoProjectSConscript()``` call. 

## Analytic Jacobians:
We used to require the third-party software Maple to generate Jacobian matricies analytically, but we now automatically do this using SymPy.

See [Code Generation From CellML] for more details of working with these CellML files.

[Code Generation From CellML]: <https://chaste.cs.ox.ac.uk/trac/wiki/ChasteGuides/CodeGenerationFromCellML>
[Functional Curation]: <https://chaste.cs.ox.ac.uk/trac/wiki/FunctionalCuration>
[Chaste user project]: <https://chaste.cs.ox.ac.uk/trac/wiki/InstallGuides/CheckoutUserProject>
