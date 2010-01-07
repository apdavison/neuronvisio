# -*- Import: -*-
from paver.easy import *
from paver.setuputils import setup
from setuptools import find_packages
import neuronvisio

try:
    # Optional tasks, only needed for development
    # -*- Optional import: -*-
    from github.tools.task import *
    import paver.doctools
    import paver.virtual
    import paver.misctasks
    ALL_TASKS_LOADED = True
except ImportError, e:
    info("some tasks could not not be imported.")
    debug(str(e))
    ALL_TASKS_LOADED = False



version = neuronvisio.__version__

classifiers = [
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    "Development Status :: 4 - Beta",
    "Programming Language :: Python",
    "Topic :: Scientific/Engineering :: Visualization"

    ]

install_requires = [
    # -*- Install requires: -*-
    'setuptools',
    ]

entry_points="""
    # -*- Entry points: -*-
    """

# compatible with distutils of python 2.3+ or later
setup(
    name='neuronvisio',
    version=version,
    description='NeuronVisio is a GTK2 user interface for NEURON simulator enviroment',
    long_description=open('README.rst', 'r').read(),
    classifiers=classifiers,
    keywords='neuron, gui, pylab, 3D, visualization',
    author='Michele Mattioni',
    author_email='mattioni@ebi.ac.uk',
    url='http://mattions.github.com/neuronvisio/',
    license='GPLv3',
    packages = find_packages(exclude=['bootstrap', 'pavement',]),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points=entry_points,
    )

options(
    # -*- Paver options: -*-
    minilib=Bunch(
        extra_files=[
            # -*- Minilib extra files: -*-
            ]
        ),
    sphinx=Bunch(
        docroot='docs',
        builddir="_build",
        sourcedir=""
        ),
    virtualenv=Bunch(
        packages_to_install=[
            # -*- Virtualenv packages to install: -*-
            'github-tools',
            "nose",
            "Sphinx>=0.6b1",
            "pkginfo", 
            "virtualenv"],
        dest_dir='./virtual-env/',
        install_paver=True,
        script_name='bootstrap.py',
        paver_command_line=None
        ),
    )

options.setup.package_data=paver.setuputils.find_package_data(
    'neuronvisio', package='neuronvisio', only_in_packages=False)

if ALL_TASKS_LOADED:
    @task
    @needs('generate_setup', 'minilib', 'setuptools.command.sdist', 
           'gh_pages_build_fix', 'build_pdf')
    def sdist():
        """Overrides sdist to make sure that our setup.py is generated."""
        print "Package baked."
        
@task
@needs(['gh_pages_build'])
def gh_pages_build_fix():
    """Generate the html and fix the _images with image
    
    Bug submitted: http://github.com/dinoboff/github-tools/issues#issue/10
    """
    import glob
    import os.path
    
    root_dir = 'docs/_build/html/'
    for filename in glob.glob(os.path.join(root_dir, '*.html')):
        f = open(filename, 'r')
        buffer = ""
        try:
            for line in f:
                buffer += line.replace('_images', 'images')
        except:
            pass
        f.close()
        # reopen and rewriting
        f = open(filename, 'w')
        f.write(buffer)
        f.close()
    print "html documentation fixed."
    
@task
def build_pdf():
    """Build the User Manual"""
    import os
    from subprocess import call
    root = os.getcwd()
    docs = os.path.join(root, 'docs')
    pdf_building = os.path.join(docs, '_build/pdf/')
    manual_filename = 'Neuronvisio_User_Manual.pdf'
    print "root dir: %s, docs dir: %s" %(root, docs)
    
    # building latex
    call(['sphinx-build', '-b', 'latex', docs, pdf_building])
    
    # building pdf
    os.chdir(pdf_building)
    call(['pdflatex', 'neuronvisio.tex'])
    # second round for the toc
    call(['pdflatex', 'neuronvisio.tex'])
    
    #copying the file
    os.rename(os.path.join(pdf_building, 'neuronvisio.pdf'), 
              os.path.join(docs, manual_filename))
    print "Usual Manual created in the docs dir"

@task
def build_and_upload_source_deb(package_ver):
    """Build a source debian package of the version supplied"""
    from subprocess import call
    import os.path
    dist_dir = 'dist'
    taball = os.path.join('dist', package_ver)
    call(['py2dsc', tarball])
    os.chdir(dist_dir)
    call(['debuild', '-S', '-sa'])
    os.chdir('..')
    package_src_changes = package_ver + '_source.changes'
    call(['dput', 'neuronvisio-ppa', os.path.join('deb_dist', 
                                                  package_src_changes)])
