from django_cron import CronJobBase, Schedule
from scrapperapp.services.service import scrape_and_save
from scrapperapp.models import Domain

class ScrapeCronJob(CronJobBase):
    RUN_EVERY_MINS = 60
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = "scrapperapp.scrape_cron_job"

    def do(self):
        domains = Domain.objects.all()
        for domain in domains:
            scrape_and_save(domain.name)
