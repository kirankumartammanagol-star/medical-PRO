/* ============================================
   HealthCareer Pro - Main JavaScript
   ============================================ */

document.addEventListener('DOMContentLoaded', function() {

    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            navbar.classList.toggle('scrolled', window.scrollY > 50);
        });
    }

    // Mobile menu toggle
    const menuToggle = document.querySelector('.nav-menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            navLinks.style.display = navLinks.classList.contains('active') ? 'flex' : '';
        });
    }

    // Scroll reveal animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.card, .feature-card, .stat-card, .widget, .job-card').forEach(el => {
        el.style.opacity = '0';
        observer.observe(el);
    });

    // Animate stat numbers
    function animateNumbers() {
        document.querySelectorAll('.stat-number, .stat-value, .widget-value').forEach(el => {
            const target = parseInt(el.textContent.replace(/[^0-9]/g, ''));
            if (isNaN(target) || target === 0) return;
            
            let current = 0;
            const increment = target / 60;
            const suffix = el.textContent.replace(/[0-9,]/g, '');
            
            const timer = setInterval(() => {
                current += increment;
                if (current >= target) {
                    current = target;
                    clearInterval(timer);
                }
                el.textContent = Math.floor(current).toLocaleString() + suffix;
            }, 20);
        });
    }

    // Trigger number animation when stats are visible
    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateNumbers();
                statsObserver.unobserve(entry.target);
            }
        });
    });

    const statsSection = document.querySelector('.stats-bar, .hero-stats, .dashboard-grid');
    if (statsSection) statsObserver.observe(statsSection);

    // Auto dismiss alerts after 5 seconds
    document.querySelectorAll('.alert').forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            alert.style.transform = 'translateY(-10px)';
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    });

    // Quiz Timer
    const timerDisplay = document.querySelector('.timer-display');
    if (timerDisplay) {
        let timeLeft = parseInt(timerDisplay.dataset.minutes || 30) * 60;
        
        const timerInterval = setInterval(() => {
            const minutes = Math.floor(timeLeft / 60);
            const seconds = timeLeft % 60;
            timerDisplay.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
            
            if (timeLeft <= 300) {
                timerDisplay.style.color = '#fa709a';
            }
            
            if (timeLeft <= 0) {
                clearInterval(timerInterval);
                const form = document.querySelector('.quiz-form');
                if (form) form.submit();
            }
            
            timeLeft--;
        }, 1000);
    }

    // Option selection highlight
    document.querySelectorAll('.option-item').forEach(item => {
        item.addEventListener('click', function() {
            const parent = this.closest('.options-list');
            parent.querySelectorAll('.option-item').forEach(opt => {
                opt.style.borderColor = 'rgba(255, 255, 255, 0.1)';
                opt.style.background = 'rgba(255, 255, 255, 0.08)';
            });
            this.style.borderColor = '#667eea';
            this.style.background = 'rgba(102, 126, 234, 0.15)';
            const radio = this.querySelector('input[type="radio"]');
            if (radio) radio.checked = true;
        });
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // Form validation
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.style.borderColor = '#fa709a';
                    field.addEventListener('input', () => {
                        field.style.borderColor = '';
                    }, { once: true });
                }
            });
            
            if (!isValid) {
                e.preventDefault();
            }
        });
    });

    // Tooltip initialization
    document.querySelectorAll('[data-tooltip]').forEach(el => {
        el.addEventListener('mouseenter', function() {
            const tooltip = document.createElement('div');
            tooltip.className = 'tooltip-popup';
            tooltip.textContent = this.dataset.tooltip;
            tooltip.style.cssText = `
                position: absolute;
                background: rgba(15, 15, 35, 0.95);
                color: white;
                padding: 0.5rem 1rem;
                border-radius: 8px;
                font-size: 0.8rem;
                z-index: 9999;
                pointer-events: none;
                white-space: nowrap;
                border: 1px solid rgba(255,255,255,0.1);
            `;
            document.body.appendChild(tooltip);
            
            const rect = this.getBoundingClientRect();
            tooltip.style.left = rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2) + 'px';
            tooltip.style.top = rect.top - tooltip.offsetHeight - 8 + 'px';
        });
        
        el.addEventListener('mouseleave', function() {
            document.querySelectorAll('.tooltip-popup').forEach(t => t.remove());
        });
    });

    // Search functionality
    const searchInput = document.querySelector('.search-input');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const query = this.value.toLowerCase();
            const cards = document.querySelectorAll('.searchable-card');
            cards.forEach(card => {
                const text = card.textContent.toLowerCase();
                card.style.display = text.includes(query) ? '' : 'none';
            });
        });
    }

    // Chart initialization (using simple canvas for workforce data)
    const chartCanvas = document.getElementById('demandChart');
    if (chartCanvas) {
        initDemandChart(chartCanvas);
    }

    const trendCanvas = document.getElementById('trendChart');
    if (trendCanvas) {
        initTrendChart(trendCanvas);
    }
});

// Simple bar chart for workforce demand
function initDemandChart(canvas) {
    const ctx = canvas.getContext('2d');
    const width = canvas.parentElement.offsetWidth;
    const height = 300;
    canvas.width = width;
    canvas.height = height;

    const dataElements = document.querySelectorAll('.chart-data-item');
    const data = [];
    dataElements.forEach(el => {
        data.push({
            label: el.dataset.label,
            demand: parseInt(el.dataset.demand),
            supply: parseInt(el.dataset.supply),
            color: el.dataset.color
        });
    });

    if (data.length === 0) return;

    const maxVal = Math.max(...data.map(d => Math.max(d.demand, d.supply)));
    const barWidth = (width - 100) / (data.length * 3);
    const chartH = height - 60;

    // Background
    ctx.fillStyle = 'transparent';
    ctx.fillRect(0, 0, width, height);

    // Grid lines
    ctx.strokeStyle = 'rgba(255,255,255,0.05)';
    ctx.lineWidth = 1;
    for (let i = 0; i <= 5; i++) {
        const y = 30 + (chartH / 5) * i;
        ctx.beginPath();
        ctx.moveTo(50, y);
        ctx.lineTo(width - 20, y);
        ctx.stroke();
    }

    // Bars
    data.forEach((item, i) => {
        const x = 60 + i * (barWidth * 3);
        
        // Demand bar
        const demandH = (item.demand / maxVal) * chartH;
        const gradient1 = ctx.createLinearGradient(0, height - 30 - demandH, 0, height - 30);
        gradient1.addColorStop(0, '#667eea');
        gradient1.addColorStop(1, '#764ba2');
        ctx.fillStyle = gradient1;
        roundRect(ctx, x, height - 30 - demandH, barWidth, demandH, 4);
        
        // Supply bar
        const supplyH = (item.supply / maxVal) * chartH;
        const gradient2 = ctx.createLinearGradient(0, height - 30 - supplyH, 0, height - 30);
        gradient2.addColorStop(0, '#00d4aa');
        gradient2.addColorStop(1, '#43e97b');
        ctx.fillStyle = gradient2;
        roundRect(ctx, x + barWidth + 4, height - 30 - supplyH, barWidth, supplyH, 4);
        
        // Label
        ctx.fillStyle = '#a0aec0';
        ctx.font = '10px Inter';
        ctx.textAlign = 'center';
        ctx.fillText(item.label.substring(0, 8), x + barWidth, height - 10);
    });
}

// Trend chart
function initTrendChart(canvas) {
    const ctx = canvas.getContext('2d');
    const width = canvas.parentElement.offsetWidth;
    const height = 300;
    canvas.width = width;
    canvas.height = height;

    const labelsEl = document.getElementById('trendLabels');
    const demandEl = document.getElementById('trendDemand');
    const supplyEl = document.getElementById('trendSupply');
    
    if (!labelsEl) return;
    
    const labels = JSON.parse(labelsEl.textContent);
    const demand = JSON.parse(demandEl.textContent);
    const supply = JSON.parse(supplyEl.textContent);

    const maxVal = Math.max(...demand, ...supply);
    const chartW = width - 80;
    const chartH = height - 60;
    const stepX = chartW / (labels.length - 1);

    // Grid
    ctx.strokeStyle = 'rgba(255,255,255,0.05)';
    for (let i = 0; i <= 5; i++) {
        const y = 30 + (chartH / 5) * i;
        ctx.beginPath();
        ctx.moveTo(50, y);
        ctx.lineTo(width - 20, y);
        ctx.stroke();
    }

    // Demand line
    drawLine(ctx, demand, maxVal, chartH, stepX, '#667eea', '#764ba2');
    
    // Supply line
    drawLine(ctx, supply, maxVal, chartH, stepX, '#00d4aa', '#43e97b');
}

function drawLine(ctx, data, maxVal, chartH, stepX, color1, color2) {
    ctx.beginPath();
    ctx.strokeStyle = color1;
    ctx.lineWidth = 3;
    ctx.lineJoin = 'round';
    
    data.forEach((val, i) => {
        const x = 60 + i * stepX;
        const y = 30 + chartH - (val / maxVal) * chartH;
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
    });
    ctx.stroke();

    // Points
    data.forEach((val, i) => {
        const x = 60 + i * stepX;
        const y = 30 + chartH - (val / maxVal) * chartH;
        ctx.beginPath();
        ctx.arc(x, y, 4, 0, Math.PI * 2);
        ctx.fillStyle = color1;
        ctx.fill();
    });
}

function roundRect(ctx, x, y, w, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.lineTo(x + w - r, y);
    ctx.quadraticCurveTo(x + w, y, x + w, y + r);
    ctx.lineTo(x + w, y + h);
    ctx.lineTo(x, y + h);
    ctx.lineTo(x, y + r);
    ctx.quadraticCurveTo(x, y, x + r, y);
    ctx.closePath();
    ctx.fill();
}
