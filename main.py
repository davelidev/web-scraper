#!/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python

# -*- coding: utf-8 -*-

from scrapy.cmdline import execute
import os


if __name__ == '__main__':
    # sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    os.chdir('web_scraper')
    with open('../resources.txt') as f:
        context = f.read()
        for line in context.strip().split('\n'):
            if not line.strip().startswith('#'):
                line = line.split(" ")
                try:
                    url = folder = year = ''
                    if len(line) == 2:
                        url, folder = line
                    elif len(line) == 3:
                        url, folder, year = line
                        year = ' -a year=' + year
                    execute(("scrapy crawl web_scraper -a base_url=%s -a folder_name=%s%s" % (url, folder, year)).split())
                except:
                    pass