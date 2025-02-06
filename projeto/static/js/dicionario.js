    function toggleArrow(element) {
        const icon = element.querySelector('i');
        if (icon.classList.contains('bi-chevron-right')) {
            icon.classList.remove('bi-chevron-right');
            icon.classList.add('bi-chevron-down');
        } else {
            icon.classList.remove('bi-chevron-down');
            icon.classList.add('bi-chevron-right');
        }
    }
