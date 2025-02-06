
/*  Desatualizado






// Configuração do JS Confetti
const canvas = document.getElementById('custom_canvas');
const jsConfetti = new JSConfetti({ canvas });

let counterValue = 0; // Valor inicial do contador

// Carrega o áudio
const celebrationAudio = new Audio('/static/audio/hino.mp3'); // Substitua pelo caminho do seu arquivo de áudio

function updateCounter() {
  const counterContainer = document.querySelector('.flip-counter');
  const digits = counterValue.toString().padStart(2, '0').split(''); // Garante dois dígitos mínimo (ex. 00, 01, 10, ...)

  // Adiciona novos dígitos se necessário
  while (counterContainer.children.length < digits.length) {
    const newDigit = document.createElement('div');
    newDigit.classList.add('digit');
    newDigit.textContent = '0';
    counterContainer.prepend(newDigit); // Adiciona o novo dígito na esquerda
  }

  // Atualiza os dígitos com animação
  [...counterContainer.children].forEach((digit, index) => {
    const newDigitValue = digits[index];
    if (digit.textContent !== newDigitValue) {
      digit.classList.add('flip');
      setTimeout(() => {
        digit.textContent = newDigitValue;
        digit.classList.remove('flip');
      }, 500);
    }
  });

  // Verifica se o contador atingiu 1000 e dispara o confetti por 20 segundos
  if (counterValue % 1000 === 0 && counterValue !== 0) {
    // Exibe a mensagem de celebração
    document.getElementById('message').textContent = `Comemoramos a marca de ${total} vidas atendidas, um marco que reflete nosso compromisso e dedicação. Obrigado por fazer parte dessa jornada de sucesso!`;
    document.getElementById('message').style.display = 'block';

    // Reproduz o áudio
    celebrationAudio.play();

    // Dispara confetti inicial
    jsConfetti.addConfetti({
      confettiRadius: 6,
      confettiNumber: 400, // Número de confetes
    });

    // Configura um intervalo para disparar confetti a cada 500ms por 20 segundos
    const confettiInterval = setInterval(() => {
      jsConfetti.addConfetti({
        confettiRadius: 6,
        confettiNumber: 400, // Número de confetes por disparo
      });
    }, 500);

    // Para o intervalo após 20 segundos de confetti
    setTimeout(() => {
      clearInterval(confettiInterval);
    }, 15000); // 20 segundos em milissegundos
  }
}

// Função para atualizar o contador manualmente
function setCounterValue(newValue) {
  counterValue = newValue;
  updateCounter();
}

// Atualize o valor do contador aqui
setCounterValue(); // Altere para 2000 para testar o confetti


*/