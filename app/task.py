from pytz import timezone
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
locale = timezone('Asia/Shanghai')


class Task:


update_period = self.config.get("update_period")
   if update_period:
        log.info("启动自动刷新程序")
        self.load_index_scheduler = BackgroundScheduler()
        self.load_index_scheduler.add_job(self.Load_item_embedding, CronTrigger.from_crontab(update_period))
        self.load_index_scheduler.start(paused=False)
    else:
        raise AttributeError("必须指定update_period")
