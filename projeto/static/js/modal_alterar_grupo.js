document.addEventListener('DOMContentLoaded', function() {
    const openModalButtons = document.querySelectorAll('.btn-open-modal');

    openModalButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const grupoId = button.dataset.grupoId;
            const grupoNome = button.dataset.grupoNome;

            // Preenche o campo hidden com o grupoId
            document.getElementById('id_grupo').value = grupoId;
            // Preenche o campo de nome com o grupoNome
            document.getElementById('nome_grupo').value = grupoNome;
        });
    });
});

