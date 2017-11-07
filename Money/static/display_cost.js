function cost(){

    var amount_cost = 0;
    var number_input = 5;
    for (var i=0; i < number_input; i++) {
        amount_cost += +$('#cost' + i).val()
    }

    return confirm('Ты подтверждаешь ввод траты на сумму ' + amount_cost + '?');
}
$(function() {
   $('#cost').on('click', cost);
});