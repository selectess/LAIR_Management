// LAIRM - Main JavaScript

// Navbar scroll effect
const navbar = document.getElementById('navbar');
let lastScroll = 0;

window.addEventListener('scroll', () => {
  const currentScroll = window.pageYOffset;
  
  if (currentScroll > 50) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
  
  lastScroll = currentScroll;
});

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      const offsetTop = target.offsetTop - 80;
      window.scrollTo({
        top: offsetTop,
        behavior: 'smooth'
      });
    }
  });
});

// Scroll animations
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, observerOptions);

// Observe all elements with scroll-animate class
document.querySelectorAll('.scroll-animate').forEach(el => {
  observer.observe(el);
});

// Waitlist form submission
const waitlistForm = document.getElementById('waitlistForm');
if (waitlistForm) {
  waitlistForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const email = e.target.querySelector('input[type="email"]').value;
    const button = e.target.querySelector('button');
    const originalText = button.textContent;
    
    // Disable button and show loading state
    button.disabled = true;
    button.textContent = 'Subscribing...';
    
    try {
      // Here you would normally send to your backend
      // For now, we'll simulate a successful submission
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      // Success state
      button.textContent = '✓ Subscribed!';
      button.style.background = '#4ade80';
      e.target.querySelector('input[type="email"]').value = '';
      
      // Reset after 3 seconds
      setTimeout(() => {
        button.disabled = false;
        button.textContent = originalText;
        button.style.background = '';
      }, 3000);
      
    } catch (error) {
      // Error state
      button.textContent = 'Error - Try again';
      button.style.background = '#ef4444';
      
      setTimeout(() => {
        button.disabled = false;
        button.textContent = originalText;
        button.style.background = '';
      }, 3000);
    }
  });
}

// Add stagger animation to grid items
const addStaggerAnimation = () => {
  const grids = document.querySelectorAll('.vision-grid, .axioms-grid, .framework-grid');
  
  grids.forEach(grid => {
    const items = grid.querySelectorAll('.scroll-animate');
    items.forEach((item, index) => {
      item.style.transitionDelay = `${index * 0.1}s`;
    });
  });
};

// Initialize stagger animations
addStaggerAnimation();

// Parallax effect for hero section
window.addEventListener('scroll', () => {
  const scrolled = window.pageYOffset;
  const hero = document.querySelector('.hero-content');
  if (hero && scrolled < window.innerHeight) {
    hero.style.transform = `translateY(${scrolled * 0.3}px)`;
    hero.style.opacity = 1 - (scrolled / window.innerHeight);
  }
});

// Add active state to navigation links
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', () => {
  let current = '';
  
  sections.forEach(section => {
    const sectionTop = section.offsetTop;
    const sectionHeight = section.clientHeight;
    if (pageYOffset >= sectionTop - 100) {
      current = section.getAttribute('id');
    }
  });
  
  navLinks.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === `#${current}`) {
      link.classList.add('active');
    }
  });
});

// Console message
console.log('%cLAIR Management', 'font-size: 24px; font-weight: bold; color: #c9a962;');
console.log('%cThe Cybernetic Criterion', 'font-size: 14px; color: #003366;');
console.log('%cGlobal Agentive Constitution 2026-2036', 'font-size: 12px; color: #666;');
console.log('%c\nGitHub: https://github.com/selectess/LAIR_Management', 'font-size: 12px; color: #c9a962;');
