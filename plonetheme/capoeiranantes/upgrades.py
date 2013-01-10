import logging
from Products.CMFCore.utils import getToolByName
from plone.app.controlpanel.security import ISecuritySchema
POLICY = 'plonetheme.capoeiranantes'
PROFILE = 'profile-%s:default' % POLICY

UNINSTALLS = ('collective.js.nivoslider',
              'collective.js.fitvids',
              'collective.js.imagesloaded')


def quickinstall_addons(context, install=None, uninstall=None, upgrades=None):
    logger = logging.getLogger(PROFILE)
    qi = getToolByName(context, 'portal_quickinstaller')
    installedProducts = qi.listInstalledProducts(showHidden=True)

    if uninstall is not None:
        qi.uninstallProducts(uninstall)

    if install is not None:
        for addon in install:
            if qi.isProductInstallable(addon):
                qi.installProduct(addon)
            else:
                logger.error('%s can t be installed' % addon)

    if upgrades is not None:
        if upgrades in ("all", True):
            #TODO: find which addons should be upgrades
            installedProducts = qi.listInstalledProducts(showHidden=True)
            upgrades = [p['id'] for p in installedProducts]
        for upgrade in upgrades:
            # do not try to upgrade myself -> recursion
            if upgrade == POLICY:
                continue
            try:
                qi.upgradeProduct(upgrade)
            except KeyError:
                logger.error('can t upgrade %s' % upgrade)


def configure_extra(context):
    """To configure extra features not already managed by genericsetup"""

    portal_url = getToolByName(context, 'portal_url')
    portal = portal_url.getPortalObject()
    security = ISecuritySchema(portal)

    if not security.enable_self_reg:
        security.enable_self_reg = True

#    if not security.enable_user_pwd_choice:
#        security.enable_user_pwd_choice = True

    if not security.enable_user_folders:
        security.enable_user_folders = True

    if not security.use_email_as_login:
        security.use_email_as_login = True


def common(context):
    logger = logging.getLogger(PROFILE)

    portal_migration = getToolByName(context, 'portal_migration')
    portal_migration.upgrade()
    logger.info("Ran Plone Upgrade")

    #upgrades installed addons
    quickinstall_addons(context, upgrades=True, uninstall=UNINSTALLS)

    context.runAllImportStepsFromProfile(PROFILE)

    configure_extra(context)
    logger.info("Apply %s" % PROFILE)
    #cleanup
    remove_old_jqueryui(context)


def remove_old_jqueryui(context):
    jsregistry = getToolByName(context, 'portal_javascripts')
    base = '++resource++jquery-ui/jquery.'
    plugins = ['ui.core', 'ui.widget', 'ui.mouse', 'ui.position',
               'ui.draggable', 'ui.droppable', 'ui.resizable', 'ui.selectable',
               'ui.sortable', 'ui.accordion', 'ui.autocomplete', 'ui.button',
               'ui.dialog', 'ui.slider', 'ui.tabs', 'ui.datepicker',
               'ui.progressbar', 'effects.core', 'effects.blind',
               'effects.bounce', 'effects.clip', 'effects.drop',
               'effects.explode', 'effects.fade', 'effects.fold',
               'effects.highlight', 'effects.pulsate', 'effects.scale',
               'effects.shake', 'effects.slide', 'effects.transfer']
    for plugin in plugins:
        jsregistry.unregisterResource('%s%s.min.js' % (base, plugin))

    jsregistry.unregisterResource('++resource++jquery-ui-i18n.js')

    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile('profile-collective.js.jqueryui:default',
                               'jsregistry', run_dependencies=False,
                               purge_old=False)

    jsregistry.cookResources()
