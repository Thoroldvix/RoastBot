# Roast Bot

Roast Bot is a small Discord bot that uses the OpenAI API to roast you in the style of Shakespeare or in the Japanese language when you react to a message with a specific emoji. It adds a touch of literary flair to your Discord server!

## Installation

To install and run Roast Bot, follow these steps:

1. Clone the repository or download the source code.

2. Make sure you have Python 3.6 or higher installed on your system.

3. Install the required dependencies by running the following command in your terminal or command prompt:

```bash
pip install -r requirements.txt
```

4. Obtain your Discord bot token and OpenAI API key.

5. Run the bot using the following command:

```bash
cd directory/with/script
$env:DISCORD_TOKEN="your_token"; $env:OPENAI_KEY="your_token"; $env:JAPANESE_ROAST_REACTION="your_reaction"; $env:CLASSY_ROAST_REACTION="your_reaction"; python main.py

```

Replace your_token with your Discord bot token, your_key with your OpenAI API key, your_emoji with the corresponding emoji for Japanese roast, and your_emoji with the emoji for the classy roast.

6. Invite the bot to your Discord server using the OAuth2 URL generated for your bot. Here's how you can do it:

   * Go to the Discord Developer Portal.
   * Create a new application and navigate to the "Bot" section.
   * Click on "Add Bot" to create a bot for your application. 
   * Copy the "Client ID" of your bot and replace the <YOUR_CLIENT_ID> in the following URL: https://discord.com/oauth2/authorize?client_id=<YOUR_CLIENT_ID>&scope=bot.
   * Open the generated URL in your web browser and select the server where you want to add the bot. Follow the instructions to add the bot to your server.
   * Once the bot is in your server, you can react to a message with a specific emoji to receive a creative roast!

## Usage

To use Roast Bot, follow these steps:

1. Make sure the bot is running and connected to your Discord server.

2. In your Discord server, navigate to a channel where the bot has access.

3. Send a message that you want to react to with a roast.

4. React to the message with one of the emojis that you provided via environment variable:

The bot will respond with a creative roast in the corresponding style!
