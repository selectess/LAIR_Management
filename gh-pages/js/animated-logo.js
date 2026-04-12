// Animated Logo - 19 Lighthouses in Pyramid Formation
function createAnimatedLogo(size = 50) {
  // Create SVG canvas for animated logo
  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.setAttribute('width', size);
  svg.setAttribute('height', size);
  svg.setAttribute('viewBox', '0 0 200 200');
  svg.setAttribute('class', 'animated-logo-svg');
  
  // Define styles
  const defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
  const style = document.createElementNS('http://www.w3.org/2000/svg', 'style');
  style.textContent = `
    @keyframes pulse-light {
      0%, 100% { opacity: 0.8; }
      50% { opacity: 1; }
    }
    @keyframes beam-sweep {
      0%, 100% { opacity: 0.3; }
      50% { opacity: 0.7; }
    }
    @keyframes glow-core {
      0%, 100% { filter: brightness(1); }
      50% { filter: brightness(1.5); }
    }
    .lighthouse-beam {
      animation: beam-sweep 3s ease-in-out infinite;
    }
    .lighthouse-light {
      animation: pulse-light 2s ease-in-out infinite;
    }
    .central-lighthouse {
      animation: glow-core 2s ease-in-out infinite;
    }
  `;
  defs.appendChild(style);
  svg.appendChild(defs);
  
  // Background
  const bgRect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
  bgRect.setAttribute('width', '200');
  bgRect.setAttribute('height', '200');
  bgRect.setAttribute('fill', '#f5f0e8');
  svg.appendChild(bgRect);
  
  // 19 Lighthouses positioned in pyramid formation
  // Row 1 (back, smallest): 5 lighthouses
  // Row 2: 4 lighthouses
  // Row 3: 3 lighthouses
  // Row 4: 3 lighthouses
  // Row 5: 2 lighthouses
  // Row 6 (front, center): 1 lighthouse (largest - Ψ-I)
  // Row 7 (front sides): 1 lighthouse
  
  const lighthouses = [
    // Back row (smallest, furthest) - 5 lighthouses
    { x: 40, y: 30, height: 15, width: 4, light: 2, beam: 25, label: 'X' },
    { x: 70, y: 28, height: 16, width: 4, light: 2, beam: 26, label: 'XI' },
    { x: 100, y: 26, height: 17, width: 4, light: 2, beam: 27, label: 'XII' },
    { x: 130, y: 28, height: 16, width: 4, light: 2, beam: 26, label: 'XIII' },
    { x: 160, y: 30, height: 15, width: 4, light: 2, beam: 25, label: 'XIV' },
    
    // Row 2 - 4 lighthouses
    { x: 55, y: 50, height: 20, width: 5, light: 2.5, beam: 30, label: 'XV' },
    { x: 85, y: 48, height: 21, width: 5, light: 2.5, beam: 31, label: 'XVI' },
    { x: 115, y: 48, height: 21, width: 5, light: 2.5, beam: 31, label: 'XVII' },
    { x: 145, y: 50, height: 20, width: 5, light: 2.5, beam: 30, label: 'XVIII' },
    
    // Row 3 - 3 lighthouses
    { x: 70, y: 70, height: 25, width: 6, light: 3, beam: 35, label: 'XIX' },
    { x: 100, y: 68, height: 26, width: 6, light: 3, beam: 36, label: 'II' },
    { x: 130, y: 70, height: 25, width: 6, light: 3, beam: 35, label: 'III' },
    
    // Row 4 - 3 lighthouses
    { x: 60, y: 95, height: 30, width: 7, light: 3.5, beam: 40, label: 'IV' },
    { x: 100, y: 93, height: 31, width: 7, light: 3.5, beam: 41, label: 'V' },
    { x: 140, y: 95, height: 30, width: 7, light: 3.5, beam: 40, label: 'VI' },
    
    // Row 5 - 2 lighthouses
    { x: 75, y: 120, height: 35, width: 8, light: 4, beam: 45, label: 'VII' },
    { x: 125, y: 120, height: 35, width: 8, light: 4, beam: 45, label: 'VIII' },
    
    // Row 6 - 1 lighthouse (front side)
    { x: 90, y: 145, height: 38, width: 9, light: 4.5, beam: 48, label: 'IX' },
    
    // Central lighthouse (largest, most luminous) - Ψ-I
    { x: 100, y: 160, height: 45, width: 12, light: 6, beam: 55, label: 'I', central: true }
  ];
  
  // Draw all light beams first (behind lighthouses)
  const beamGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
  beamGroup.setAttribute('opacity', '0.4');
  
  // Create crossing beams between lighthouses
  lighthouses.forEach((lh1, i) => {
    lighthouses.forEach((lh2, j) => {
      if (i < j && Math.random() > 0.6) { // Random connections for visual interest
        const beam = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        beam.setAttribute('x1', lh1.x);
        beam.setAttribute('y1', lh1.y - lh1.height);
        beam.setAttribute('x2', lh2.x);
        beam.setAttribute('y2', lh2.y - lh2.height);
        beam.setAttribute('stroke', '#c9a962');
        beam.setAttribute('stroke-width', '0.5');
        beam.setAttribute('class', 'lighthouse-beam');
        beam.setAttribute('style', `animation-delay: ${i * 0.2}s`);
        beamGroup.appendChild(beam);
      }
    });
  });
  
  svg.appendChild(beamGroup);
  
  // Draw nodes where beams cross (simplified - at lighthouse tops)
  lighthouses.forEach((lh, i) => {
    const node = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    node.setAttribute('cx', lh.x);
    node.setAttribute('cy', lh.y - lh.height);
    node.setAttribute('r', lh.light * 0.8);
    node.setAttribute('fill', '#c9a962');
    node.setAttribute('opacity', '0.6');
    node.setAttribute('class', 'lighthouse-light');
    node.setAttribute('style', `animation-delay: ${i * 0.15}s`);
    svg.appendChild(node);
  });
  
  // Draw lighthouses from back to front
  lighthouses.forEach((lh, index) => {
    const group = document.createElementNS('http://www.w3.org/2000/svg', 'g');
    if (lh.central) {
      group.setAttribute('class', 'central-lighthouse');
    }
    
    // Lighthouse base
    const base = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
    base.setAttribute('x', lh.x - lh.width / 2);
    base.setAttribute('y', lh.y - lh.height * 0.3);
    base.setAttribute('width', lh.width);
    base.setAttribute('height', lh.height * 0.3);
    base.setAttribute('fill', '#001f3f');
    base.setAttribute('stroke', '#c9a962');
    base.setAttribute('stroke-width', '0.5');
    group.appendChild(base);
    
    // Lighthouse tower
    const tower = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
    tower.setAttribute('x', lh.x - lh.width / 2.5);
    tower.setAttribute('y', lh.y - lh.height);
    tower.setAttribute('width', lh.width / 1.25);
    tower.setAttribute('height', lh.height * 0.7);
    tower.setAttribute('fill', lh.central ? '#003366' : '#001f3f');
    tower.setAttribute('stroke', '#c9a962');
    tower.setAttribute('stroke-width', '0.5');
    group.appendChild(tower);
    
    // Light chamber
    const chamber = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
    chamber.setAttribute('x', lh.x - lh.width / 2);
    chamber.setAttribute('y', lh.y - lh.height);
    chamber.setAttribute('width', lh.width);
    chamber.setAttribute('height', lh.height * 0.15);
    chamber.setAttribute('fill', '#c9a962');
    chamber.setAttribute('opacity', lh.central ? '1' : '0.8');
    group.appendChild(chamber);
    
    // Light source (glowing)
    const light = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    light.setAttribute('cx', lh.x);
    light.setAttribute('cy', lh.y - lh.height);
    light.setAttribute('r', lh.light);
    light.setAttribute('fill', '#c9a962');
    light.setAttribute('opacity', lh.central ? '1' : '0.7');
    light.setAttribute('class', 'lighthouse-light');
    light.setAttribute('style', `animation-delay: ${index * 0.1}s`);
    group.appendChild(light);
    
    // Light beam (upward)
    const beamPath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    const beamWidth = lh.beam;
    beamPath.setAttribute('d', `M ${lh.x - beamWidth/2} ${lh.y - lh.height} L ${lh.x - beamWidth} ${lh.y - lh.height - lh.beam} L ${lh.x + beamWidth} ${lh.y - lh.height - lh.beam} L ${lh.x + beamWidth/2} ${lh.y - lh.height} Z`);
    beamPath.setAttribute('fill', '#c9a962');
    beamPath.setAttribute('opacity', lh.central ? '0.3' : '0.2');
    beamPath.setAttribute('class', 'lighthouse-beam');
    beamPath.setAttribute('style', `animation-delay: ${index * 0.1}s`);
    group.appendChild(beamPath);
    
    svg.appendChild(group);
  });
  
  // Ground/water line
  const ground = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
  ground.setAttribute('x', '0');
  ground.setAttribute('y', '180');
  ground.setAttribute('width', '200');
  ground.setAttribute('height', '20');
  ground.setAttribute('fill', '#001f3f');
  ground.setAttribute('opacity', '0.2');
  svg.appendChild(ground);
  
  return svg;
}

document.addEventListener('DOMContentLoaded', function() {
  // Add logo to header
  const logoContainer = document.querySelector('.logo');
  if (logoContainer) {
    const h1 = logoContainer.querySelector('h1');
    const headerLogo = createAnimatedLogo(60);
    headerLogo.style.marginRight = '12px';
    logoContainer.insertBefore(headerLogo, h1);
  }
  
  // Add larger logo to hero section
  const heroContent = document.querySelector('.hero-content');
  if (heroContent) {
    const heroTitle = heroContent.querySelector('.hero-title');
    const heroLogoContainer = document.createElement('div');
    heroLogoContainer.className = 'hero-logo-container';
    const heroLogo = createAnimatedLogo(150);
    heroLogoContainer.appendChild(heroLogo);
    heroContent.insertBefore(heroLogoContainer, heroTitle);
  }
});
