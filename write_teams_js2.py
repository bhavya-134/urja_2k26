import codecs

js_code = """
const volunteerNames = [
  "Aayush Rai", "Adarsh", "Arun", "Bhavya Joshi", "Dalaja", "Dev", "Dev Bhatt", "Devam", "Dhruvi", "Dhruti Parmar",
  "Elisha", "Harsh", "Hetarth Shah", "Hetvi", "Hitarth", "Hrishi", "Jashmin Vaghashiya", "Jay", "Jeet", "Kashyap",
  "Krish", "Kunal", "Manav", "Megh", "Meet", "Mihir Makwana", "Moxit", "Neel", "Neel Nikam", "Neel Patel",
  "Neel Sardhara", "Neet", "Nisarg", "Om", "Om Sonani", "Pari Tandel", "Phalak", "Prakash Chaudhary", "Prachi",
  "Raj", "Revaty", "Revathy", "Rujal Ghori", "Rupesh Nikam", "Sai Tanikella", "Sanket", "Shaan", "Tisha Patel",
  "Tisha Prajapati", "Vaishnavi", "Vansh Patel", "Vishva", "Yuvraj"
];

(function initTeams() {
  document.addEventListener('DOMContentLoaded', () => {
    // 1. Volunteer Grid Setup
    const volGrid = document.getElementById('vol-grid');
    const showAllBtn = document.getElementById('vol-show-all');
    const termLine = document.getElementById('term-line');
    const volSection = document.getElementById('volunteer-section');

    if (volGrid) {
      let html = '';
      volunteerNames.forEach(name => {
        html += `<div class="vol-node">${name}</div>`;
      });
      volGrid.innerHTML = html;

      const nodes = Array.from(document.querySelectorAll('.vol-node'));
      let waveIndex = 0;
      const waveSize = 5;
      let cascadeTimer = null;
      let hasBooted = false;

      function bootNetwork() {
        if (hasBooted) return;
        hasBooted = true;
        
        cascadeTimer = setInterval(() => {
          const start = waveIndex * waveSize;
          const end = start + waveSize;
          const waveNodes = nodes.slice(start, end);
          
          if (waveNodes.length === 0) {
            clearInterval(cascadeTimer);
            if(termLine) termLine.style.opacity = 1;
            if(showAllBtn) showAllBtn.style.display = 'none';
            return;
          }
          
          waveNodes.forEach(n => n.classList.add('online'));
          waveIndex++;
        }, 300);
      }

      function showAll() {
        if(cascadeTimer) clearInterval(cascadeTimer);
        nodes.forEach(n => n.classList.add('online'));
        if(termLine) termLine.style.opacity = 1;
        if(showAllBtn) showAllBtn.style.display = 'none';
        hasBooted = true;
      }

      if (showAllBtn) {
        showAllBtn.addEventListener('click', showAll);
      }

      // Observer for Volunteers
      if(window.IntersectionObserver) {
        const volObserver = new IntersectionObserver((entries) => {
          entries.forEach(e => {
            if(e.isIntersecting && window.getComputedStyle(e.target).display !== 'none') {
              bootNetwork();
              volObserver.unobserve(e.target);
            }
          });
        }, { threshold: 0.2 });

        if(volSection) volObserver.observe(volSection);
      }
    }

    // 2. Pulse Dividers Observer
    if(window.IntersectionObserver) {
      const pulseObserver = new IntersectionObserver((entries) => {
        entries.forEach(e => {
          if(e.isIntersecting && window.getComputedStyle(e.target).display !== 'none') {
            const dot = e.target.querySelector('.pulse-dot');
            if(dot) {
              dot.style.animation = 'none';
              void dot.offsetWidth; // trigger reflow
              dot.style.animation = 'pulseTravel 1.5s ease-in-out forwards';
            }
            pulseObserver.unobserve(e.target);
          }
        });
      }, { threshold: 0.5 });
      
      document.querySelectorAll('.pulse-divider').forEach(div => pulseObserver.observe(div));
    }
    
    // We also need to re-trigger observers when the user switches to the Teams tab
    // because IntersectionObserver fires once when hidden and then might not fire properly
    const teamsTabBtn = document.querySelector('[data-tab="teams"]');
    if (teamsTabBtn) {
      teamsTabBtn.addEventListener('click', () => {
        setTimeout(() => {
           const evt = new Event('scroll');
           window.dispatchEvent(evt);
        }, 300);
      });
    }

  });
})();
"""

with codecs.open('teams-app.js', 'w', 'utf-8') as f:
    f.write(js_code)
print("Updated teams-app.js with real volunteer names!")
