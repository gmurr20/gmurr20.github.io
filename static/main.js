$("#upArrow").click(function() {
	var scrollTop = $(window).scrollTop() - 50;
	var top= 0;
	var work = $("#work").offset().top;
	var projects = $("#projects").offset().top;
	var travel = $("#travel").offset().top;
	var contact = $("#contact").offset().top;
	if(scrollTop < work) {
		scrollTo(top);
	}
	else if(scrollTop < projects) {
		scrollTo(work);
	}
	else if(scrollTop < travel) {
		scrollTo(projects);
	}
	else {
		scrollTo(travel);
	}
});

$("#downArrow").click(function() {
	var scrollTop = $(window).scrollTop() + 50;
	var work = $("#work").offset().top;
	var projects = $("#projects").offset().top;
	var travel = $("#travel").offset().top;
	var contact = $("#contact").offset().top;
	if(scrollTop < work) {
		scrollTo(work);
	}
	else if(scrollTop < projects) {
		scrollTo(projects);
	}
	else if(scrollTop < travel) {
		scrollTo(travel);
	}
	else {
		scrollTo(contact);
	}
});
function scrollTo(top) {
    $('html, body').animate({
        scrollTop: top
	}, 1000);
}

function set_body_height() {
    $("#topPic").height($(window).height());
  }
  $(document).ready(function() {
    $(window).bind('resize', set_body_height);
    set_body_height();
  });