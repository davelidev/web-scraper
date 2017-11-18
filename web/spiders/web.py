import scrapy
import os
import datetime

class WebSpider(scrapy.Spider):
    name = 'web'

    def __init__(self, base_url='', default_path="resources", folder_name='', year=''):
        assert base_url != '' and folder_name != ''

        self.default_path = default_path
        self.start_urls = [base_url]
        if '.' in base_url:
            base_url = '/'.join(base_url.split('/')[:-1])
        self.allowed_prefix = base_url.rstrip('/') + '/'
        year = year if year else datetime.datetime.now().year
        self.folder_name = "%s-%s" %(folder_name, year)
        self.allowed_domains = []

        assert not os.path.exists("%s/%s" %(self.default_path, self.folder_name))

        for url in self.start_urls:
            self.allowed_domains.append(url.split('/')[2])
        scrapy.Spider.__init__(self)

    def parse(self, response):
        yield {'url': response.url}

        full_path = "%s/%s/%s" % (self.default_path, self.folder_name, response.url[len(self.allowed_prefix):])
        directory = full_path[:full_path.rfind('/')]
        file_name = full_path[full_path.rfind('/') + 1:]
        if not file_name:
            full_path = full_path + "index.html"
        try:
            os.makedirs(directory)
        except:
            pass

        with open(full_path, 'wb') as f:
            f.write(response.body)

        if response.headers['Content-Type'] == 'text/html':
            content = open(full_path).read()
            f = open(full_path, 'w')
            f.write(content.replace(self.allowed_prefix, '').replace('/' + '/'.join(self.allowed_prefix.split('/')[3:]), ''))
            next_pages = response.css('*::attr(href)').extract()
            for page in next_pages:
                if page is not None:
                    new_link = response.urljoin(page)
                    if new_link.startswith(self.allowed_prefix):
                        yield scrapy.Request(new_link, callback=self.parse)