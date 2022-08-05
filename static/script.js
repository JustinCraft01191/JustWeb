function Jump_To_Section(section){
    var id = document.getElementById(section);
    window.scrollTo({top:id.offsetTop-50, behavior:'smooth'});
    var x = window.matchMedia("(max-width: 992px)")
    if (x.matches){
        document.getElementById("navbar-toggler").click();
    }
}
(function($) {

	"use strict";


  // Form
	var contactForm = function() {
		if ($('#contactForm').length > 0 ) {
			$( "#contactForm" ).validate( {
				rules: {
					name: "required",
					subject: "required",
					email: {
						required: true,
						email: true
					},
					message: {
						required: true,
						minlength: 5
					}
				},
				messages: {
					name: "Please enter your name",
					subject: "Please enter your subject",
					email: "Please enter a valid email address",
					message: "Please enter a message"
				}
			});
		}
	};
	contactForm();

})(jQuery);
