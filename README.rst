.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============
test.migration
==============

Addon for Plone5.1 to get data from Plone4.

Features
--------

- Converts data from Archetypes to Dexterity



Installation
------------

Install test.migration and dependencies by adding it to your Plone5 buildout::

    [buildout]

    ...

    eggs =
        test.migration
        collective.jsonmigrator
        transmogrify.dexterity
        test.migration


and then running ``bin/buildout``



License
-------

The project is licensed under the GPLv2.
