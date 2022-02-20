from abc import ABC, abstractmethod

DUMMY_MAILCHIMP_DATA = [{
    'id': 1,
    'name': 'John',
},
    {
    'id': 2,
    'name': 'Jane',
},
    {
    'id': 3,
    'name': 'Jack',
}
]
DUMMY_SALESFORCE_DATA = [{
    'id': 1,
    'species': 'Dog',
},
    {
    'id': 2,
    'species': 'Cat',
},
    {
    'id': 3,
    'species': 'Bird',
}
]
DUMMY_MAILGUN_DATA = [{
    'id': 1,
    'brand': 'Samsung',
},
    {
    'id': 2,
    'brand': 'Apple',
},
    {
    'id': 3,
    'brand': 'Sony',
}
]


class Pipeline(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def fetch(self):
        pass

    @abstractmethod
    def transform(self, data):
        pass

    def upload(self, data):
        print(f"Uploading data to {self.name} table of DB...\n", data)

    def handle_error(self, e):
        print("Error:", e)
        # add other error handling here if needed, eg. slack notification
        return {
            'name': self.name,
            'error': str(e),
        }

    def start(self):
        try:
            data = self.fetch()
            transformed_data = self.transform(data)
            self.upload(transformed_data)
        except Exception as e:
            return self.handle_error(e)


class MailchimpPipeline(Pipeline):
    name = "mailchimp"

    def fetch(self):
        print(f"Fetching data from {self.name}...")
        return DUMMY_MAILCHIMP_DATA

    def transform(self, data):
        print(f"Transforming {self.name} data...")
        return [{'name': x['name'].upper(), **x} for x in data]


class SalesforcePipeline(Pipeline):
    name = "salesforce"

    def fetch(self):
        print(f"Fetching data from {self.name}...")
        # simulate error, so we can test error handling
        raise Exception("Something went wrong")

    def transform(self, data):
        print(f"Transforming {self.name} data...")
        return [{'species': x['species'].capitalize(), **x} for x in data]


class MailgunPipeline(Pipeline):
    name = "mailgun"

    def fetch(self):
        print(f"Fetching data from {self.name}...")
        return DUMMY_MAILGUN_DATA

    def transform(self, data):
        print(f"Transforming {self.name} data...")
        return [{'brand': x['brand'].capitalize(), **x} for x in data]
