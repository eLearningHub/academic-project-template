window.HELP_IMPROVE_VIDEOJS = false;

// Update base path for interpolation images
var INTERP_BASE = "./interpolation/stacked";
var NUM_INTERP_FRAMES = 240;

var interp_images = [];
function preloadInterpolationImages() {
  for (var i = 0; i < NUM_INTERP_FRAMES; i++) {
    var path = INTERP_BASE + '/' + String(i).padStart(6, '0') + '.jpg';
    interp_images[i] = new Image();
    interp_images[i].src = path;
  }
}

function setInterpolationImage(i) {
  var image = interp_images[i];
  if (image) {
    image.ondragstart = function() { return false; };
    image.oncontextmenu = function() { return false; };
    $('#interpolation-image-wrapper').empty().append(image);
  }
}

$(document).ready(function() {
    // Initialize navbar burger menu
    $(".navbar-burger").click(function() {
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");
    });

    // Carousel configuration
    var carouselOptions = {
        slidesToScroll: 1,
        slidesToShow: 3,
        loop: true,
        infinite: true,
        autoplay: false,
        autoplaySpeed: 3000,
        pagination: false,
        navigationSwipe: true,
        navigationKeys: true
    };

    // Initialize carousels
    var carousels = bulmaCarousel.attach('.carousel', carouselOptions);
    console.log('Carousels initialized:', carousels);

    // Add event listeners to carousels
    carousels.forEach(carousel => {
        carousel.on('before:show', state => {
            console.log('Slide changing:', state);
        });
    });

    // Initialize interpolation
    try {
        preloadInterpolationImages();
        
        $('#interpolation-slider').on('input', function(event) {
            setInterpolationImage(this.value);
        });
        
        setInterpolationImage(0);
        $('#interpolation-slider').prop('max', NUM_INTERP_FRAMES - 1);
    } catch (e) {
        console.warn('Interpolation initialization failed:', e);
    }

    // Initialize Bulma slider
    if (typeof bulmaSlider !== 'undefined') {
        bulmaSlider.attach();
    }

    // Handle video elements
    document.querySelectorAll('video').forEach(video => {
        video.addEventListener('loadedmetadata', function() {
            console.log('Video loaded:', video.id);
        });
        
        // Add error handling for videos
        video.addEventListener('error', function() {
            console.warn('Error loading video:', video.id);
        });
    });
});