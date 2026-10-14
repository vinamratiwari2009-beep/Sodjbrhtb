# Vercel TW / HostP Request Notification

## Deploy
1. Upload this project to a private GitHub repository.
2. Import the repository into Vercel.
3. In Vercel Project Settings → Environment Variables, add:
   - `TELEGRAM_BOT_TOKEN` = your newly rotated Telegram bot token
   - `TELEGRAM_OWNER_ID` = your Telegram owner/chat ID
4. Redeploy the project.

## Test
After deployment, open:
`https://YOUR-PROJECT.vercel.app/request?tw=sample123&hostp=sample`

The endpoint sends a generic Telegram notification only. It does not store, log,
or forward either parameter value because `hostp` may contain a password or other
secret. Use HTTPS and only collect data users have knowingly agreed to share.

Important: if a bot token has been exposed in a chat, revoke it with BotFather
and use a newly generated token. Keep tokens out of source code and Git.
