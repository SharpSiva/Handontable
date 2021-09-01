import logging

class Log_generate:
    @staticmethod
    def log_gen():
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler = logging.FileHandler(filename='.\\Log_files\\automation.log')
        handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        return logger

