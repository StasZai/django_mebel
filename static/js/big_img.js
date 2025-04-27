var bigImgBox = document.getElementById("BigImgBox");
var bigImg = document.getElementById("BigImg");

function openBigImg(pic) {
    bigImgBox.style.display = "flex"; // Показываем контейнер
    bigImg.src = pic; // Устанавливаем источник изображения
}

function closeBigImg() {
    bigImgBox.style.display = "none"; // Скрываем контейнер
}