document.addEventListener("DOMContentLoaded", function() {
    var alerts = document.querySelectorAll('.alert');

    alerts.forEach(function(alert) {
        var timeout = 4000; // 5000ms = 5 segundos
        var progressBar = alert.querySelector('.progress-bar');
        var interval = 20; // Atualização a cada 10ms para uma transição mais suave
        var increment = (interval / timeout) * 100;

        var width = 0;
        var progressInterval = setInterval(function() {
            width += increment;
            progressBar.style.width = width + '%';

            if (width >= 100) {
                clearInterval(progressInterval);
                alert.classList.remove('show');
                alert.classList.add('fade');

                setTimeout(function() {
                    alert.remove();
                }, 150);
            }
        }, interval);

        setTimeout(function() {
            clearInterval(progressInterval);
            alert.classList.remove('show');
            alert.classList.add('fade');

            setTimeout(function() {
                alert.remove();
            }, 150);
        }, timeout);
    });
});