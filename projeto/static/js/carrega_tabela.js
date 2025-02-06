
    document.addEventListener("DOMContentLoaded", function () {
        // Ocultar a tabela inicialmente
        var tabela = document.getElementById("div_tabela");
        tabela.classList.add("hidden");
  
        // Mostrar a tabela após 1 segundo
        setTimeout(function () {
            tabela.classList.remove("hidden");
        }, 300);
    });