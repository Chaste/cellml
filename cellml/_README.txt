This collection of CellML files, while now independent, was originally used
for the Functional Curation project (see
https://chaste.cs.ox.ac.uk/cgi-bin/trac.cgi/wiki/FunctionalCuration).  In
that context, all the *.cellml files directly in this folder are used by the
main long-running protocol tests, and results compared with historic data,
to ensure there are no regressions in functionality.

Models which are not called *.cellml, for example *.cellml_invalid, did not
convert properly for some reason when they were last checked.  They have not
necessarily been tried with the latest code version.

Models within the not_run subfolder do convert correctly, but are not run
automatically by the main tests.

The CellML files originated from Alan Garny/Penny Noble/Gary Mirams's
repository as of r72 of that repository.  They are mostly the excitable
models that are packaged with COR, with additional models from the CellML
electrophysiology models repository as of around January 2011.

