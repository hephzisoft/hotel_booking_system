(function ($) {

   "use strict";

   var fullHeight = function () {

      $('.js-fullheight').css('height', $(window).height());
      $(window).resize(function () {
         $('.js-fullheight').css('height', $(window).height());
      });

   };
   fullHeight();

   var carousel = function () {
      $('.featured-carousel').owlCarousel({
         loop: false,
         autoplay: true,
         margin: 20,
         animateOut: 'fadeOut',
         animateIn: 'fadeIn',
         nav: true,
         dots: true,
         autoplayHoverPause: false,
         items: 1,
         navText: ["<span class='ion-ios-arrow-back'></span>", "<span class='ion-ios-arrow-forward'></span>"],
         // responsive: {
         //    0: {
         //       items: 1
         //    },
         //    600: {
         //       items: 2
         //    },
         //    1000: {
         //       items: 3
         //    }
         // }
      });

   };
   carousel();

})(jQuery);

$(function () {

   if ($('.owl-2').length > 0) {
      $('.owl-2').owlCarousel({
         center: false,
         items: 1,
         loop: false,
         stagePadding: 0,
         margin: 20,
         smartSpeed: 1000,
         autoplay: true,
         nav: true,
         dots: true,
         pauseOnHover: false,
         responsive: {
            600: {
               margin: 20,
               nav: true,
               items: 2
            },
            1000: {
               margin: 20,
               stagePadding: 0,
               nav: true,
               items: 3
            }
         }
      });
   }

})