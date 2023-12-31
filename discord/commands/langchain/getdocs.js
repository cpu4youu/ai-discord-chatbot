const Discord = require("discord.js");
const fetch = require("node-fetch");
var moment = require("moment");
const config = require("config");
const spawn = require("child_process").spawn;

function getdocs(input) {
  return new Promise(function (resolve, reject) {
    const process = spawn("python3", ["server/getdocs.py", input]);
    var output;

    process.stdout.on("data", function (data) {
      console.log("Got data back");
      console.log("here it is: -- ", new TextDecoder().decode(data));
      output = new TextDecoder().decode(data);
    });

    process.on("close", function (code) {
      // Should probably be 'exit', not 'close'
      // *** Process completed
      console.log("Closing spawn");
      resolve(output);
    });

    process.on("error", function (err) {
      // *** Process creation failed
      reject(err);
    });
  });
}

module.exports = {
  //Command Information
  name: "getdocs",
  description:
    "get information from the technical blueprint in human readable form",
  usage: "getdocs @message",
  enabled: true,
  aliases: ["gd"],
  category: "langchain",
  memberPermissions: [],
  botPermissions: ["SEND_MESSAGES", "EMBED_LINKS"],
  nsfw: false,
  cooldown: 3000,
  ownerOnly: false,

  execute(client, message, args, data) {
    (async () => {
      if (!args[0]) {
        let content =
          `${message.author} ` +
          ` Please ask me something about the tehcnical blieprint!`;
        return message.channel.send(content);
      } else {
        try {
          const startTime = Date.now();
          const question = args.join(" ");
          console.log("Opening spawn");
          const answer = await getdocs(question);
          const msElapsed = Date.now() - startTime;
          return message.reply(
            answer +
              "\n AI query took " +
              msElapsed / 1000 +
              " seconds to complete."
          );
        } catch (error) {
          console.error(error);
          return message.channel.send("An error occurred while fetching data.");
        }
      }
    })();
  },
};
