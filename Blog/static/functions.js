$(document).ready(function(){

    var urls = $('#urls').val().split(',');
    var len = urls.length;

    $('#url_name, #tittle' ).blur(function () {

        var id = $(this).attr('id');
        var element = $(this).val();

        switch(id) {
            case 'url_name':
                $('#warningUrl').remove();
                for (var i=0; i < len; i++) {
                if ((element === urls[i]) || (element.length === 0))  {
                    $(this).removeClass('not_errorform').addClass('errorform');
                    if (element.length > 0) {
                        $(this).before('<p id="warningUrl" style="color:red;"> Это название для URL уже существует</p>');
                    } else {
                        $(this).before('<p id="warningUrl" style="color:red;"> Поле не может быть пустым</p>');
                    }
                    break
                    }
                $(this).removeClass('errorform').addClass('not_errorform');
                }
            break;

            case 'tittle':
                $('#warningTittle').remove();
                if (element.length > 0) {
                    $(this).removeClass('errorform').addClass('not_errorform');
                } else {
                    $(this).removeClass('not_errorform').addClass('errorform');
                    $(this).before('<p id="warningTittle" style="color:red;"> Поле не может быть пустым</p>');
                }
             break;
        }

        if ($('.not_errorform').length === 2) {
            $('#disabledButton').attr('disabled', false)
        } else {
            $('#disabledButton').attr('disabled', true)
        }
        
    });

});

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