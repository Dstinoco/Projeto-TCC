/*Exibir senha de login */

const togglePassword = document.querySelector('#togglePassword');
const passwordExibir = document.querySelector('#passwordExibir');
const eyeIcon = document.querySelector('#eyeIcon');

togglePassword.addEventListener('click', function (e) {
    // Toggle the type attribute using getAttribute() and setAttribute()
    const type = passwordExibir.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordExibir.setAttribute('type', type);
    
    // Toggle the eye icon
    if (type === 'password') {
        eyeIcon.classList.remove('fa-eye-slash');
        eyeIcon.classList.add('fa-eye');
    } else {
        eyeIcon.classList.remove('fa-eye');
        eyeIcon.classList.add('fa-eye-slash');
    }
});
