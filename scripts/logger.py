import logging

logging.basicConfig(level=logging.INFO, 
    format='%(asctime)s:%(levelname)s:%(message)s', filename='history.log')

logging.info('hello 2')

logging.info('hello 3')

logging.info('user starts authorization')

logging.debug('user: Mike age 20 account #30')

try:
    b = 10 / 0 
    #raise Exception('wrong age')
except Exception as e:
    logging.error(e)

logging.info('user ends authorization')

def authorize_user(user: str) -> None:
    logging.info('start authorizing user')

    try:
        a = print('action: validatation ....')
        logging.debug('user validation success' + a)
    except Exception as e:
        logging.error(e)

    try:
        b = print('action: saving in user store ....')
        logging.debug('user validation success' + b)

    except Exception as e:
        logging.error(e)

    try:
        c = print('action: sending email invitation to user ....')
    except Exception as e:
        logging.error(e)

    logging.info('success authorizing user')