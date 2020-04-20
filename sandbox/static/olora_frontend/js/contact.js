$(document).ready(function(){
    
    (function($) {
        "use strict";

    const lockModal = $("#lock-modal");
    const loadingCircle = $("#loading-circle");
    const Form = $('#contactForm')
    jQuery.validator.addMethod('answercheck', function (value, element) {
        return this.optional(element) || /^\bcat\b$/.test(value)
    }, "type the correct answer -_-");

    // validate contactForm form
    $(function() {
        $('#contactForm').validate({
            rules: {
                name: {
                    required: true,
                    minlength: 2
                },
                subject: {
                    required: true,
                    minlength: 4
                },
                number: {
                    required: true,
                    minlength: 5
                },
                email: {
                    required: true,
                    email: true
                },
                message: {
                    required: true,
                    minlength: 20
                }
            },
            messages: {
                name: {
                    required: "come on, you have a name, don't you?",
                    minlength: "your name must consist of at least 2 characters"
                },
                subject: {
                    required: "come on, you have a subject, don't you?",
                    minlength: "your subject must consist of at least 4 characters"
                },
                number: {
                    required: "come on, you have a number, don't you?",
                    minlength: "your Number must consist of at least 5 characters"
                },
                email: {
                    required: "no email, no message"
                },
                message: {
                    required: "um...yea, you have to write something to send this form.",
                    minlength: "thats all? really?"
                }
            },
            submitHandler: function(form) {
                 lockModal.css("display", "block");
                 loadingCircle.css("display", "block");
                 Form.children("input").each(function() {
                    $(this).attr("readonly", true);
                 });
                $(form).ajaxSubmit({
                    type:"POST",
                    data: $(form).serialize(),
                    url:"/api/contact_us",
                    success: function(data) {
                        if (data.message === "success"){
                            $("#contactForm")[0].reset();
                            lockModal.css("display", "none");
                            loadingCircle.css("display", "none");
                            Form.children("input").each(function() {
                                $(this).attr("readonly", false);
                            });
                            // $('#contactForm :input').attr('disabled', 'disabled');
                            $('#contactForm').fadeTo( "slow", 1, 'swing', function() {
                                // $(this).find(':input').attr('disabled', 'disabled');
                                $(this).find('label').css('cursor','default');
                                swal({icon: "success",
                                    title: "Your message has been submitted.",
                                    text: "We will get back to you soon.",
                                    showConfirmButton: false,
                                    timer: 2000
                                })
                                // $('#success').fadeIn();
                                // $('.modal').modal('hide');
                                // $('#success').modal('show');
                            })
                        }
                    },
                    error: function(data) {
                        if (data.message === 'error'){
                            $('#contactForm').fadeTo( "slow", 1, "swing", function() {
                                lockModal.css("display", "none");
                                loadingCircle.css("display", "none");
                                Form.children("input").each(function() {
                                    $(this).attr("readonly", false);
                                });
                                swal({icon: "error",
                                    title: "Ooops...",
                                    text: 'Message not sent. Send again!',
                                    showConfirmButton: false,
                                    timer: 1500
                                })
                                // $('#error').fadeIn();
                                // $('.modal').modal('hide');
                                // $('#error').modal('show');
                            })
                        }
                    }
                })
            }
        })
    })
        
 })(jQuery)
})