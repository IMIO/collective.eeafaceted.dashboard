# encoding: utf-8

from collective.eeafaceted.z3ctable.interfaces import IFacetedColumn
from zope.component import getGlobalSiteManager
from zope.globalrequest import getRequest
from zope.i18n import translate
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


CURRENT_CRITERION = 'querynextprev.current_criterion'


class CustomViewFieldsVocabularyAdapter(object):
    """Handles customViewFields for default plone.app.contenttypes collection."""

    def __init__(self, context):
        self.context = context
        self.request = getRequest()

    def __call__(self):
        """See docstring in interfaces.py."""

        gsm = getGlobalSiteManager()
        columns = [adapter.name for adapter in list(gsm.registeredAdapters())
                   if issubclass(adapter.provided, IFacetedColumn)]

        terms = [
            SimpleTerm(
                name,
                translate(name,
                          'collective.eeafaceted.z3ctable',
                          context=self.request).encode('utf-8')) for name in columns]

        return SimpleVocabulary(terms)
