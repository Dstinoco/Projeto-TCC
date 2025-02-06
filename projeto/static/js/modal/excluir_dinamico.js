document.addEventListener('DOMContentLoaded', () => {
    const deleteModal = document.getElementById('deleteUserModal');
    const deleteIDInput = deleteModal.querySelector('#deleteID');
    const deleteNameInput = deleteModal.querySelector('#deleteName');
    const deleteMessage = deleteModal.querySelector('#deleteMessage'); // Selecione a tag <p>

    deleteModal.addEventListener('show.bs.modal', (event) => {
        const button = event.relatedTarget; // Botão que acionou o modal
        const deleteID = button.getAttribute('data-delete-id'); // Extrai o ID do usuário
        const deleteName = button.getAttribute('data-delete-name'); // Extrai o nome do usuário

        // Define os valores nos campos de entrada do modal
        deleteIDInput.value = deleteID;
        deleteNameInput.value = deleteName;

        // Atualize o conteúdo da tag <p> com o nome do usuário
        deleteMessage.innerHTML = `Deseja realmente excluir <strong>${deleteName}</strong>?`;
    });
});
