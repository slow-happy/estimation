// const slickSlide = jQuery('#slick-slide')

// if(slickSlide) {
//     slickSlide.slick({
//         dots: true,
//         arrow: false,
//         slidesToShow: 3,
//         slideToScroll: 1,
//         autoplay: true,
//         autoplaySpeed: 3000,
//         responsive: [
//             {
//                 breakpoint: 768,
//                 settings: {
//                     slideToShow: 2
//                 }
//             },
//             {
//                 breakpoint: 576,
//                 settings: {
//                     slideToShow:1
//                 }
//             }
//         ]
//     })
// }

$(function(){
    $(".fold-table tr.view").on("click", function(){
      if($(this).hasClass("open")) {
        $(this).removeClass("open").next(".fold").removeClass("open");
      } else {
        $(".fold-table tr.view").removeClass("open").next(".fold").removeClass("open");
        $(this).addClass("open").next(".fold").addClass("open");
      }
    });
  });

