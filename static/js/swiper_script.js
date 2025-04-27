const panorama = new Swiper('.catalog-panorama-swiper', {
    slidesPerView: 1, // Показываем 5 слайдов
    spaceBetween: 10, // Отступ между слайдам // Центрируем активный слайд
    loop: true, // Включаем бесконечный цикл
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    autoplay: {
        delay: 5000, // время в миллисекундах (3000 мс = 3 сек.)
        disableOnInteraction: false, // продолжать автопрокрутку после взаимодействия
    },
});





const swiper = new Swiper('.swiper-container', {
    slidesPerView: 5, // Показываем 5 слайдов
    spaceBetween: 10, // Отступ между слайдам // Центрируем активный слайд
    loop: false, // Включаем бесконечный цикл
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});
