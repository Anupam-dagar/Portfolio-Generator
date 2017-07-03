$(document).ready(function () {
   $('.myform fieldset:first-child').fadeIn('slow');

    $('.myform input[type="text"]').on('focus', function () {
        $(this).removeClass('input-error');
    });

    // next step
    $('.myform .next').on('click', function () {
        var parent_fieldset = $(this).parents('fieldset');
        var next_step = true;

        if (next_step) {
            parent_fieldset.fadeOut(400, function () {
                $(this).next().fadeIn();
            });
        }

    });

    // previous step
    $('.myform .previous').on('click', function () {
        $(this).parents('fieldset').fadeOut(400, function () {
            $(this).prev().fadeIn();
        });
    });

    // submit
/*    $('.myform').on('submit', function (e) {

        $(this).find('input[type="text"],input[type="email"]').each(function () {
            if ($(this).val() == "") {
                e.preventDefault();
                $(this).addClass('input-error');
            } else {
                $(this).removeClass('input-error');
            }
        });

    });*/

   
});