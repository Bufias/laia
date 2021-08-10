import psutil
import notify2

from apscheduler.schedulers.blocking import BlockingScheduler


MAX_CHARGE_PERCENTAGE = 80
MIN_CHARGE_PERCENTAGE = 50
MINUTES_SCHEDULE = 5


class Notifier:

    def __init__(self):
        notify2.init("Battery")
        self.urgency = notify2.URGENCY_CRITICAL
        self.timeout = 1000

        self.notification = notify2.Notification("Battery level")
        self.notification.set_urgency(self.urgency)
        self.notification.set_timeout(self.timeout)

    def notify(self, current_percent, action):
        summary = f"Battery at {current_percent}%!"
        msg = f"Please {action} the laptop."

        self.notification.update(summary, msg)
        self.notification.show()

    def notify_min(self, current_percent):
        action = "PLUG"
        self.notify(current_percent, action)

    def notify_max(self, current_percent):
        action = "UNPLUG"
        self.notify(current_percent, action)


def check_battery(notifier):
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    current_percent = round(battery.percent, 2)

    if plugged and current_percent > MAX_CHARGE_PERCENTAGE:
        notifier.notify_max(current_percent)
    elif not plugged and current_percent < MIN_CHARGE_PERCENTAGE:
        notifier.notify_min(current_percent)


def main():
    notifier = Notifier()

    scheduler = BlockingScheduler()
    scheduler.add_job(
        lambda: check_battery(notifier), 'interval', minutes=MINUTES_SCHEDULE
    )
    scheduler.start()


if __name__ == "__main__":
    main()
