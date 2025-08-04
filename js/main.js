
// JavaScript para o carrossel
document.addEventListener('DOMContentLoaded', function () {
    const carouselSlide = document.querySelector('.carousel-slide');
    const carouselImages = document.querySelectorAll('.carousel-slide img');
    const prevBtn = document.querySelector('.prevBtn');
    const nextBtn = document.querySelector('.nextBtn');

    // Contador de imagens
    let counter = 1;
    const size = carouselImages[0].clientWidth;

    carouselSlide.style.transform = 'translateX(' + (-size * counter) + 'px)';

    // Botão de próxima imagem
    nextBtn.addEventListener('click', () => {
        if (counter >= carouselImages.length - 1) {
            counter = 1;
            carouselSlide.style.transition = "none";
            carouselSlide.style.transform = 'translateX(' + (-size * counter) + 'px)';
            return;
        }
        counter++;
        carouselSlide.style.transition = "transform 0.4s ease-in-out";
        carouselSlide.style.transform = 'translateX(' + (-size * counter) + 'px)';
    });

    // Botão de imagem anterior
    prevBtn.addEventListener('click', () => {
        if (counter <= 0) {
            counter = carouselImages.length - 2;
            carouselSlide.style.transition = "none";
            carouselSlide.style.transform = 'translateX(' + (-size * counter) + 'px)';
            return;
        }
        counter--;
        carouselSlide.style.transition = "transform 0.4s ease-in-out";
        carouselSlide.style.transform = 'translateX(' + (-size * counter) + 'px)';
    });

    // Transição infinita
    carouselSlide.addEventListener('transitionend', () => {
        if (carouselImages[counter].id === 'lastClone') {
            carouselSlide.style.transition = "none";
            counter = carouselImages.length - 2;
            carouselSlide.style.transform = 'translateX(' + (-size * counter) + 'px)';
        }
        if (carouselImages[counter].id === 'firstClone') {
            carouselSlide.style.transition = "none";
            counter = carouselImages.length - counter;
            carouselSlide.style.transform = 'translateX(' + (-size * counter) + 'px)';
        }
    });
});


function openForm() {
    document.getElementById("myForm").style.display = "block";
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
}
function submitForm(event) {
    // Evitar o comportamento padrão de envio do formulário
    event.preventDefault();

    // Exibir pop-up com a mensagem
    alert("Ok! Entraremos em contato!");
    // Fechar o formulário
    closeForm();

}
