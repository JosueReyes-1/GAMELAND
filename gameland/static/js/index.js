$(function () {

  if ($('.owl-2').length > 0) {
    $('.owl-2').owlCarousel({
      center: false,
      items: 1,
      loop: true,
      stagePadding: 0,
      margin: 20,
      smartSpeed: 1000,
      autoplay: true,
      pauseOnHover: false,
      responsive: {
        600: {
          margin: 20,
          items: 2
        },
        1000: {
          margin: 20,
          stagePadding: 0,
          items: 5
        }
      }
    });
  }

})
$(function () {

  if ($('.owl-3').length > 0) {
    $('.owl-3').owlCarousel({
      center: false,
      items: 1,
      loop: true,
      stagePadding: 0,
      margin: 20,
      smartSpeed: 1000,
      autoplay: true,
      pauseOnHover: false,
      responsive: {
        600: {
          margin: 20,
          items: 2
        },
        1000: {
          margin: 20,
          stagePadding: 0,
          nav: true,
          items: 4
        }
      }
    });
  }

})

