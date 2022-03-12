import yaml

def firewall(mode="all"):
    """ Firewall decorator
    Checks functions or method execution privileges
    Example of using:
    >>> @firewall(mode="admins")
    >>> def send_info(update, context):
    >>>     context.bot.send_message(
    >>>     chat_id=update.effective_message.chat_id,
    >>>     text="password: 1488"
    >>> )
    >>> pass
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) == 2:
                update, context = args
            elif len(args) == 3:
                _, update, context = args

            if update.callback_query is not None:
                chat_id = update.callback_query.message.chat_id
            else:
                if hasattr(update.message, "chat_id"):
                    chat_id = update.message.chat_id
                else:
                    chat_id = update.message.chat.id


                

            with open("privileges.yml", "r") as file:
                privileges = yaml.safe_load(file)

            if mode != "all" and mode not in privileges:
                raise AssertionError(
                    "Syntax error: can't find firewall mode in yaml"
                )

            if chat_id in privileges[mode] or mode == "all":
                return func(*args)
            else:
                context.bot.send_message(
                    chat_id=chat_id,
                    text=privileges["access_denied_msg"]
                )

        return wrapper
    return decorator
