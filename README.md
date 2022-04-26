# Zapier Telegram Bot

Telegram bot that sends messages to Zapier and other webhooks

Copy `.envrc_template` to `.envrc` and replace the TODOs.

Next, either use direnv or evaluate the content of `.envrc`:

```bash
eval $(cat .envrc)
```

## Bot listener

Start the bot in the listener mode:

```bash
python main.py
```

Send it messages or use the `/todo` command in groups. It will forward the request to Zapier where you can do everything you want 

## Scheduled messages

For recurring tasks, you can use cron for scheduling them.

Copy `message_templates.json` to `messages.json` and edit it. 

Then you can send messages:

```bash
./send.sh message_id
```

For scheduling it with cron, use crontab:

```bash
crontab -e
```

And add:

```cron
0 5 * * WED /home/ubuntu/zapier-telegram-bot/send.sh newsletter_wednesday_reminder
```

Example of `messages.json`:

```json
{
    "newsletter_wednesday_reminder": {
        "message": "Prepare a newsletter for the next week!",
        "chat_id": -12345
    },
    "template": "New TODO item added:\n\n{message}"
}
```



