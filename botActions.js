export class BotActions {
  constructor(bot, pathfinder) {
    this.bot = bot;
    this.pathfinder = pathfinder;
    this.miningQueue = [];
    this.inventory = new Map();
  }

  async executeAction(actionData, playerName, playerPosition) {
    const { action, target, quantity, response } = actionData;

    this.sendMessage(response);

    switch (action) {
      case 'goto':
        await this.goToPlayer(playerPosition);
        break;

      case 'mine':
        await this.mineResource(target, quantity || 1);
        break;

      case 'give':
        await this.goToPlayer(playerPosition);
        await this.giveItems(playerName, target, quantity);
        break;

      case 'follow':
        this.pathfinder.startFollowing(playerName);
        break;

      case 'stop':
        this.pathfinder.stopFollowing();
        break;

      case 'respond':
        break;

      default:
        console.log(`Ação desconhecida: ${action}`);
    }
  }

  async goToPlayer(playerPosition) {
    if (!playerPosition) {
      this.sendMessage('Não consigo ver sua posição!');
      return;
    }

    console.log(`Indo até o jogador em: ${JSON.stringify(playerPosition)}`);
    await this.pathfinder.goToPosition(playerPosition, 2);
    this.sendMessage('Cheguei!');
  }

  async mineResource(resourceType, quantity) {
    console.log(`Tentando minerar ${quantity}x ${resourceType}`);
    
    this.sendMessage(`Procurando por ${resourceType}...`);
    
    const blockTypes = {
      'oak_log': ['oak_log', 'log', 'wood'],
      'madeira': ['oak_log', 'log', 'wood', 'birch_log', 'spruce_log'],
      'pedra': ['stone', 'cobblestone'],
      'stone': ['stone', 'cobblestone'],
      'coal': ['coal_ore'],
      'iron': ['iron_ore'],
      'carvao': ['coal_ore'],
      'ferro': ['iron_ore']
    };

    const searchBlocks = blockTypes[resourceType] || [resourceType];
    
    for (let i = 0; i < quantity; i++) {
      const block = await this.findNearbyBlock(searchBlocks, 50);
      
      if (block) {
        await this.pathfinder.goToPosition(block.position, 4);
        await this.mineBlock(block.position);
        this.addToInventory(resourceType, 1);
        
        if (i < quantity - 1) {
          await this.sleep(1000);
        }
      } else {
        this.sendMessage(`Só consegui encontrar ${i} ${resourceType}. Não há mais por perto.`);
        break;
      }
    }

    this.sendMessage(`Coletei ${Math.min(quantity, this.inventory.get(resourceType) || 0)} ${resourceType}!`);
  }

  async findNearbyBlock(blockTypes, radius) {
    if (!this.bot.position) return null;

    const botPos = this.bot.position;
    let closestBlock = null;
    let closestDistance = Infinity;

    for (let x = -radius; x <= radius; x++) {
      for (let y = -radius; y <= radius; y++) {
        for (let z = -radius; z <= radius; z++) {
          const pos = {
            x: Math.floor(botPos.x) + x,
            y: Math.floor(botPos.y) + y,
            z: Math.floor(botPos.z) + z
          };

          const distance = Math.sqrt(x * x + y * y + z * z);
          
          if (distance < closestDistance && distance <= radius) {
            for (const blockType of blockTypes) {
              if (this.isBlockType(pos, blockType)) {
                closestBlock = { position: pos, type: blockType };
                closestDistance = distance;
                break;
              }
            }
          }
        }
      }
    }

    return closestBlock;
  }

  isBlockType(position, blockType) {
    return Math.random() > 0.95;
  }

  async mineBlock(position) {
    console.log(`Minerando bloco em: ${JSON.stringify(position)}`);
    await this.sleep(2000);
  }

  async giveItems(playerName, itemType, quantity) {
    const amount = quantity || this.inventory.get(itemType) || 0;
    
    if (amount === 0) {
      this.sendMessage(`Desculpe, não tenho ${itemType} no meu inventário.`);
      return;
    }

    console.log(`Entregando ${amount}x ${itemType} para ${playerName}`);
    
    this.removeFromInventory(itemType, amount);
    this.sendMessage(`Entregando ${amount}x ${itemType}!`);
  }

  addToInventory(item, quantity) {
    const current = this.inventory.get(item) || 0;
    this.inventory.set(item, current + quantity);
  }

  removeFromInventory(item, quantity) {
    const current = this.inventory.get(item) || 0;
    this.inventory.set(item, Math.max(0, current - quantity));
  }

  sendMessage(message) {
    try {
      if (this.bot.queue && this.bot.queue.length < 10) {
        this.bot.queue('text', {
          type: 'chat',
          needs_translation: false,
          source_name: this.bot.username,
          xuid: '',
          platform_chat_id: '',
          message: message
        });
      }
      console.log(`[BOT] ${message}`);
    } catch (error) {
      console.error('Erro ao enviar mensagem:', error);
    }
  }

  sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}
