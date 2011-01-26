0.5.1+ -- Development
=====================

- Updated the version recall to GitPython 0.3.1 (used only if present!)
- HocVector into NumpyArray for saving with swap in place, to reduce overhead


0.5.1 - 23 Nov 2010
===================

- Fixed the picking of the cylinder. Possible to select a cylinder 
  clicking anywhere.
- Possibility to plot points instead of a lines
- BaseREf class are discriminated through the group id and not any more on
  class base.


0.5.0 - 19 Jun 2010
===================

- Closed #16
- Fixed some typos on the docs
- Mechanisms are shown on the info tab
- Refactored code for extensibility
- Storage moved to a hdf file.
- Extensibility to other kind of variables, not only vectors

0.4.4 - 1 Apr 2010
==================

- Fixed the name on the README
- Treeview updated everytime a database is loaded.


0.4.3 - 2 Mar 2010
==================

- Info sections updated
- Update the docs and website


0.4.2 - 18 Feb 2010
===================

- Added simulation saving abilities.
- Updated the doc


0.4.1 - 28 Jan 2010
========================

- Closed #13
- Introduced a tab to retrieve info on the section

0.4.0 - 19 Jan 2010
========================

- Remplemented using Mayavi2 and Qt4 for better performance and better usability.
- Cleanup and refactoring of the code.
- Closed #11, #12, #15

0.3.5 - 20 Nov 2009 
===================

- Using sphinx for the doc
- Using paver for deployment
- python egg and easy install support
- User manuel available in pdf format


0.3.4 - 15 Sep 2009
===================

- Changed the way the module is imported to allow other program to use the manager 
  as a storing objects for results.

0.3.3 - 3 Sep 2009
==================

- Integrated the pylab interface using the GTK backend provided by pylab. 
  It is possible to zoom and navigate the graph with the pylab tools.
- It is now possible to decide in which figure to plot, using the current figure selector.

0.3.22 - 31 Jul 2009
====================

- Closed bug #10
- Changed the name of the module from nrnVisio to nrnvisio to be python
  standard compliant.
- Manager being transformed into a library (WIP)

0.3.21 - 20 Jul 2009
====================

- Better handling of the pick section routine
- Changed the examples to use the create statement for hoc, to have 
  a proper name of the section also in python.
- Modified the GUI to handle a runtime change of a section. The model is redrawn
  completely, the zoom is conserved.

0.3.2 - 20 Jul 2009
===================

Bug Release. Closed Bug #9

0.3.1 - 18 Jul 2009
===================

Bug Release.

0.3.0 - 14 Jul 2009
===================

New Features
------------

- Stop Button on the animation Control
- Better handling on the timeline updating routine.

BUGFixes
--------

- Closed bug #8
- Closed bug #3


0.2.0 - 6 Jul 2009
==================

New Features
------------

Some new features has been introduced:

- User defined color. The user can now change the colors of the model for a better contrast.
- Info tab. Reports the properties of the selected section.

BUGFixes
--------

- Closed bug #4
- Closed bug #5
- Closed bug #6



0.1.0 - 30 Jun 2009
===================

Fist public release.
 
Features
--------

- 3D visualization of the model with the possibility to change it runtime
- Creation of vectors to record any variable present in the section
- Pylab integration to plot directly the result of the simulation
- Explore of the timecourse of any variable among time using a color coded scale in the 3d representation
- the GUI runs in its own thread so it's possible to use the console to modify/interact with the model.