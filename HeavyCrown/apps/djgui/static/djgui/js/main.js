
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

$(".work-link-2").click(function() {
    $('html, body').animate({scrollTop: $('.work').offset().top + 20}, 10);
});

$(".contact-link-1").click(function() {
    $('html, body').animate({
        scrollTop: $(".contact-1").offset().top
    }, 500);
});

$(".contact-link-2").click(function() {
    $('html, body').animate({
        scrollTop: $(".contact-1").offset().top
    }, 500);
});

$(".contact-link-3").click(function() {
    $('html, body').animate({scrollTop: $('.contact-2').offset().top + 20}, 10);
});

$(".contact-link-4").click(function() {
    $('html, body').animate({scrollTop: $('.contact-2').offset().top + 20}, 10);
});

$(".lets-talk").click(function() {
    $('html, body').animate({scrollTop: $('.contact-2').offset().top + 20}, 10);
});

$(".photo-thumb").hover(function() {
    $(this).fadeTo('fast', 0.6);
    },
    function() {
    $(this).fadeTo('fast', 1);
    }
);