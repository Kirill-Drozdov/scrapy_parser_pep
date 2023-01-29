from pep_parse.constants import ALLOWED_STATUS


def parse_status(response):
    tags = response.css('dd')
    for tag in tags:
        text = tag.css('abbr::text').get()
        if text in ALLOWED_STATUS:
            return text
    return 'Unexisting status!'
