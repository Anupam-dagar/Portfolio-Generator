$(function() {
  // Initialize form validation on the registration form.
  // It has the name attribute "registration"
  $.validator.addMethod(
        "regex",
        function(value, element, regexp) {
            var re = new RegExp(regexp);
            return this.optional(element) || re.test(value);
        },
        "Please check your input."
);
  $("form[name='details']").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      password1: {
        required: true,
        regex: /(?:[A-Z].*[0-9])|(?:[0-9].*[A-Z])/
      },
      firstname: "required",
      email_address: {
        required: true,
        // Specify that email should be validated
        // by the built-in "email" rule
        email: true
      },
      date_of_birth: {
        required: true,
        dateISO: true,
        minlength: 10
      },
      phone_number: {
        required: true,
        minlength: 10,
        maxlength: 10
      },
      main_bio: "required",
      skill1: "required",
      skill2: "required",
      facebook: "required",
      project1_name: "required",
      project1_url: {
        required: false,
        url: false
      },
      project1_description: "false",
      blog: "url"
    },
    // Specify validation error messages
    messages: {
      first_name: {
        required: "error",
        regex: "regex error"
      },
      password: {
        required: "Please provide a password",
        minlength: "Your password must be at least 5 characters long"
      },
      email_address: "Please enter a valid email address",
      date_of_birth: "Please enter in YYYY-MM-DD format",
      phone_number: {
        required:"Please enter your phone_number",
        minlength:"Phone number must be of 10 digits",
        maxlength:"Phone number must be of 10 digits"
      },
      main_bio:"Please enter your main bio",
      skill1:"Please enter your skill1",
      skill2:"Please enter your skill2",
      facebook:"Please enter your facebook username",
      project1_name:"Please enter name of project1",
      project1_url: {
        required: "Please enter GitHub Link for the project",
        url: "Please enter a valid url"
      },
      blog: "Please enter a valid url"
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    submitHandler: function(form) {
      form.submit();
    }
  });
});
