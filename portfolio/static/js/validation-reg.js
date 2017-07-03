$(function() {
  // Initialize form validation on the registration form.
  // It has the name attribute "registration"
  $.validator.addMethod(
        "regex",
        function(value, element, regexp) {
            var re = new RegExp(regexp);
            return this.optional(element) || re.test(value);
        },
        "Invalid username"
);
  $("form[name='register']").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      username: {
        required: true,
        regex: /(?:[A-Z].*[0-9])|(?:[0-9].*[A-Z])/
      },
      email: {
        required: true,
        // Specify that email should be validated
        // by the built-in "email" rule
        email: true
      },
      password1: {
        required: true,
        minlength: 8
      },
      password2: {
        equalTo: "#id_password1"
      }
    },
    // Specify validation error messages
    messages: {
      password1: {
        required: "Please enter password",
        minlength:"Password should be minimum 8 characters long"
      },
      email:{
        required: "Please enter email",        
        email: "Invalid email address"
      },
      password2: {
        required: "Please enter password",
        minlength:"Password should be minimum 8 characters long"
      },
      
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    submitHandler: function(form) {
      form.submit();
    }
  });
});