# coding=utf-8
from zope.schema import TextLine, Text, Choice
from gs.group.properties.interfaces import IGroupProperties
from zope.schema.vocabulary import SimpleVocabulary
import pytz


class IEDemGroupProperties(IGroupProperties):
    ptn_coach_id = TextLine(title=u'Participation Coach ID',
        description=u'The groupserver profile ID of the primary '\
          u'participation coach/forum manager.',
        required=True)
    group_tz = Choice(title=u'Timezone',
      description=u'The timezone you wish to use as the default for the group '\
            'and users who join via the group.',
      required=True,
      default=u'US/Central',
      vocabulary=SimpleVocabulary.fromValues(pytz.common_timezones))
    facebookId = TextLine(title=u'Facebook ID',
        description=u'The ID of the group on Facebook, if the group has an '\
          u'associated Facebook account.',
        required=False)
    twitterId = TextLine(title=u'Twitter ID',
        description=u'The ID of the group on Twitter, if the group has a '\
                     'associated twitter account.',
        required=False)
    footer = Text(title=u'Additional Email Footer',
        description=u'A short snippet of text which will be displayed in the '\
          u'footer of group emails.',
        required=False)
