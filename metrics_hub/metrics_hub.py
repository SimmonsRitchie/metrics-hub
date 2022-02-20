from pipeline import MailchimpPipeline, SalesforcePipeline, MailgunPipeline


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
            error_report = new_pipeline.start()
            if error_report:
                print("Adding error report to list...")
                self.error_reports.append(error_report)
        if len(self.error_reports) > 0:
            print(
                f"{len(self.error_reports)} of {len(self.pipelines)} pipelines failed")
            print(f"Emailing error report...\n")
            print(self.error_reports)
            # add email logic here
            return
        print("All pipelines ran successfully")


def main():
    m = MetricsHub()
    m.start()


if __name__ == "__main__":
    main()
