
function painting(){
    var category = document.getElementsByClassName('category');
    var len = category.length;
    var content = document.getElementsByClassName('container-post');

    for (var i=0; i < len; i++) {

        content[i].style.transform = 'rotate(' + (Math.random() * (4 - 1) + 1) + 'deg)';

        if (category[i].innerText === 'Программирование') {
            category[i].style.backgroundColor = '#ff820b';
        } else if (category[i].innerText === 'Жизнь') {
            category[i].style.backgroundColor = '#991FFF';
        } else if (category[i].innerText === 'Малыш') {
            category[i].style.backgroundColor = '#21f0ff';
        } else if (category[i].innerText === 'Алиэкспресс') {
            category[i].style.backgroundColor = '#FF232D';
        } else if (category[i].innerText === 'Мысли') {
            category[i].style.backgroundColor = '#0c18ff';
        } else if (category[i].innerText === 'Рецепты') {
            category[i].style.backgroundColor = '#40FF23';
        } else {
            category[i].style.backgroundColor = '#0c18ff';
        }
    }
}


// function body() {

//     var body = document.getElementById('body');

//     var category = document.getElementById('category');

//     if (category.innerText === 'Программирование') {
//         body.style.backgroundImage = 'url("http://www.beloglazov-projects.com/media/site/programm.png")';
//     }
// }