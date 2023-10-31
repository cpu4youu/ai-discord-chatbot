const Discord = require('discord.js');
const config = require('config'),
    fs = require('fs'),
    util = require('util'),
    readdir = util.promisify(fs.readdir);

const token = config.get("token");
var CronJob = require('cron').CronJob;

const client = new Discord.Client({ intents: ['GUILDS', 'GUILD_MESSAGES']});
client.commands = new Discord.Collection();
client.cooldowns = new Discord.Collection();
client.logger = require('./modules/logger.js');
client.tools = require("./modules/tools.js");



// var job_left = new CronJob('*/5 * * * *', async function() {
//   var data = await getInfo();
//   let left = Number((parseFloat(data["total_wax"]) - parseFloat(data["current_loaned"])).toFixed(2))
//   var voiceChannelleft = client.channels.resolve('channel number');
//   voiceChannelleft.setName(`Free-WAX-${left}`)
// }, null, true, 'America/Los_Angeles');


async function startUp(){

    //Starting all events
    const eventFiles = fs.readdirSync('./events/').filter(file => file.endsWith('.js'));
    for (const file of eventFiles) {
        const event = require(`./events/${file}`);
        const eventName = file.split(".")[0];
        client.logger.event(`Loading Event - ${eventName}`);
        client.on(eventName, event.bind(null, client));
      };
    
    //Load all the commands
    let folders = await readdir("./commands/");
    folders.forEach(direct =>{
      const commandFiles = fs.readdirSync('./commands/' + direct + "/").filter(file => file.endsWith('.js'));
      for (const file of commandFiles) {
          const command = require(`./commands/${direct}/${file}`);
          client.commands.set(command.name, command);
        };
      });
    
      client.login(token);
      job_left.start()
      job_total.start()
      job_free.start()
      job_rate.start()
    };

startUp();

//Error Logging
client.on("disconnect", () => client.logger.log("Bot is disconnecting...", "warn"))
    .on("reconnecting", () => client.logger.log("Bot reconnecting...", "log"))
    .on("error", (e) => client.logger.log(e, "error"))
    .on("warn", (info) => client.logger.log(info, "warn"));

//Logging unhandeld errors
process.on("unhandledRejection", (err) => {
    console.error(err);
    });   

module.exports = {client};