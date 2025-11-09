const bedrock = require('bedrock-protocol');
const fs = require('fs');

async function testConnection() {
    console.log('===============================================');
    console.log('  TESTE DE CONEXÃO BEDROCK PROTOCOL');
    console.log('===============================================');
    console.log('');

    const config = JSON.parse(fs.readFileSync('config.json', 'utf8'));
    
    console.log(`Servidor: ${config.server.host}`);
    console.log(`Porta: ${config.server.port}`);
    console.log(`Bot: ${config.bot_name}`);
    console.log('');
    console.log('Tentando conectar...');
    console.log('');

    try {
        const client = bedrock.createClient({
            host: config.server.host,
            port: config.server.port,
            username: config.bot_name,
            offline: true,
            version: '1.21.0'
        });

        client.on('spawn', () => {
            console.log('✓ CONEXÃO BEM-SUCEDIDA!');
            console.log('✓ Bot entrou no mundo!');
            console.log('');
            console.log('Teste concluído com sucesso!');
            
            setTimeout(() => {
                client.close();
                process.exit(0);
            }, 2000);
        });

        client.on('error', (error) => {
            console.error('✗ ERRO DE CONEXÃO:', error.message);
            console.log('');
            console.log('POSSÍVEIS CAUSAS:');
            console.log('- Servidor está offline');
            console.log('- Porta incorreta');
            console.log('- Firewall bloqueando conexão');
            process.exit(1);
        });

        setTimeout(() => {
            console.log('✗ TIMEOUT - Servidor não responde');
            console.log('');
            console.log('DICAS:');
            console.log('- Verifique se o servidor Aternos está online');
            console.log('- Confirme a porta no config.json');
            process.exit(1);
        }, 10000);

    } catch (error) {
        console.error('✗ ERRO:', error.message);
        process.exit(1);
    }
}

testConnection();
