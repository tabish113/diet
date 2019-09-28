
function stickyHeader() {
    if (jQuery('.stricky').length) {
        var strickyScrollPos = 100;
        if (jQuery(window).scrollTop() > strickyScrollPos) {
            jQuery('.stricky').addClass('stricky-fixed');
            jQuery('.scroll-to-top').fadeIn(1500);
        } else if (jQuery(this).scrollTop() <= strickyScrollPos) {
            jQuery('.stricky').removeClass('stricky-fixed');
            jQuery('.scroll-to-top').fadeOut(1500);
        }
    };
}
(function($){
    if($('.accordion-box').length){
        $(".accordion-box").on('click', '.accord-btn', function() {

            if($(this).hasClass('active')!==true){
            $('.accordion .accord-btn').removeClass('active');

            }

            if ($(this).next('.accord-content').is(':visible')){
                $(this).removeClass('active');
                $(this).next('.accord-content').slideUp(500);
            }else{
                $(this).addClass('active');
                $('.accordion .accord-content').slideUp(500);
                $(this).next('.accord-content').slideDown(500); 
            }
        }); 
    }

    if ($('.contact-info-carousel').length) {
        $('.contact-info-carousel').owlCarousel({
            dots: true,
            loop:true,
            margin:20,
            nav:false,
            navText: [
                '<i class="fa fa-angle-left"></i>',
                '<i class="fa fa-angle-right"></i>'
            ],
            autoplayHoverPause: false,
            autoplay: 6000,
            smartSpeed: 1000,
            responsive:{
                0:{
                    items:1
                },
                600:{
                    items:1
                },
                800:{
                    items:1
                },
                1024:{
                    items:1
                },
                1100:{
                    items:1
                },
                1200:{
                    items:1
                }
            }
        });         
    }


})(jQuery);
//===Header Sticky===
// function stickyHeader() {
//     if ($('.stricky').length) {
//         var strickyScrollPos = 100;
//         if ($(window).scrollTop() > strickyScrollPos) {
//             $('.stricky').addClass('stricky-fixed');
//             $('.scroll-to-top').fadeIn(1500);
//         } else if ($(this).scrollTop() <= strickyScrollPos) {
//             $('.stricky').removeClass('stricky-fixed');
//             $('.scroll-to-top').fadeOut(1500);
//         }
//     };
// }
