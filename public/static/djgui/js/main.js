
$(document).ready(function(){
    $("#social_link_facebook").click(function(){
        window.location.href='https://www.facebook.com/HeavyCrownMedia/'
    });
});

$(document).ready(function(){
    $("#social_link_twitter").click(function(){
        window.location.href='#'
    });
});

$(document).ready(function(){
    $("#social_link_linkedin").click(function(){
        window.location.href='#'
    });
});

$(".home-link").click(function() {
    $('html, body').animate({
        scrollTop: $(".home").offset().top
    }, 500);
});

$(".work-link").click(function() {
    $('html, body').animate({
        scrollTop: $(".work").offset().top
    }, 500);
});

$(".contact-link").click(function() {
    $('html, body').animate({
        scrollTop: $(".contact").offset().top
    }, 500);
});

$(".photo-thumb").hover(function() {
    $(this).fadeTo('fast', 0.6);
    },
    function() {
    $(this).fadeTo('fast', 1);
    }
);