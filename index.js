import bedrock from 'bedrock-protocol';
import fs from 'fs';
import { GeminiAI } from './geminiAI.js';
import { Pathfinder } from './pathfinding.js';
import { BotActions } from './botActions.js';

const config = JSON.parse(fs.readFileSync('./config.json', 'utf8'));

class MinecraftBot {
  constructor() {
    this.client = null;
    this.gemini = new GeminiAI(config.gemini.apiKey);
    this.pathfinder = null;
    this.actions = null;
    this.position = { x: 0, y: 0, z: 0 };
    this.players = {};
    this.username = config.botName;
    this.isProcessing = false;
  }

  async connect() {
    console.log(`🤖 Conectando ao servidor ${config.server.host}:${config.server.port}...`);
    console.log(`👤 Nome do bot: ${this.username}`);

    try {
      this.client = bedrock.createClient({
        host: config.server.host,
        port: config.server.port,
        username: this.username,
        offline: true,
        version: config.server.version,
        skipPing: true,
        conLog: console.debug.bind(console)
      });

      this.pathfinder = new Pathfinder(this);
      this.actions = new BotActions(this, this.pathfinder);

      this.setupEventHandlers();

    } catch (error) {
      console.error('❌ Erro ao conectar:', error.message);
      console.log('⏳ Tentando reconectar em 10 segundos...');
      setTimeout(() => this.connect(), 10000);
    }
  }

  setupEventHandlers() {
    this.client.on('spawn', () => {
      console.log('✅ Bot conectado e spawnou no servidor!');
      console.log(`📍 Aguardando comandos com o prefixo: ${config.commandPrefix}`);
      
      setTimeout(() => {
        this.sendChat('Olá! Sou o bot Hailgames, controlado por IA. Use !BOT seguido do seu comando para me controlar!');
      }, 2000);
    });

    this.client.on('join', () => {
      console.log('✅ Bot entrou no servidor!');
    });

    this.client.on('start_game', (packet) => {
      console.log('🎮 Jogo iniciado!');
      if (packet.position) {
        this.position = packet.position;
      }
    });

    this.client.on('move_player', (packet) => {
      if (packet.runtime_id === this.client.entityId) {
        this.position = {
          x: packet.position.x,
          y: packet.position.y,
          z: packet.position.z
        };
      }
    });

    this.client.on('add_player', (packet) => {
      console.log(`👤 Jogador entrou: ${packet.username}`);
      this.players[packet.username] = {
        runtimeId: packet.runtime_id,
        position: packet.position || { x: 0, y: 0, z: 0 }
      };
    });

    this.client.on('player_list', (packet) => {
      if (packet.records && packet.records.records) {
        packet.records.records.forEach(player => {
          if (player.username && player.username !== this.username) {
            console.log(`📋 Jogador na lista: ${player.username}`);
            if (!this.players[player.username]) {
              this.players[player.username] = {
                uuid: player.uuid,
                position: { x: 0, y: 0, z: 0 }
              };
            }
          }
        });
      }
    });

    this.client.on('text', async (packet) => {
      try {
        const message = packet.message || '';
        const playerName = packet.source_name || packet.xuid || 'Jogador';

        if (playerName === this.username || !message) return;

        console.log(`💬 ${playerName}: ${message}`);

        if (message.startsWith(config.commandPrefix)) {
          const command = message.substring(config.commandPrefix.length).trim();
          
          if (command) {
            await this.handleCommand(command, playerName);
          }
        }
      } catch (error) {
        console.error('❌ Erro ao processar mensagem:', error);
      }
    });

    this.client.on('disconnect', (packet) => {
      const reason = packet.message || packet.reason || 'Sem motivo especificado';
      console.log('❌ Desconectado do servidor:', reason);
      console.log('⏳ Tentando reconectar em 10 segundos...');
      setTimeout(() => this.connect(), 10000);
    });

    this.client.on('error', (error) => {
      console.error('❌ Erro no cliente:', error.message);
    });

    this.client.on('kick', (reason) => {
      console.log('❌ Kickado do servidor:', reason);
      console.log('⏳ Tentando reconectar em 10 segundos...');
      setTimeout(() => this.connect(), 10000);
    });

    this.client.on('close', () => {
      console.log('🔌 Conexão fechada');
    });
  }

  async handleCommand(command, playerName) {
    if (this.isProcessing) {
      this.sendChat('Aguarde, ainda estou processando o comando anterior!');
      return;
    }

    this.isProcessing = true;
    console.log(`🤖 Processando comando de ${playerName}: "${command}"`);

    try {
      const playerData = this.players[playerName] || {};
      const playerPosition = playerData.position || this.position;

      const context = {
        botPosition: this.position,
        playerName: playerName,
        playerPosition: playerPosition
      };

      const actionData = await this.gemini.processCommand(command, context);
      console.log('🧠 Gemini respondeu:', JSON.stringify(actionData, null, 2));

      await this.actions.executeAction(actionData, playerName, playerPosition);

    } catch (error) {
      console.error('❌ Erro ao executar comando:', error);
      this.sendChat('Desculpe, tive um erro ao processar seu comando.');
    } finally {
      this.isProcessing = false;
    }
  }

  sendChat(message) {
    try {
      if (!this.client) return;
      
      this.client.queue('text', {
        type: 'chat',
        needs_translation: false,
        source_name: this.username,
        xuid: '',
        platform_chat_id: '',
        message: message
      });
      console.log(`📤 [BOT]: ${message}`);
    } catch (error) {
      console.error('❌ Erro ao enviar mensagem:', error.message);
    }
  }

  queue(packetName, data) {
    try {
      if (this.client) {
        this.client.queue(packetName, data);
      }
    } catch (error) {
      console.error(`❌ Erro ao enviar pacote ${packetName}:`, error.message);
    }
  }

  lookAt(yaw, pitch) {
  }

  get jump() {
    return this._jump || false;
  }

  set jump(value) {
    this._jump = value;
  }

  get moveDirection() {
    return this._moveDirection || { x: 0, y: 0, z: 0 };
  }

  set moveDirection(value) {
    this._moveDirection = value;
  }
}

const bot = new MinecraftBot();
bot.connect();

process.on('SIGINT', () => {
  console.log('\n👋 Encerrando bot...');
  if (bot.client) {
    bot.client.close();
  }
  process.exit(0);
});

process.on('uncaughtException', (error) => {
  console.error('❌ Erro não capturado:', error.message);
});

process.on('unhandledRejection', (error) => {
  console.error('❌ Promise rejeitada:', error.message);
});
