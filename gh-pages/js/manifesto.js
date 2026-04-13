// LAIRM Documentary Manifesto JavaScript

// Smooth scroll for TOC links
document.querySelectorAll('.toc-link, .toc-section-link').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            // Smooth scroll to target
            targetElement.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
            
            // Update active state
            document.querySelectorAll('.toc-link').forEach(l => l.classList.remove('active'));
            if (this.classList.contains('toc-link')) {
                this.classList.add('active');
            }
        }
    });
});

// Highlight active section in TOC on scroll
const observerOptions = {
    root: null,
    rootMargin: '-20% 0px -70% 0px',
    threshold: 0
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const id = entry.target.id;
            const correspondingLink = document.querySelector(`.toc-link[href="#${id}"]`);
            
            if (correspondingLink) {
                // Remove active from all links
                document.querySelectorAll('.toc-link').forEach(link => {
                    link.classList.remove('active');
                });
                
                // Add active to current link
                correspondingLink.classList.add('active');
            }
        }
    });
}, observerOptions);

// Observe all document entries
document.querySelectorAll('.doc-entry').forEach(entry => {
    observer.observe(entry);
});

// Back to top button
const backToTop = document.getElementById('backToTop');

window.addEventListener('scroll', () => {
    if (window.pageYOffset > 500) {
        backToTop.classList.add('visible');
    } else {
        backToTop.classList.remove('visible');
    }
});

backToTop.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// Smooth scroll for hero CTA
document.querySelector('.hero-cta')?.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
        target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
});

// Track reading progress
let readingProgress = {};

const progressObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const docId = entry.target.id;
            if (docId && !readingProgress[docId]) {
                readingProgress[docId] = {
                    timestamp: new Date().toISOString(),
                    title: entry.target.querySelector('.doc-title')?.textContent || 'Unknown'
                };
                console.log('Reading:', readingProgress[docId].title);
            }
        }
    });
}, {
    threshold: 0.5
});

document.querySelectorAll('.doc-entry').forEach(entry => {
    progressObserver.observe(entry);
});

// Save reading progress to localStorage
window.addEventListener('beforeunload', () => {
    localStorage.setItem('lairm-reading-progress', JSON.stringify(readingProgress));
});

// Load reading progress on page load
window.addEventListener('load', () => {
    const saved = localStorage.getItem('lairm-reading-progress');
    if (saved) {
        readingProgress = JSON.parse(saved);
        console.log('Loaded reading progress:', Object.keys(readingProgress).length, 'documents');
    }
});

// Print reading statistics
function getReadingStats() {
    const docsRead = Object.keys(readingProgress).length;
    const totalDocs = document.querySelectorAll('.doc-entry').length;
    const percentage = ((docsRead / totalDocs) * 100).toFixed(1);
    
    return {
        docsRead,
        totalDocs,
        percentage,
        estimatedTimeRemaining: Math.ceil((totalDocs - docsRead) * 15 / 60) // hours
    };
}

// Expose stats to console
window.getLAIRMStats = getReadingStats;

console.log('LAIRM Documentary Manifesto loaded');
console.log('Use getLAIRMStats() to see your reading progress');
