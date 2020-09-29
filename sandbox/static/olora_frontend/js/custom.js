(function ($) {
  "use strict";
  // niceSelect js code
  $(document).ready(function () {
    $("select").niceSelect();
  });

  $(".popup-youtube, .popup-vimeo").magnificPopup({
    // disableOn: 700,
    type: "iframe",
    mainClass: "mfp-fade",
    removalDelay: 160,
    preloader: false,
    fixedContentPos: false,
  });

  $(".banner_text").slick({
    vertical: true,
    verticalSwiping: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    arrows: true,
    autoplaySpeed: 3000,
    pauseOnHover: true,
    pauseOnHover: true,
    touchMove: true,
    verticalSwiping: true,
    prevArrow: $(".prev"),
    nextArrow: $(".next"),
  });

  // service_slider js code
  var service = $(".service_slider");
  if (service.length) {
    service.owlCarousel({
      items: 1,
      loop: true,
      dots: false,
      autoplay: true,
      autoplayHoverPause: true,
      autoplayTimeout: 5000,
      nav: true,
      smartSpeed: 2000,
      navText: [
        '<i class="ti-angle-left"></i>',
        '<i class="ti-angle-right"></i>',
      ],
      responsive: {
        0: {
          nav: false,
        },
        768: {
          nav: true,
        },
        992: {
          nav: true,
        },
      },
    });
  }
  // project_slider js code
  var project = $(".project_slider");
  if (project.length) {
    project.owlCarousel({
      items: 1,
      loop: true,
      dots: false,
      autoplay: true,
      autoplayHoverPause: true,
      autoplayTimeout: 5000,
      nav: true,
      smartSpeed: 2000,
      navText: [
        '<i class="flaticon-left-arrow"></i>',
        '<i class="flaticon-right-arrow"></i>',
      ],
      responsive: {
        0: {
          nav: false,
        },
        768: {
          nav: true,
        },
        992: {
          nav: true,
        },
      },
    });
  }
  // blog_slider js code
  var single_page = $(".single_page_special_item");
  if (single_page.length) {
    single_page.owlCarousel({
      items: 4,
      loop: true,
      dots: false,
      autoplay: true,
      autoplayHoverPause: true,
      autoplayTimeout: 5000,
      nav: true,
      smartSpeed: 2000,
      navText: [
        '<i class="flaticon-left-arrow"></i>',
        '<i class="flaticon-right-arrow"></i>',
      ],
      responsive: {
        0: {
          nav: false,
          items: 1,
        },
        576: {
          items: 1,
        },
        768: {
          nav: true,
          items: 2,
        },
        992: {
          nav: true,
          items: 3,
        },
        1200: {
          nav: true,
          items: 3,
        },
      },
    });
  }

  $(".blog_post_slider")
    .on("initialized.owl.carousel changed.owl.carousel", function (e) {
      if (!e.namespace) {
        return;
      }
      var carousel = e.relatedTarget;
      $(".slider-counter").text(
        carousel.relative(carousel.current()) +
          1 +
          "/" +
          carousel.items().length
      );
    })
    .owlCarousel({
      items: 1,
      loop: true,
      dots: false,
      autoplay: true,
      autoplayHoverPause: true,
      autoplayTimeout: 5000,
      nav: true,
      smartSpeed: 2000,
      navText: ["", "NEXT"],
    });
  // map js code
  var map = $(".map");
  if (map.length) {
    $(".map").gmap3({
      center: [40.74, -74.18],
      zoom: 12,
    });
  }
  // menu fixed js code
  if (!window.matchMedia("(max-width: 575px)").matches) {
    var interval = setInterval(() => {
      if ($(window).scrollTop() > 50) {
        $(".main_menu").addClass("menu_fixed animated");
      } else {
        $(".main_menu").removeClass("menu_fixed animated");
      }
    }, 250);
  }
  // Search Toggle
  $("#search_input_box").hide();
  $("#search_1").on("click", function () {
    $("#search_input_box").slideToggle();
    $("#search_input").focus();
  });
  $("#close_search").on("click", function () {
    $("#search_input_box").slideUp(500);
  });

  //memnu js

  $(".toggelContainer").on("click", function () {
    $("body").toggleClass("showToggle");
    $(".off-canven-menu").addClass("active");
    $(".offcanvas-overlay").addClass("active");
  });
  $(".close-icon i, .offcanvas-overlay").on("click", function () {
    $(".off-canven-menu").removeClass("active");
    $(".offcanvas-overlay").removeClass("active");
  });

  //gallery js
  $(".grid").masonry({
    itemSelector: ".grid-item",
    columnWidth: ".grid-sizer",
    percentPosition: true,
  });

  $(".gallery").each(function () {
    // the containers for all your galleries
    $(this).magnificPopup({
      delegate: "a", // the selector for gallery item
      type: "image",
      gallery: {
        enabled: true,
      },
    });
  });

  //------- Mailchimp js --------//
  function mailChimp() {
    $("#mc_embed_signup").find("form").ajaxChimp();
  }
  mailChimp();
})(jQuery);

// ************************* Mobile responsive ******************************* //

wow = new WOW({
  animateClass: "animated",
  offset: 100,
  callback: function (box) {
    // console.log("WOW: animating <" + box.tagName.toLowerCase() + ">");
  },
});
wow.init();

if ($(".portfolioAccordion").length) {
  $(".portfolioimgBlock").click(function () {
    $(".portfolioimgBlock").removeClass("active");
    $(this).toggleClass("active");
  });
}
// $(function () {
//   // Smooth Scrolling
//   $('.canven-menu-iner a[href*="#"]:not([href="#"])').click(function () {
//     if (
//       location.pathname.replace(/^\//, "") ==
//         this.pathname.replace(/^\//, "") &&
//       location.hostname == this.hostname
//     ) {
//       var target = $(this.hash);
//       target = target.length ? target : $("[name=" + this.hash.slice(1) + "]");
//       if (target.length) {
//         $("html, body").animate(
//           {
//             scrollTop: target.offset().top(600),
//           },
//           1000
//         );
//         return false;
//       }
//     }
//   });
// });

var firstNavigation;
var sections = $("section"),
  nav = $("nav");
var mobileMode;

$(document).ready(function () {
  // This is needed to make stop pause function work
  $("#indexSlider").carousel({
    pause: "",
    ride: false,
  });
  if (window.innerWidth < 575) {
    mobileMode = true;
  }
});

function switchToDesktop() {
  $("section")
    .css("display", "block")
    .css("opacity", "1")
    .css("transform", "none")
    .find("*")
    .each(function () {
      $(this).removeAttr("style");
    });

  $(".mobile-mode").removeClass("mobile-mode");
  $(".desktopLink").hide();
  $("#indexSlider").carousel("cycle");
  mobileMode = false;
}

$(window).on("scroll", function () {
  var cur_pos = $(this).scrollTop();

  sections.each(function () {
    var top = $(this).offset().top - 200;
    bottom = top + $(this).outerHeight();

    if (cur_pos >= top && cur_pos <= bottom) {
      nav.find("a").removeClass("active");
      sections.removeClass("active");

      $(this).addClass("active");
      nav.find('a[href="#' + $(this).attr("id") + '"]').addClass("active");
    }
  });
});

nav.find("a").on("click", function () {
  if (mobileMode) {
    switchToDesktop();
  }
  var $el = $(this),
    id = $el.attr("href");

  $("html, body").animate(
    {
      scrollTop: $(id).offset().top,
    },
    500
  );
  return false;
});
// Footer nav fixes
$("a.quick-link").on("click", function (e) {
  if (mobileMode) {
    switchToDesktop();
  }
  var $el = $(this),
    id = $el.attr("href");
  // Fix for footer navigation
  if ($(id).offset()) {
    e.preventDefault();
    sr.reveal($(id), { mobile: false, viewFactor: 0 });
    e.preventDefault();
    setTimeout(function () {
      $("html, body").animate(
        {
          scrollTop: $(id).offset().top,
        },
        500
      );
    }, 300);
  }
});

$(".btn_1.button-contactForm").on("click", function () {
  // Ensure contact submits first click
  return true;
});

// Mobile learn more buttons
$("a.btn_1").on("click", function (e) {
  // Check if mobile
  if (window.innerWidth <= 575 && mobileMode) {
    // Hide all sections
    $("section").css("display", "none").css("opacity", "0");
    // Show selected section

    $($(this).attr("reveal"))
      .css("display", "block")
      .css("opacity", "1")
      .css("transform", "none")
      .find("*")
      .each(function () {
        $(this).removeAttr("style");
      });
    // Disable autoplays
    $("#indexSlider").carousel("pause");
  } else {
    // Desktop manual scroll and reveal animation in preporation
    var $el = $(this),
      id = $el.attr("reveal");

    sr.reveal($(id), { viewFactor: 0 });
    if ($(id) && $(id).offset()) {
      $("html, body").animate(
        {
          scrollTop: $(id).offset().top,
        },
        500
      );
    }
    return true;
  }
});

// Mobile footer desktop link
$(".desktopLink").click(function () {
  // Check if mobile
  if (window.innerWidth <= 575) {
    switchToDesktop();
    $("html, body").animate({ scrollTop: 0 }, 0);
  }
});
