document.addEventListener('DOMContentLoaded', () => {
    const editModal = document.getElementById('editGrupoModal');
    const grupoIdInput = editModal.querySelector('#grupoId');
    const grupoNomeInput = editModal.querySelector('#grupoNome');
    const statusSwitch = editModal.querySelector('#status_modal');

    editModal.addEventListener('show.bs.modal', (event) => {
        const button = event.relatedTarget; // Botão que acionou o modal
        const grupoId = button.getAttribute('data-grupo_id'); // Extrai o ID do grupo
        const grupoNome = button.getAttribute('data-grupo_nome'); // Extrai o Nome do grupo
        const grupoStatus = button.getAttribute('data-grupo_status'); // Extrai o Status do grupo

        // Define os valores nos campos de entrada do modal
        grupoIdInput.value = grupoId;
        grupoNomeInput.value = grupoNome;

        // Define o estado do switch conforme o status do grupo
        if (grupoStatus === 'A') {
            statusSwitch.checked = true;
        } else {
            statusSwitch.checked = false;
        }
    });
});
