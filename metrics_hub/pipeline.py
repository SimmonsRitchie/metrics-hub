from abc import ABC, abstractmethod

from metrics_hub.dummy_data import DUMMY_MAILCHIMP_DATA, DUMMY_MAILGUN_DATA, DUMMY_SALESFORCE_DATA


class Pipeline(ABC):

    @property
    @abstractmethod
    def name(self):
        # This is a python/ABC trick to ensure that each subclass has to 
        # implement a name property
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
        raise e

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
        return DUMMY_SALESFORCE_DATA

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
