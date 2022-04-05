from tools import is_prime


def next_prime(update, context):
    x = context.args
    if len(x) != 1:
        update.message.reply_text(f'НЕПРАВИЛЬНО!')
    elif not x[0].isdigit():
        update.message.reply_text(f'НЕПРАВИЛЬНО!')
    else:
        x = int(x[0]) + 1
        while not is_prime(x):
            x += 1
        update.message.reply_text(f'OTBET: {x}')
