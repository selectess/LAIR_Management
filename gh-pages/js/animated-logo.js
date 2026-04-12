// Animated Logo - Robotic Lighthouse with Laser Web
function createAnimatedLogo(size = 50) {
  // Create SVG canvas for animated logo
  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.setAttribute('width', size);
  svg.setAttribute('height', size);
  svg.setAttribute('viewBox', '0 0 100 100');
  svg.setAttribute('class', 'animated-logo-svg');
  
  // Define styles
  const defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
  const style = document.createElementNS('http://www.w3.org/2000/svg', 'style');
  style.textContent = `
    @keyframes rotate-lasers {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }
    @keyframes pulse-light {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.4; }
    }
    @keyframes glow-core {
      0%, 100% { r: 6; opacity: 1; }
      50% { r: 8; opacity: 0.7; }
    }
    @keyframes pulse-web {
      0%, 100% { opacity: 0.3; }
      50% { opacity: 0.7; }
    }
    .laser-group {
      animation: rotate-lasers 12s linear infinite;
      transform-origin: 50px 30px;
    }
    .light-pulse {
      animation: pulse-light 2s ease-in-out infinite;
    }
    .core-glow {
      animation: glow-core 2s ease-in-out infinite;
    }
    .laser-web {
      animation: pulse-web 3s ease-in-out infinite;
    }
  `;
  defs.appendChild(style);
  
  // Gradient for lighthouse
  const gradient = document.createElementNS('http://www.w3.org/2000/svg', 'linearGradient');
  gradient.setAttribute('id', 'lighthouseGradient');
  gradient.setAttribute('x1', '0%');
  gradient.setAttribute('y1', '0%');
  gradient.setAttribute('x2', '0%');
  gradient.setAttribute('y2', '100%');
  
  const stop1 = document.createElementNS('http://www.w3.org/2000/svg', 'stop');
  stop1.setAttribute('offset', '0%');
  stop1.setAttribute('style', 'stop-color:#001f3f;stop-opacity:1');
  gradient.appendChild(stop1);
  
  const stop2 = document.createElementNS('http://www.w3.org/2000/svg', 'stop');
  stop2.setAttribute('offset', '100%');
  stop2.setAttribute('style', 'stop-color:#003366;stop-opacity:1');
  gradient.appendChild(stop2);
  
  defs.appendChild(gradient);
  svg.appendChild(defs);
  
  // Background circle
  const bgCircle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
  bgCircle.setAttribute('cx', '50');
  bgCircle.setAttribute('cy', '50');
  bgCircle.setAttribute('r', '48');
  bgCircle.setAttribute('fill', '#f5f0e8');
  bgCircle.setAttribute('stroke', '#001f3f');
  bgCircle.setAttribute('stroke-width', '1.5');
  svg.appendChild(bgCircle);
  
  // Ocean waves at bottom
  const wave1 = document.createElementNS('http://www.w3.org/2000/svg', 'path');
  wave1.setAttribute('d', 'M 10 75 Q 25 70 40 75 T 70 75 T 90 75 L 90 95 L 10 95 Z');
  wave1.setAttribute('fill', '#001f3f');
  wave1.setAttribute('opacity', '0.3');
  svg.appendChild(wave1);
  
  const wave2 = document.createElementNS('http://www.w3.org/2000/svg', 'path');
  wave2.setAttribute('d', 'M 10 80 Q 30 77 50 80 T 90 80 L 90 95 L 10 95 Z');
  wave2.setAttribute('fill', '#001f3f');
  wave2.setAttribute('opacity', '0.2');
  svg.appendChild(wave2);
  
  // Lighthouse base (wider at bottom)
  const lighthouseBase = document.createElementNS('http://www.w3.org/2000/svg', 'path');
  lighthouseBase.setAttribute('d', 'M 42 75 L 40 55 L 60 55 L 58 75 Z');
  lighthouseBase.setAttribute('fill', 'url(#lighthouseGradient)');
  lighthouseBase.setAttribute('stroke', '#001f3f');
  lighthouseBase.setAttribute('stroke-width', '1');
  svg.appendChild(lighthouseBase);
  
  // Lighthouse middle section
  const lighthouseMiddle = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
  lighthouseMiddle.setAttribute('x', '40');
  lighthouseMiddle.setAttribute('y', '35');
  lighthouseMiddle.setAttribute('width', '20');
  lighthouseMiddle.setAttribute('height', '20');
  lighthouseMiddle.setAttribute('fill', 'url(#lighthouseGradient)');
  lighthouseMiddle.setAttribute('stroke', '#001f3f');
  lighthouseMiddle.setAttribute('stroke-width', '1');
  svg.appendChild(lighthouseMiddle);
  
  // Robotic segments (horizontal lines)
  for (let i = 0; i < 3; i++) {
    const segment = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    segment.setAttribute('x1', '40');
    segment.setAttribute('y1', 42 + (i * 6));
    segment.setAttribute('x2', '60');
    segment.setAttribute('y2', 42 + (i * 6));
    segment.setAttribute('stroke', '#c9a962');
    segment.setAttribute('stroke-width', '0.5');
    segment.setAttribute('opacity', '0.6');
    svg.appendChild(segment);
  }
  
  // Lighthouse top (light chamber)
  const lightChamber = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
  lightChamber.setAttribute('x', '38');
  lightChamber.setAttribute('y', '25');
  lightChamber.setAttribute('width', '24');
  lightChamber.setAttribute('height', '10');
  lightChamber.setAttribute('fill', '#001f3f');
  lightChamber.setAttribute('stroke', '#c9a962');
  lightChamber.setAttribute('stroke-width', '1.5');
  svg.appendChild(lightChamber);
  
  // Lighthouse roof
  const roof = document.createElementNS('http://www.w3.org/2000/svg', 'path');
  roof.setAttribute('d', 'M 35 25 L 50 18 L 65 25 Z');
  roof.setAttribute('fill', '#c9a962');
  roof.setAttribute('stroke', '#001f3f');
  roof.setAttribute('stroke-width', '1');
  svg.appendChild(roof);
  
  // Laser beams group (rotating) with web structure
  const laserGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
  laserGroup.setAttribute('class', 'laser-group');
  
  // Create 8 main laser beams in beige
  const laserAngles = [0, 45, 90, 135, 180, 225, 270, 315];
  const laserEndPoints = [];
  
  laserAngles.forEach((angle, index) => {
    const radian = (angle * Math.PI) / 180;
    const x2 = 50 + Math.cos(radian) * 45;
    const y2 = 30 + Math.sin(radian) * 45;
    
    laserEndPoints.push({ x: x2, y: y2 });
    
    const laser = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    laser.setAttribute('x1', '50');
    laser.setAttribute('y1', '30');
    laser.setAttribute('x2', x2);
    laser.setAttribute('y2', y2);
    laser.setAttribute('stroke', '#c9a962');
    laser.setAttribute('stroke-width', '1.5');
    laser.setAttribute('opacity', '0.7');
    laser.setAttribute('class', 'light-pulse');
    laser.setAttribute('style', `animation-delay: ${index * 0.25}s`);
    laserGroup.appendChild(laser);
    
    // Laser endpoint glow
    const laserEnd = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    laserEnd.setAttribute('cx', x2);
    laserEnd.setAttribute('cy', y2);
    laserEnd.setAttribute('r', '2');
    laserEnd.setAttribute('fill', '#c9a962');
    laserEnd.setAttribute('opacity', '0.8');
    laserGroup.appendChild(laserEnd);
  });
  
  // Create web connections between laser endpoints (toile d'araignée)
  const webGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
  webGroup.setAttribute('class', 'laser-web');
  
  // Connect adjacent endpoints to form octagon
  for (let i = 0; i < laserEndPoints.length; i++) {
    const next = (i + 1) % laserEndPoints.length;
    const webLine = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    webLine.setAttribute('x1', laserEndPoints[i].x);
    webLine.setAttribute('y1', laserEndPoints[i].y);
    webLine.setAttribute('x2', laserEndPoints[next].x);
    webLine.setAttribute('y2', laserEndPoints[next].y);
    webLine.setAttribute('stroke', '#c9a962');
    webLine.setAttribute('stroke-width', '0.8');
    webLine.setAttribute('opacity', '0.4');
    webGroup.appendChild(webLine);
  }
  
  // Add inner web ring (connections at 60% distance)
  const innerPoints = [];
  laserAngles.forEach((angle) => {
    const radian = (angle * Math.PI) / 180;
    const x = 50 + Math.cos(radian) * 27;
    const y = 30 + Math.sin(radian) * 27;
    innerPoints.push({ x, y });
  });
  
  for (let i = 0; i < innerPoints.length; i++) {
    const next = (i + 1) % innerPoints.length;
    const innerWeb = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    innerWeb.setAttribute('x1', innerPoints[i].x);
    innerWeb.setAttribute('y1', innerPoints[i].y);
    innerWeb.setAttribute('x2', innerPoints[next].x);
    innerWeb.setAttribute('y2', innerPoints[next].y);
    innerWeb.setAttribute('stroke', '#c9a962');
    innerWeb.setAttribute('stroke-width', '0.6');
    innerWeb.setAttribute('opacity', '0.3');
    webGroup.appendChild(innerWeb);
  }
  
  // Add cross connections for web effect
  for (let i = 0; i < laserEndPoints.length; i += 2) {
    const opposite = (i + 4) % laserEndPoints.length;
    const crossWeb = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    crossWeb.setAttribute('x1', laserEndPoints[i].x);
    crossWeb.setAttribute('y1', laserEndPoints[i].y);
    crossWeb.setAttribute('x2', laserEndPoints[opposite].x);
    crossWeb.setAttribute('y2', laserEndPoints[opposite].y);
    crossWeb.setAttribute('stroke', '#c9a962');
    crossWeb.setAttribute('stroke-width', '0.5');
    crossWeb.setAttribute('opacity', '0.2');
    webGroup.appendChild(crossWeb);
  }
  
  laserGroup.appendChild(webGroup);
  svg.appendChild(laserGroup);
  
  // Central light core (pulsing)
  const lightCore = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
  lightCore.setAttribute('cx', '50');
  lightCore.setAttribute('cy', '30');
  lightCore.setAttribute('r', '6');
  lightCore.setAttribute('fill', '#c9a962');
  lightCore.setAttribute('class', 'core-glow');
  svg.appendChild(lightCore);
  
  // Inner core
  const innerCore = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
  innerCore.setAttribute('cx', '50');
  innerCore.setAttribute('cy', '30');
  innerCore.setAttribute('r', '3');
  innerCore.setAttribute('fill', '#f5f0e8');
  svg.appendChild(innerCore);
  
  // Robotic details - antenna on top
  const antenna = document.createElementNS('http://www.w3.org/2000/svg', 'line');
  antenna.setAttribute('x1', '50');
  antenna.setAttribute('y1', '18');
  antenna.setAttribute('x2', '50');
  antenna.setAttribute('y2', '12');
  antenna.setAttribute('stroke', '#c9a962');
  antenna.setAttribute('stroke-width', '1.5');
  svg.appendChild(antenna);
  
  const antennaTop = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
  antennaTop.setAttribute('cx', '50');
  antennaTop.setAttribute('cy', '12');
  antennaTop.setAttribute('r', '2');
  antennaTop.setAttribute('fill', '#c9a962');
  svg.appendChild(antennaTop);
  
  return svg;
}

document.addEventListener('DOMContentLoaded', function() {
  // Add logo to header
  const logoContainer = document.querySelector('.logo');
  const h1 = logoContainer.querySelector('h1');
  const headerLogo = createAnimatedLogo(60);
  headerLogo.style.marginRight = '12px';
  logoContainer.insertBefore(headerLogo, h1);
  
  // Add larger logo to hero section
  const heroContent = document.querySelector('.hero-content');
  const heroTitle = heroContent.querySelector('.hero-title');
  const heroLogoContainer = document.createElement('div');
  heroLogoContainer.className = 'hero-logo-container';
  const heroLogo = createAnimatedLogo(120);
  heroLogoContainer.appendChild(heroLogo);
  heroContent.insertBefore(heroLogoContainer, heroTitle);
});
