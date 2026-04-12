// Animated Logo with World Map and Cybernetic Symbol
document.addEventListener('DOMContentLoaded', function() {
  const logoContainer = document.querySelector('.logo');
  
  // Create SVG canvas for animated logo
  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.setAttribute('width', '50');
  svg.setAttribute('height', '50');
  svg.setAttribute('viewBox', '0 0 100 100');
  svg.setAttribute('class', 'animated-logo-svg');
  svg.style.marginRight = '10px';
  svg.style.display = 'inline-block';
  svg.style.verticalAlign = 'middle';
  
  // Define styles
  const defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
  const style = document.createElementNS('http://www.w3.org/2000/svg', 'style');
  style.textContent = `
    @keyframes rotate-world {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }
    @keyframes pulse-core {
      0%, 100% { r: 8; opacity: 1; }
      50% { r: 12; opacity: 0.6; }
    }
    @keyframes glow-ring {
      0%, 100% { stroke-width: 1; opacity: 0.8; }
      50% { stroke-width: 2; opacity: 1; }
    }
    .world-map {
      animation: rotate-world 20s linear infinite;
      transform-origin: 50px 50px;
    }
    .core-pulse {
      animation: pulse-core 2s ease-in-out infinite;
    }
    .glow-ring {
      animation: glow-ring 2s ease-in-out infinite;
    }
  `;
  defs.appendChild(style);
  svg.appendChild(defs);
  
  // Background circle
  const bgCircle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
  bgCircle.setAttribute('cx', '50');
  bgCircle.setAttribute('cy', '50');
  bgCircle.setAttribute('r', '48');
  bgCircle.setAttribute('fill', '#f5f0e8');
  bgCircle.setAttribute('stroke', '#001f3f');
  bgCircle.setAttribute('stroke-width', '1');
  svg.appendChild(bgCircle);
  
  // World map group (rotating)
  const worldGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
  worldGroup.setAttribute('class', 'world-map');
  
  // Simplified world map outline
  const continents = [
    // North America
    { path: 'M 15 25 L 20 20 L 25 22 L 23 30 L 18 32 Z', fill: '#001f3f', opacity: 0.6 },
    // South America
    { path: 'M 20 35 L 25 32 L 26 45 L 22 48 Z', fill: '#001f3f', opacity: 0.6 },
    // Europe
    { path: 'M 45 20 L 52 18 L 55 25 L 48 28 Z', fill: '#001f3f', opacity: 0.6 },
    // Africa
    { path: 'M 50 30 L 58 28 L 60 45 L 52 48 Z', fill: '#001f3f', opacity: 0.6 },
    // Asia
    { path: 'M 60 20 L 75 18 L 78 35 L 65 38 Z', fill: '#001f3f', opacity: 0.6 },
    // Australia
    { path: 'M 72 45 L 78 44 L 77 52 L 71 53 Z', fill: '#001f3f', opacity: 0.6 },
  ];
  
  continents.forEach(continent => {
    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    path.setAttribute('d', continent.path);
    path.setAttribute('fill', continent.fill);
    path.setAttribute('opacity', continent.opacity);
    worldGroup.appendChild(path);
  });
  
  // Orbital rings
  const ring1 = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
  ring1.setAttribute('cx', '50');
  ring1.setAttribute('cy', '50');
  ring1.setAttribute('r', '35');
  ring1.setAttribute('fill', 'none');
  ring1.setAttribute('stroke', '#c9a962');
  ring1.setAttribute('stroke-width', '0.5');
  ring1.setAttribute('opacity', '0.4');
  worldGroup.appendChild(ring1);
  
  const ring2 = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
  ring2.setAttribute('cx', '50');
  ring2.setAttribute('cy', '50');
  ring2.setAttribute('r', '42');
  ring2.setAttribute('fill', 'none');
  ring2.setAttribute('stroke', '#001f3f');
  ring2.setAttribute('stroke-width', '0.5');
  ring2.setAttribute('opacity', '0.3');
  worldGroup.appendChild(ring2);
  
  svg.appendChild(worldGroup);
  
  // Cybernetic core - central pulsing element
  const coreCircle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
  coreCircle.setAttribute('cx', '50');
  coreCircle.setAttribute('cy', '50');
  coreCircle.setAttribute('r', '8');
  coreCircle.setAttribute('fill', '#001f3f');
  coreCircle.setAttribute('class', 'core-pulse');
  svg.appendChild(coreCircle);
  
  // Glow ring around core
  const glowRing = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
  glowRing.setAttribute('cx', '50');
  glowRing.setAttribute('cy', '50');
  glowRing.setAttribute('r', '12');
  glowRing.setAttribute('fill', 'none');
  glowRing.setAttribute('stroke', '#c9a962');
  glowRing.setAttribute('stroke-width', '1');
  glowRing.setAttribute('class', 'glow-ring');
  svg.appendChild(glowRing);
  
  // Cybernetic nodes (4 points around core)
  const nodePositions = [
    { x: 50, y: 20 },  // top
    { x: 80, y: 50 },  // right
    { x: 50, y: 80 },  // bottom
    { x: 20, y: 50 }   // left
  ];
  
  nodePositions.forEach((pos, index) => {
    const node = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    node.setAttribute('cx', pos.x);
    node.setAttribute('cy', pos.y);
    node.setAttribute('r', '2');
    node.setAttribute('fill', '#c9a962');
    svg.appendChild(node);
    
    // Connection lines from core to nodes
    const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    line.setAttribute('x1', '50');
    line.setAttribute('y1', '50');
    line.setAttribute('x2', pos.x);
    line.setAttribute('y2', pos.y);
    line.setAttribute('stroke', '#c9a962');
    line.setAttribute('stroke-width', '0.5');
    line.setAttribute('opacity', '0.5');
    svg.appendChild(line);
  });
  
  // Insert logo before the h1
  const h1 = logoContainer.querySelector('h1');
  logoContainer.insertBefore(svg, h1);
});
