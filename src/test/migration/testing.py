# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import test.migration


class TestMigrationLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=test.migration)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'test.migration:default')


TEST_MIGRATION_FIXTURE = TestMigrationLayer()


TEST_MIGRATION_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TEST_MIGRATION_FIXTURE,),
    name='TestMigrationLayer:IntegrationTesting',
)


TEST_MIGRATION_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(TEST_MIGRATION_FIXTURE,),
    name='TestMigrationLayer:FunctionalTesting',
)


TEST_MIGRATION_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        TEST_MIGRATION_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='TestMigrationLayer:AcceptanceTesting',
)
