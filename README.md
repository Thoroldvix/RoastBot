# Roast Bot using OpenAI API

Roast Bot is a small Discord bot that uses the OpenAI API to roast you in the style of Shakespeare when you react to a message with a specific emoji. The bot runs in a Docker container and can be deployed easily using the provided Docker image.

## Installation

### Prerequisites
- Docker installed on your machine

### Steps

1. Clone the repository:
```
git clone https://github.com/yourusername/roast-bot.git
```

2. Change directory into the repository:
```
cd roast-bot
```

3. Create a file named `.env` in the root of the repository and add the following environment variables:
```
DISCORD_TOKEN=your_discord_bot_token
OPENAI_API_KEY=your_openai_api_key
```
Replace `your_discord_bot_token` and `your_openai_api_key` with your Discord bot token and OpenAI API key respectively.

4. Build the Docker image:
```
docker build -t thorold/roast_bot .
```

5. Run the Docker container:
```
docker run --name roast-bot -d thorold/roast_bot
```

The bot is now running in a Docker container with the name `roast-bot`. You can view the logs of the container using the command `docker logs roast-bot`.

6. Add the bot to your Discord server:
   - Create a Discord bot account and get its token
   - Go to the Discord Developer Portal and add a new application
   - Navigate to the Bot tab and add a new bot
   - Copy the bot token and add it to your server using the following URL, replacing `YOUR_BOT_TOKEN` with your bot token: 
   ```
   https://discord.com/oauth2/authorize?client_id=YOUR_BOT_TOKEN&scope=bot
   ```

7. React to a message with the  emoji to trigger the bot to roast you in the style of Shakespeare.

## Usage

React to a message with the  emoji to trigger the bot to generate a Shakespearean insult based on the message. The bot will respond to the channel with the insult.
