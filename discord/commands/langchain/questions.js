const Discord = require("discord.js");

module.exports = {
    //Command Information
    name: "examples",
    description: "Get a list of questions the chatbot can easily answer",
    usage: "questions\nquestions [command]",
    enabled: true,
    aliases: [],
    category: "langchain",
    memberPermissions: [],
    botPermissions: [ "SEND_MESSAGES", "EMBED_LINKS" ],
    nsfw: false,
    cooldown: 3000,
    ownerOnly: false,

    async execute(client, message, args, data) {
        try {
          const answer = "Here are a few examples of questions I can answer for you: \n \
          Using $$getdaoapi Who is a custodian on kavian? \n \
          Usins $$getdaoapi Who are the custodians for the dac naron? \n \
          Using $$getdaoapi Who were the last 5 people to vote for 42lra.wam on dac naron? \n \
          Using $$getdaoapi Who are the candidates on dac magor? \n \
          Using $$getdaoapi Who did t1dbe.wam vote for the last 2 times on dac naron? \n \
          Using $$getdocs How do the mining pools fill with tlm? \n";
          return message.reply(answer);
        } catch (error) {
          console.error(error);
          return message.channel.send(
            "An error occurred while sending data."
          );
        }
    },
};