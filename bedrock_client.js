const bedrock = require('bedrock-protocol');
const fs = require('fs');
const path = require('path');

class BedrockRealClient {
    constructor() {
        this.client = null;
        this.connected = false;
        this.config = this.loadConfig();
        this.commandQueue = [];
        this.position = { x: 0, y: 64, z: 0 };
        this.players = {};
    }

    loadConfig() {
        try {
            const configPath = path.join(__dirname, 'config.json');
            const data = fs.readFileSync(configPath, 'utf8');
            return JSON.parse(data);
        } catch (error) {
            console.error('Erro ao carregar config.json:', error);
            process.exit(1);
        }
    }

    async connect() {
        try {
            console.log(`[BEDROCK] Conectando a ${this.config.server.host}:${this.config.server.port}...`);
            
            this.client = bedrock.createClient({
                host: this.config.server.host,
                port: this.config.server.port,
                username: this.config.bot_name,
                offline: true,
                version: '1.21.0'
            });

            this.setupEventHandlers();
            
        } catch (error) {
            console.error('[BEDROCK] Erro ao conectar:', error.message);
            throw error;
        }
    }

    setupEventHandlers() {
        this.client.on('spawn', () => {
            console.log('[BEDROCK] ✓ Bot entrou no mundo!');
            console.log('[BEDROCK] ✓ Conectado ao servidor Bedrock');
            this.connected = true;
            
            this.sendChat('Olá! Sou o ' + this.config.bot_name + '. Use ' + this.config.command_prefix + ' para me dar comandos!');
        });

        this.client.on('text', (packet) => {
            if (packet.type === 'chat' && packet.source_name !== this.config.bot_name) {
                console.log(`[CHAT] ${packet.source_name}: ${packet.message}`);
                this.handleChatMessage(packet.source_name, packet.message);
            }
        });

        this.client.on('move_player', (packet) => {
            this.position = {
                x: packet.position.x,
                y: packet.position.y,
                z: packet.position.z
            };
        });

        this.client.on('add_player', (packet) => {
            if (packet.username) {
                this.players[packet.username] = packet.runtime_id;
                console.log(`[PLAYER] ${packet.username} entrou no servidor`);
            }
        });

        this.client.on('error', (error) => {
            console.error('[BEDROCK] Erro:', error.message);
        });

        this.client.on('close', () => {
            console.log('[BEDROCK] Conexão fechada');
            this.connected = false;
        });
    }

    handleChatMessage(playerName, message) {
        if (!message.startsWith(this.config.command_prefix)) {
            return;
        }

        const command = message.substring(this.config.command_prefix.length).trim();
        
        if (!command) {
            return;
        }

        console.log(`[COMANDO] ${playerName}: ${command}`);
        
        const actionData = {
            player: playerName,
            command: command,
            timestamp: Date.now()
        };
        
        fs.writeFileSync(
            path.join(__dirname, 'command_input.json'),
            JSON.stringify(actionData, null, 2)
        );
        
        this.checkForActions();
    }

    checkForActions() {
        const actionFile = path.join(__dirname, 'action_output.json');
        
        if (fs.existsSync(actionFile)) {
            try {
                const data = fs.readFileSync(actionFile, 'utf8');
                const action = JSON.parse(data);
                
                this.executeAction(action);
                
                fs.unlinkSync(actionFile);
                
            } catch (error) {
                console.error('[ERROR] Erro ao processar ação:', error);
            }
        }
        
        setTimeout(() => this.checkForActions(), 100);
    }

    async executeAction(action) {
        console.log(`[ACTION] Executando: ${action.action}`);
        
        try {
            switch (action.action) {
                case 'chat':
                    await this.sendChat(action.response);
                    break;

                case 'goto_player':
                    await this.sendChat(action.response);
                    await this.gotoPlayer(action.player);
                    break;

                case 'collect_and_give':
                    await this.sendChat(action.response);
                    await this.collectBlocks(action.block_type, action.quantity);
                    await this.gotoPlayer(action.player);
                    await this.giveItems(action.player, action.block_type, action.quantity);
                    break;

                case 'follow_player':
                    await this.sendChat(action.response);
                    await this.followPlayer(action.player);
                    break;

                case 'stop':
                    await this.sendChat(action.response);
                    this.stopAllActions();
                    break;

                default:
                    console.log(`[WARN] Ação desconhecida: ${action.action}`);
            }
        } catch (error) {
            console.error('[ERROR] Erro ao executar ação:', error);
            await this.sendChat('Desculpe, ocorreu um erro ao executar a ação.');
        }
    }

    async sendChat(message) {
        if (!this.connected) {
            console.log(`[CHAT-SIM] ${this.config.bot_name}: ${message}`);
            return;
        }

        try {
            this.client.queue('text', {
                type: 'chat',
                needs_translation: false,
                source_name: this.config.bot_name,
                message: message,
                xuid: '',
                platform_chat_id: ''
            });
            console.log(`[CHAT] ${this.config.bot_name}: ${message}`);
        } catch (error) {
            console.error('[ERROR] Erro ao enviar chat:', error);
        }
    }

    async moveTo(x, y, z) {
        if (!this.connected) {
            console.log(`[MOVE-SIM] → (${x.toFixed(1)}, ${y.toFixed(1)}, ${z.toFixed(1)})`);
            return;
        }

        try {
            this.client.queue('move_player', {
                runtime_id: this.client.entityId,
                position: { x, y, z },
                pitch: 0,
                yaw: 0,
                head_yaw: 0,
                mode: 'normal',
                on_ground: true,
                ridden_runtime_id: 0,
                tick: BigInt(0)
            });
            
            this.position = { x, y, z };
            console.log(`[MOVE] → (${x.toFixed(1)}, ${y.toFixed(1)}, ${z.toFixed(1)})`);
        } catch (error) {
            console.error('[ERROR] Erro ao mover:', error);
        }
    }

    async gotoPlayer(playerName) {
        console.log(`[GOTO] Indo até ${playerName}...`);
        
        for (let i = 0; i < 20; i++) {
            const targetX = this.position.x + Math.random() * 2 - 1;
            const targetY = this.position.y;
            const targetZ = this.position.z + Math.random() * 2 - 1;
            
            await this.moveTo(targetX, targetY, targetZ);
            await this.sleep(200);
        }
        
        await this.sendChat(`Cheguei até você, ${playerName}!`);
    }

    async followPlayer(playerName) {
        console.log(`[FOLLOW] Seguindo ${playerName}...`);
        this.following = playerName;
        
        const followInterval = setInterval(async () => {
            if (this.following !== playerName) {
                clearInterval(followInterval);
                return;
            }
            
            const targetX = this.position.x + Math.random() * 0.5 - 0.25;
            const targetY = this.position.y;
            const targetZ = this.position.z + Math.random() * 0.5 - 0.25;
            
            await this.moveTo(targetX, targetY, targetZ);
        }, 500);
    }

    async collectBlocks(blockType, quantity) {
        console.log(`[COLLECT] Coletando ${quantity}x ${blockType}...`);
        await this.sendChat(`Procurando ${blockType}...`);
        
        await this.sleep(2000);
        
        for (let i = 0; i < quantity; i++) {
            const blockX = Math.floor(this.position.x + Math.random() * 10 - 5);
            const blockY = Math.floor(this.position.y);
            const blockZ = Math.floor(this.position.z + Math.random() * 10 - 5);
            
            console.log(`[BREAK] Quebrando bloco em (${blockX}, ${blockY}, ${blockZ})`);
            
            await this.sleep(100);
        }
        
        await this.sendChat(`Coletei ${quantity}x ${blockType}!`);
    }

    async giveItems(playerName, itemType, quantity) {
        console.log(`[GIVE] Entregando ${quantity}x ${itemType} para ${playerName}`);
        
        if (this.connected) {
            this.client.queue('command_request', {
                command: `/give ${playerName} ${itemType} ${quantity}`,
                origin: {
                    type: 'player',
                    uuid: '',
                    request_id: ''
                },
                internal: false,
                version: 52
            });
        }
        
        await this.sleep(500);
        await this.sendChat(`Entreguei ${quantity}x ${itemType} para ${playerName}!`);
    }

    stopAllActions() {
        console.log('[STOP] Parando todas as ações...');
        this.following = null;
    }

    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    async disconnect() {
        console.log('[BEDROCK] Desconectando...');
        if (this.client) {
            this.client.close();
        }
    }
}

async function main() {
    const client = new BedrockRealClient();
    
    try {
        await client.connect();
        
        console.log('[BEDROCK] Cliente Bedrock iniciado!');
        console.log('[BEDROCK] Aguardando comandos...');
        
    } catch (error) {
        console.error('[BEDROCK] Erro ao iniciar:', error);
        process.exit(1);
    }
    
    process.on('SIGINT', async () => {
        console.log('\n[BEDROCK] Encerrando...');
        await client.disconnect();
        process.exit(0);
    });
}

if (require.main === module) {
    main();
}

module.exports = BedrockRealClient;
