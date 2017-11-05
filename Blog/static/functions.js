function painting(){

    var category = document.getElementsByClassName('category');
    var len = category.length;

    for (var i=0; i < len; i++) {
        if (category[i].innerText === 'Программирование') {
            category[i].style.backgroundColor = '#ff820b';
        } else if (category[i].innerText === 'Жизнь') {
            category[i].style.backgroundColor = '#21f0ff';
        } else {
            category[i].style.backgroundColor = '#0c18ff';
        }
    }
}