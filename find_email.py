#!../venv/bin/python3
# -*- coding: utf-8 -*-

import httplib2, re

def get_emails(url):
    '''Take a url and returns a list of email addresses that are in the page source code.
    This is part of a mechanical turk automation attempt.'''

    h = httplib2.Http('.cache')
    response, content = h.request(url)
    content = str(content)
    pattern = r'[\w\.-]+@[\w\.-]+'
    temp = re.findall(pattern, content, re.IGNORECASE)

    return temp

