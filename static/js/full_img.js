var fullImgBox = document.getElementById("FullImgBox");
var fullImg = document.getElementById("FullImg");

function openFullImg(pic) {
    fullImgBox.style.display = "flex";
    fullImg.src = pic;
}

function closeFullImg() {
    fullImgBox.style.display = "none";
}