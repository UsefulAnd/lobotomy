import os


class Logger(object):
    @staticmethod
    def run_logger(args):
        with open("{0}/logs/log".format(os.getcwd()), "a") as log:
            log.writelines(args)
            log.close()
