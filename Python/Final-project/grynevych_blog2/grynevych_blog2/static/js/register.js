$(document).ready(function() {

    // 1 - Переменные - флаги результатов валидации:
    let res1 = false;
    let res2 = false;
    let res3 = false;
    let res4 = false;

    // 2 - Валидация логина:
    $('#login').blur(function() {
        let loginX = $('#login').val();
        let loginR = /^[a-zA-z][a-zA-Z0-9_]{5,15}$/;
        if (loginR.test(loginX) == true) {
            // Проверка занятости логина ...
            $.ajax({
                url: '/account/ajax_reg',
                data: 'login=' + loginX,
                success: function(result) {
                    if (result.message === 'занят') {
                        $('#login-err').text('Логин занят! Введите другой');
                        res1 = false;
                    } else {
                        $('#login-err').text('');
                        res1 = true;
                    }
                }
            });
        } else {
            $('#login-err').text('Логин - не правильный');
            res1 = false;
        }
    });

    // 3 - Валидация 1 пароля:
    $('#pass1').blur(function() {
        let pass1X = $('#pass1').val();
        let pass1R = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9_]{8,}$/;
        if (pass1R.test(pass1X) == true) {
            $('#pass1-err').text('');
            res2 = true;
        } else {
            $('#pass1-err').text('Пароль - не правильный');
            res2 = false;
        }
    });

    // 4 - Валидация 2 пароля:
    $('#pass2').blur(function() {
        let pass1X = $('#pass1').val();
        let pass2X = $('#pass2').val();
        if (pass1X === pass2X) {
            $('#pass2-err').text('');
            res3 = true;
        } else {
            $('#pass2-err').text('Пароли - не совпадают');
            res3 = false;
        }
    });

    // 5 - Валидация E-Mail:
    $('#email').blur(function() {
        let emailX = $('#email').val();
        let emailR = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;
        if (emailR.test(emailX) == true) {
            $('#email-err').text('');
            res4 = true;
        } else {
            $('#email-err').text('Email - не правильный');
            res4 = false;
        }
    });

    // # - Финальная проверка:
    $('#submit').click(function() {
        if (res1 == true && res2 == true && res3 == true && res4 == true) {
            $('#form-1').attr('onsubmit', 'return true'); // - разблокировка формы
        } else {
            $('#form-1').attr('onsubmit', 'return false'); // - переблокировка формы
            alert('Форма содержит некорректные данные! \nОтправка данных заблокирована!');
        }
    });
});
