$(document).ready(function(){
    $('.one-post').hover(function(event){
        $(event.currentTarget).find('.one-post-shadow').animate({opacity: '0.2'}, 300);
    }, function(event){
        $(event.currentTarget).find('.one-post-shadow').animate({opacity: '0'}, 300);
    });

    $('.header img').hover(function(){
        $(this).animate({
            width: '+=20px'
        }, 200);
    }, function(){
        $(this).animate({
            width: '-=20px'
        }, 200);
    });
});