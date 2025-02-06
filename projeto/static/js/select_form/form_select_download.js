
document.addEventListener('DOMContentLoaded', function() {
    var tipoSelect = document.getElementById('select_download');
    tipoSelect.addEventListener('focus', function() {
        var options = this.options;
        for (var i = 0; i < options.length; i++) {
            if (options[i].value == "0") {
                options[i].disabled = true;
                break;
            }
        }
    });
});
