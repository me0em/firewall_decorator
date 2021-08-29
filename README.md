# firewall_decorator
Decorate python-telegram-bot handlers to allow different groups of users to run them

#### Using
Create a yaml config **privileges.yml** with groups of users and the error message, i.e:
```
admins:
  - chat_id_1
  - chat_id_2
access_denied_msg: you can't use this bot right now
```
Then you can decorate your handlers and allow any of your user groups to run them

```
>>> @firewall(mode="admins")
>>> def send_info(update, context):
>>>     context.bot.send_message(
>>>     chat_id=update.effective_message.chat_id,
>>>     text="password: 1488"
>>> )
```
