# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import od4dasia.theme


class Od4DasiaThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=od4dasia.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'od4dasia.theme:default')


OD4DASIA_THEME_FIXTURE = Od4DasiaThemeLayer()


OD4DASIA_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(OD4DASIA_THEME_FIXTURE,),
    name='Od4DasiaThemeLayer:IntegrationTesting',
)


OD4DASIA_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(OD4DASIA_THEME_FIXTURE,),
    name='Od4DasiaThemeLayer:FunctionalTesting',
)


OD4DASIA_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        OD4DASIA_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='Od4DasiaThemeLayer:AcceptanceTesting',
)
