$(document).ready(function(){ // начать выполнение функции после загрузки документа

    var urls = $('#urls').val().split(','); // получение данных о ранее созданных имён URL с сервера и создание массивах данных из строки
    var len = urls.length;

    $('#url_name, #tittle' ).blur(function () { // функция обработки события после потери фокуса наших полей

        var id = $(this).attr('id'); // данная конструкция поочередно переберет наши поля и получит с них необходимые данные
        var element = $(this).val(); // получение значения ввода пользователем

        switch(id) {
            case 'url_name': // поле имя URL
                $('#warningUrl').remove(); // так как для отображения ошибки я добавляю определенный текст в HTML, при повторной потери фокуса
                for (var i=0; i < len; i++) { // необходимо удалять предыдущую ошибку, иначе получится целый список устаревших данных
                if ((element === urls[i]) || (element.length === 0))  { // если веденный url встречается в БД, либо ничего не введено
                    $(this).removeClass('not_errorform').addClass('errorform'); // добавляем нашему полю класс 'ошибки'. Оно подсветится красным
                    if (element.length > 0) {
                        $(this).before('<p id="warningUrl" style="color:red;"> Это название для URL уже существует</p>'); // добавляем текст ошибки
                    } else {
                        $(this).before('<p id="warningUrl" style="color:red;"> Поле не может быть пустым</p>'); // текст ошибки, если поле пустое
                    }
                    break
                    }
                $(this).removeClass('errorform').addClass('not_errorform'); // соотвественно, если совпадений нету, добавляем класс "нет ошибки". Поле будет зеленным!
                }
            break;

            case 'tittle': // обработка другого поля по аналогичному методу, только данные из БД здесь не нужны
                $('#warningTittle').remove();
                if (element.length > 0) {
                    $(this).removeClass('errorform').addClass('not_errorform');
                } else {
                    $(this).removeClass('not_errorform').addClass('errorform');
                    $(this).before('<p id="warningTittle" style="color:red;"> Поле не может быть пустым</p>');
                }
             break;
        }

        if ($('.not_errorform').length === 2) {  // если на нашей странице есть два элемента с классом not_errorform
            $('#disabledButton').attr('disabled', false) // делаем нашу кнопку активной
        } else {
            $('#disabledButton').attr('disabled', true) // иначе оставляем все как есть
        }
        
    });

});

function painting(){ // первое знакомство с JavaScripts. Функция раскраски таблички "категория"
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