// ============================================================================
// LAIRM Teaser - Main JavaScript
// ============================================================================

document.addEventListener('DOMContentLoaded', function() {
  initScrollAnimations();
  initSmoothScroll();
});

// ============================================================================
// Scroll Animations
// ============================================================================

function initScrollAnimations() {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, observerOptions);

  // Observe all elements with scroll-animate class
  document.querySelectorAll('.axiom-card, .case-card').forEach(el => {
    el.classList.add('scroll-animate');
    observer.observe(el);
  });
}

// ============================================================================
// Smooth Scroll
// ============================================================================

function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
}

// ============================================================================
// Navbar Scroll Effect
// ============================================================================

window.addEventListener('scroll', function() {
  const navbar = document.querySelector('.navbar');
  if (window.scrollY > 50) {
    navbar.style.borderBottomColor = 'rgba(201, 169, 98, 0.3)';
  } else {
    navbar.style.borderBottomColor = 'rgba(201, 169, 98, 0.15)';
  }
});

// ============================================================================
// Active Navigation Link
// ============================================================================

window.addEventListener('scroll', function() {
  const sections = document.querySelectorAll('section');
  const navLinks = document.querySelectorAll('.nav-links a');

  let current = '';
  sections.forEach(section => {
    const sectionTop = section.offsetTop;
    if (pageYOffset >= sectionTop - 200) {
      current = section.getAttribute('id');
    }
  });

  navLinks.forEach(link => {
    link.style.color = 'var(--text-secondary)';
    if (link.getAttribute('href').slice(1) === current) {
      link.style.color = 'var(--accent-gold)';
    }
  });
});

console.log('LAIRM Teaser loaded successfully');
