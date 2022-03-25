import logging
import queue
import threading
from time import sleep


def main():
    q = queue.Queue()

    def worker():
        i = 0
        while True:
            logging.info(f'Loop {i} started...')
            item = q.get()  # This is a blocking get
            logging.info(f'Working on {item}')
            logging.info(f'Finished {item}')
            q.task_done()
            logging.info(f'Loop {i} finished.')
            i += 1

    # Turn-on the worker thread.
    threading.Thread(target=worker, daemon=True).start()

    # Send thirty task requests to the worker.
    for item in range(10):
        q.put(item)
        q.put(item)
        sleep(1)

    # Block until all tasks are done.
    q.join()
    logging.info('All work completed')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(filename)s:%(funcName)s %(levelname)-7s %(message)s")
    main()
