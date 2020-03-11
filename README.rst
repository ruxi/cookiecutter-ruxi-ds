===================================
cookiecutter painless data science
===================================

|version| |tag| |coverage-codacy| |grade-codacy| |issues| |last commit|
| TravisCI |travis-ci| ShippableCI: |shippable-ci| CodeshipCI: |codeship-ci| 

Project template for reproducible data science using conda environments. This `cookiecutter`_ is forked from `painless-continuous-delivery`_ for continous integration support

The directory structure is based recommendations from `datadriven-datascience-cookiecutter`_

Boilerplate includes preloaded conda environment.yml of standard data science tools.  




.. |coverage-codacy| image:: https://img.shields.io/codacy/coverage/fd7f451342dc46b1ac0301d986f9b6a0/master.svg
   :target: https://img.shields.io/codacy/coverage/fd7f451342dc46b1ac0301d986f9b6a0

.. |grade-codacy| image:: https://img.shields.io/codacy/grade/fd7f451342dc46b1ac0301d986f9b6a0/master.svg
   :target: https://app.codacy.com/ruxi/grade/fd7f451342dc46b1ac0301d986f9b6a0

.. |shippable-ci| image:: https://img.shields.io/shippable/5e6888ca7cb7fa000657594e/master.svg
   :target: https://app.shippable.com/projects/5e6888ca7cb7fa000657594e
   :alt: Shippable

.. |codeship-ci| image:: https://img.shields.io/codeship/45a9ae30-4592-0138-3cfc-36e98d2c9ab6/master.svg
   :target: https://app.codeship.com/projects/45a9ae30-4592-0138-3cfc-36e98d2c9ab6
   :alt: codeship

   
.. |issues| image:: https://img.shields.io/github/issues/ruxi/cookiecutter-ruxi-ds/master.svg
   :target: https://img.shields.io/github/issues/ruxi/cookiecutter-ruxi-ds

.. |last commit| image::  https://img.shields.io/github/last-commit/ruxi/cookiecutter-ruxi-ds/master.svg
   :target: https://img.shields.io/github/last-commit/ruxi/cookiecutter-ruxi-ds

.. |version| image::  https://img.shields.io/github/v/release/ruxi/cookiecutter-ruxi-ds?include_prereleases/master.svg
   :target: https://img.shields.io/github/v/release/ruxi/cookiecutter-ruxi-ds?include_prereleases

.. |tag| image::  https://img.shields.io/github/v/tag/ruxi/cookiecutter-ruxi-ds?include_prereleases/master.svg
   :target: https://img.shields.io/github/v/tag/ruxi/cookiecutter-ruxi-ds?include_prereleases
   
.. |travis-ci| image:: https://img.shields.io/travis/ruxi/cookiecutter-ruxi-ds/master.svg
   :target: https://travis-ci.org/ruxi/cookiecutter-ruxi-ds
   :alt: Travis CI




.. |bitbucket-ci| image:: https://img.shields.io/bitbucket/pipelines/ruxi/cookiecutter-ruxi-ds/master.svg
   :target: https://bitbucket.org/ruxi/cookiecutter-ruxi-ds/addon/pipelines/home
   :alt: Bitbucket Pipelines



 
usage
===================================

Install `cookiecutter`_:

.. code-block:: bash

    conda install -c conda-forge cookiecutter

Generate a new Cookiecutter template layout:

.. code-block:: bash

    cookiecutter gh:ruxi/cookiecutter-ruxi-ds


.. |asciicast| image:: https://asciinema.org/a/244658.svg

.. code-block:: bash

    cd <name.of.your.project>

edit environment.yml to configure conda environment to your needs

.. code-block:: bash

   conda env update # create conda environment
   source activate <name.of.your.project>

add your project to github or bitbucket

.. code-block:: bash

   git init
   git add --all :/
   git commit -a -m 'first commit'
   git remote add origin git@github.com:<username>/<project name> # or use bitbucket.org
   git push origin master
     
----------



Under The Hood
==============

The underscore folder, ``{{cookiecutter.project_slug}}/_``, contains files
that are integrated by the post generate hook, ``hooks/post_gen_project.py``,
according to the choices made during the cookiecutter execution.

The ``generators`` folder contains scripts to pre-generate code skeletons
that are integrated manually in this cookiecutter (e.g. framework setups).

Please refer to the README files in those folders for additional details.



Credits
=======

Fork of `Painless Software`_ cookiecutter


References
==========

`rst cheatsheet <https://hyperpolyglot.org/lightweight-markup>`_


.. _ruxi: https://github.com/ruxi/cookiecutter-ruxi-ds
.. _field tests: tests/field/
.. _APPUiO, GitLab CI, Django: https://gitlab.com/appuio/example-django
.. _cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _painless-continuous-delivery: https://github.com/painless-software/painless-continuous-delivery
.. _datadriven-datascience-cookiecutter: https://drivendata.github.io/cookiecutter-data-science/
.. _Painless Software: https://painless.software/
