$(function() {
  'use strict'
  

  $('#form').parsley().on('form:submit', function() {
    $('.modal--success').addClass('is-visible');
    return true; // Don't submit form for this pen
  });;

  $(document).ready(function() {
    $('.input-wrapper input').filter(function() {
      if ($(this).val().length > 0) {
        $(this).parent().addClass('has-content');
      } else {
        $(this).parent().removeClass('has-content');
      }
      
      if ($(this).hasClass('parsley-success')) {
        $(this).parent().addClass('input--success');
      }
      else {
        $(this).parent().removeClass('input--success');
      }
    });
  });

  $('.input-wrapper input').blur(function() {
    if ($(this).val().length > 0) {
      $(this).parent().addClass('has-content');
    } else {
      $(this).parent().removeClass('has-content');
    }

    if ($(this).hasClass('parsley-success')) {
      $(this).parent().addClass('input--success'); 
    }
    else {
      $(this).parent().removeClass('input--success');
    }
  });

  $('.form__close').on('click', function() {
    $(this).prevAll('.form__input').val('');
    $(this).prevAll('.form__input').removeClass('parsley-success');
    $(this).closest('.input-wrapper').removeClass('has-content input--success');
  });
  
 
});