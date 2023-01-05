from .constants import EXT, RESULTS_DIR

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

FEED_EXPORT_FIELDS = {
    'number': 'Номер',
    'name': 'Имя',
    'status': 'Статус',
}
FEEDS = {
    f'{RESULTS_DIR}/pep_%(time)s.csv': {
        'format': EXT,
        # 'fields': ['number', 'name', 'status'],
        'overwrite': False,
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
