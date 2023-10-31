const Discord = require("discord.js");
const fetch = require("node-fetch");
const {
  freecpu,
  getTimeout,
  getAccount,
  enBal,
  getFreeTrans,
} = require("../../transaction");
var moment = require("moment");
const config = require("config");

function getdocs(input) {
  return new Promise((resolve, reject) => {
    $.ajax({
      type: "POST",
      url: "/server/getdocs.py",
      data: { param: input },
      success: (response) => {
        resolve(response);
      },
      error: (error) => {
        reject(error);
      },
    });
  });
}

postData("data to process");

module.exports = {
  //Command Information
  name: "getapi",
  description: "get information from API in human readable form",
  usage: "getapi\ngetapi [command]",
  enabled: true,
  aliases: [],
  category: "langchain",
  memberPermissions: [],
  botPermissions: ["SEND_MESSAGES", "EMBED_LINKS"],
  nsfw: false,
  cooldown: 3000,
  ownerOnly: false,

  execute(client, message, args, data) {
    async () => {
      if (config["channels"].includes(message.channel.id)) {
        if (!args[0]) {
          let content =
            `${message.author} ` +
            ` Please ask me something about alien worlds technical docs!`;
          return message.channel.send(content);
        } else {
          try {
            const question = args.join(" ");
            const answer = await getapi(question);
            return message.channel.send(answer);
          } catch (error) {
            console.error(error);
            return message.channel.send(
              "An error occurred while fetching data."
            );
          }
        }
      }
    };
  },
};
