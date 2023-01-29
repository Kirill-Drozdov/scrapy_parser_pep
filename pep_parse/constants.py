from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

RESULTS_DIR = BASE_DIR / 'results'

RESULTS_PEP = [('Статус', 'Количество')]

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

FILE_NAME = 'status_summary_{}.csv'

ALLOWED_STATUS = ('Active',
                  'Accepted',
                  'Deferred',
                  'Final',
                  'Provisional',
                  'Rejected',
                  'Superseded',
                  'Withdrawn',
                  'Draft',
                  'Total')
