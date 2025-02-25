# Chaste CellML Project
This project contains highly-annotated CellML versions of a large number of
cardiac electrophysiology cell-level models, for use with Chaste, [ApPredict](https://www.maths.nottingham.ac.uk/plp/pmzgm/ap_predict/) and [WebLab](https://chaste.cs.ox.ac.uk/WebLab).  

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
Chaste and [ApPredict](www.github.com/Chaste/ApPredict) now pull in CellML files automatically via cmake at cmake configure time (an internet connection is required). 
These are placed in `<ApPredict>/src/cellml`, *do not* place any other code or cellml files in this location.
Additional CellML files can be placed in `<ApPredict>/src/extra_models`.

It is also possible to pull in cellml files using this repository as a git submodule, or to copy files manually.

### Git Submodules
Git submodules make this cellml folder appear to be within your own project, and record which revision of this repository you are using.
From the command line, the relevant incantation will look something like:

```sh
$ cd <my_project>
$ git submodule add https://github.com/Chaste/cellml.git src/cellml
$ git submodule init
$ git submodule update
```
This will import all of the CellML files into your source (`src`) tree, and all of them will be automatically converted to .hpp and .cpp files for use with Chaste at compile time. If you don't want this to happen, change the ```src/cellml``` to just ```cellml``` and then convert as you require, as per [Code Generation From CellML].

#### Updating: 

If you pull in files as above, then whatever version of your repository 
you load, it will contain the revision of the cellml files in this repository when you typed ```git submodule update```. 
We tend to just add metadata to existing models, and perhaps add tweaks to prevent hitting divide by zeros, we try to leave the maths unchanged. So it may be a good idea to keep it up to date, which you can do with:

```sh
$ git submodule update
$ cd <my_project>/src/cellml
$ git checkout master
$ git pull
```

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
```cmake
set(Chaste_PYCML_EXTRA_ARGS "--expose-annotated-variables")
```

### Scons
For older ```scons``` rather than ```cmake``` projects, include lines like this in your project
'SConscript' file:

```python
# Change some flags just for this project
env = SConsTools.CloneEnv(env)
env['Chaste_CODEGEN_EXTRA_ARGS'] = ['--expose-annotated-variables']
```
Or for pre 2021 Releases (using PyCml)
```python
env['PYCML_EXTRA_ARGS'] = ['--expose-annotated-variables']
```

This must come before the ```DoProjectSConscript()``` call. 

## Analytic Jacobians:
We used to require the third-party software Maple to generate Jacobian matricies analytically, but we now automatically do this using SymPy.

See [Code Generation From CellML] for more details of working with these CellML files.

[Code Generation From CellML]: <https://chaste.github.io/docs/user-guides/code-generation-from-cellml/>
[Functional Curation]: <https://chaste.github.io/docs/paper-tutorials/functionalcuration/>
[Chaste user project]: <https://chaste.github.io/docs/user-guides/user-projects/>
