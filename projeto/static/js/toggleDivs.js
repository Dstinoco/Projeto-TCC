// toggleDivs.js
document.addEventListener('DOMContentLoaded', (event) => {
    const toggleCheckbox = document.getElementById('toggleCheckbox');
    if (toggleCheckbox) {
        toggleCheckbox.addEventListener('change', function() {
            const div1 = document.getElementById('div1');
            const div2 = document.getElementById('div2');

            if (this.checked) {
                div1.classList.remove('hidden');
                div2.classList.add('hidden');
            } else {
                div1.classList.add('hidden');
                div2.classList.remove('hidden');
            }
        });
    }
});
