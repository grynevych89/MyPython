$(document).ready(function() {

    const user_id = $('#user_id').val();

    $.ajax({
        url: '/orders/ajax_cart_display',
        data: `uid=${user_id}`,
        success: function (result) {
            $('#count').text(result.count);
            $('#amount').text(`Количество товаров: ${result.count} шт.`);
            $('#cost').text(`Общая стоимость: ${result.cost} грн.`);
        }
    });

});
