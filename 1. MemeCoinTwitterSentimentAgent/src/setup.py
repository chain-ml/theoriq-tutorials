import logging

is_ready = False
is_live = True


def init() -> None:
    logging.info('message="starting background init"')
    global is_ready, is_live, model
    try:
        is_ready = is_live
        is_live = is_ready
        logging.info('message="background init completed"')
    except Exception as e:
        is_live = False
        logging.error(f'message="background init failed" error="{e}"')
