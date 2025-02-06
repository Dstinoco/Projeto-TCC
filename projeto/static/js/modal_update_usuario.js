document.addEventListener('DOMContentLoaded', function () {
    var editButtons = document.querySelectorAll('a[href^="/cadastro/usuario/update/"]');
    
    editButtons.forEach(function(button) {
      button.addEventListener('click', function(event) {
        event.preventDefault();
        
        var userId = this.getAttribute('href').split('/').pop();
  
        fetch('/cadastro/usuario/update/' + userId)
          .then(response => response.json())
          .then(data => {
            document.querySelector('#editUserModal input[name="nome"]').value = data.nome;
            document.querySelector('#editUserModal input[name="email"]').value = data.email;
            document.querySelector('#editUserModal input[name="status"]').checked = data.status === 'A';
            document.querySelector('#editUserForm').action = '/cadastro/usuario/update/' + userId;
            
            var editUserModal = new bootstrap.Modal(document.getElementById('editUserModal'));
            editUserModal.show();
          })
          .catch(error => console.error('Erro ao carregar os dados do usuário:', error));
      });
    });
  });