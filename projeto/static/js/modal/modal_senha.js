document.addEventListener('DOMContentLoaded', () => {
    const editModal = document.getElementById('editUserModal');
    const userIdInput = editModal.querySelector('#userId');
    const userNameInput = editModal.querySelector('#userName');
    const userMessage = editModal.querySelector('#userMessage'); // Selecione a tag <p>

    editModal.addEventListener('show.bs.modal', (event) => {
        const button = event.relatedTarget; // Botão que acionou o modal
        const userId = button.getAttribute('data-user-id'); // Extrai o ID do usuário
        const userName = button.getAttribute('data-user-name'); // Extrai o nome do usuário

        // Define os valores nos campos de entrada do modal
        userIdInput.value = userId;
        userNameInput.value = userName;

        // Atualize o conteúdo da tag <p> com o nome do usuário
        userMessage.innerHTML = `Um e-mail com a nova senha será enviado para caixa de entrada do usuário <strong>${userName}</strong>. Deseja prosseguir?`;
    });
});
