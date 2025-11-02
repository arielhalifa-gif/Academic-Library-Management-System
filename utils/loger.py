import time

class Logger:
    @staticmethod
    def log_action(action_type: str, details: str) -> None:
        print(action_type, time.time)
        print(details)