document.addEventListener('DOMContentLoaded', function() {
  document.querySelector('.hamburger-icon').addEventListener('click', function() {
      document.querySelector('.side-menu').classList.toggle('active');
  });
});
