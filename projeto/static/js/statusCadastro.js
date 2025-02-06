
  document.getElementById('status_modal').addEventListener('change', function() {
      const statusLabel = document.getElementById('status_label');
      if (this.checked) {
          statusLabel.textContent = 'Ativo';
          statusLabel.classList.remove('status-inactive');
          statusLabel.classList.add('status-active');
      } else {
          statusLabel.textContent = 'Inativo';
          statusLabel.classList.remove('status-active');
          statusLabel.classList.add('status-inactive');
      }
  });

  // Definindo o texto do rótulo e a cor inicialmente
  window.onload = function() {
      const statusLabel = document.getElementById('status_label');
      const checkbox = document.getElementById('status_modal');
      if (checkbox.checked) {
          statusLabel.textContent = 'Ativo';
          statusLabel.classList.add('status-active');
      } else {
          statusLabel.textContent = 'Inativo';
          statusLabel.classList.add('status-inactive');
      }
  };
