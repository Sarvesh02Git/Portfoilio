// portfolio/static/js/main.js
document.addEventListener('DOMContentLoaded', () => {
    // Mobile menu toggle logic (existing)
    const mobileMenu = document.getElementById('mobile-menu');
    const navLinks = document.querySelector('.navbar-nav'); // Changed to .navbar-nav for Bootstrap

    if (mobileMenu && navLinks) {
        mobileMenu.addEventListener('click', () => {
            // Bootstrap's navbar-toggler handles the collapse, but if you had custom mobile menu, this would be active
            // navLinks.classList.toggle('active');
            // mobileMenu.classList.toggle('is-active');
        });

        // Close mobile menu when a link is clicked (Bootstrap handles this with data-bs-target, but good to keep if custom)
        navLinks.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                const navbarCollapse = document.getElementById('navbarNav');
                if (navbarCollapse && navbarCollapse.classList.contains('show')) {
                    const bsCollapse = new bootstrap.Collapse(navbarCollapse, {
                        toggle: false
                    });
                    bsCollapse.hide();
                }
            });
        });
    }

    // Theme Toggle Logic (New)
    const themeToggleBtn = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement; // The <html> tag

    if (themeToggleBtn) {
        // Function to update the icon based on current theme
        function updateThemeIcon() {
            const currentTheme = htmlElement.getAttribute('data-theme');
            if (currentTheme === 'dark') {
                themeToggleBtn.innerHTML = '<i class="fas fa-sun"></i>'; // Show sun for dark mode
            } else {
                themeToggleBtn.innerHTML = '<i class="fas fa-moon"></i>'; // Show moon for light mode
            }
        }

        // Set initial icon
        updateThemeIcon();

        // Add event listener for the toggle button
        themeToggleBtn.addEventListener('click', () => {
            let currentTheme = htmlElement.getAttribute('data-theme');
            let newTheme = currentTheme === 'dark' ? 'light' : 'dark';

            htmlElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme); // Save preference

            updateThemeIcon(); // Update icon immediately
        });
    }
});
