// main.js inicial
document.addEventListener('DOMContentLoaded', function () {
  var imgs = document.querySelectorAll('.carousel-slide img');
  function openLightbox(src, alt) {
    var overlay = document.createElement('div');
    overlay.className = 'lightbox-overlay';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    var content = document.createElement('div');
    content.className = 'lightbox-content';
    var image = document.createElement('img');
    image.className = 'lightbox-image';
    image.src = src;
    image.alt = alt || '';
    var close = document.createElement('button');
    close.className = 'lightbox-close';
    close.setAttribute('aria-label', 'Fechar');
    close.textContent = '×';
    content.appendChild(image);
    content.appendChild(close);
    overlay.appendChild(content);
    document.body.appendChild(overlay);
    var prevOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    function closeLightbox() {
      document.body.style.overflow = prevOverflow || '';
      document.removeEventListener('keydown', onKey);
      overlay.remove();
    }
    function onKey(e) {
      if (e.key === 'Escape') closeLightbox();
    }
    document.addEventListener('keydown', onKey);
    close.addEventListener('click', closeLightbox);
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) closeLightbox();
    });
  }
  imgs.forEach(function (img) {
    img.style.cursor = 'zoom-in';
    img.addEventListener('click', function () {
      openLightbox(img.src, img.alt);
    });
  });
});
