const coin = document.querySelector('.coin');

// Função para atualizar a posição e rotação da moeda
function updateCoinPosition(event) {
    const mouseX = event.clientX; // Posição X do mouse
    const mouseY = event.clientY; // Posição Y do mouse

    // Calcular a rotação da moeda com base na posição do mouse
    const rotateX = (mouseY / window.innerHeight - 0.5) * 100; // Gira com base na altura
    const rotateY = (mouseX / window.innerWidth - 0.5) * -100; // Gira com base na largura

    // Aplica a transformação 3D à moeda, adicionando a rotação do mouse
    coin.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
}

// Adiciona um ouvinte de evento para o movimento do mouse
document.addEventListener('mousemove', updateCoinPosition);
