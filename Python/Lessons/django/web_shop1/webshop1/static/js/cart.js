$(document).ready(function() {

    $('.add-to-cart-btn').click(function() {
        //
        let productId = $(this).prev().val();
        let userId = $(this).prev().prev().val();

        //
        if (userId == 'None') {
            alert('Для использования корзины, Вы должны авторизоваться!');
            window.location = '/account/entry';
        } else {
            let uid = userId;
            let pid = productId;
            $.ajax({
                url: '/orders/ajax_cart',
                data: `uid=${uid}&pid=${pid}`,
                success: function (result) {
                    alert('Товар успешно добавлен в корзину!');
                    $('#count').text(result.count);
                    $('#amount').text(`Количество товаров: ${result.count} шт.`);
                    $('#cost').text(`Общая стоимость: ${result.cost} грн.`);
                }
            });
        }

    });
});
