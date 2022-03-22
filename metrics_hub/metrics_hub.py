from .pipeline import MailchimpPipeline, SalesforcePipeline, MailgunPipeline


class MetricsHub():
    error_reports = []
    pipelines = [
        MailchimpPipeline,
        SalesforcePipeline,
        MailgunPipeline,
        # ... other pipelines
    ]

    def start(self):
        for pipeline in self.pipelines:
            new_pipeline = pipeline()
            try: 
                new_pipeline.start()
            except Exception as e:
                print("Adding error report to list...")
                self.error_reports.append(e)
        if len(self.error_reports) > 0:
            print(
                f"{len(self.error_reports)} of {len(self.pipelines)} pipelines failed")
            print(f"Emailing error report...\n")
            print(self.error_reports)
            # add email logic here
            return
        print("All pipelines ran successfully")
