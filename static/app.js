// app.js
// - Handles theme toggle
// - Personalized greeting on Home using /api/profile
// - Small page transition nicety

// Theme toggle (dark / light)
const body = document.body;
const toggleBtn = document.getElementById('theme-toggle');
if (toggleBtn) {
  // Restore last choice
  const saved = localStorage.getItem('yalla-theme');
  if (saved === 'dark') body.classList.add('dark');
  toggleBtn.textContent = body.classList.contains('dark') ? '☀️' : '🌙';

  toggleBtn.addEventListener('click', () => {
    body.classList.toggle('dark');
    const mode = body.classList.contains('dark') ? 'dark' : 'light';
    localStorage.setItem('yalla-theme', mode);
    toggleBtn.textContent = mode === 'dark' ? '☀️' : '🌙';
  });
}

// Personalized greeting (Home page)
async function loadGreeting() {
  const el = document.getElementById('greeting');
  if (!el) return;
  try {
    const res = await fetch('/api/profile');
    const user = await res.json();
    el.textContent = `Welcome back, ${user.name}! Ready to plan your day?`;
  } catch(e) {
    // silently ignore
  }
}
loadGreeting();

// Page fade animation when clicking any navbar link
document.querySelectorAll('.tabs a').forEach(a=>{
  a.addEventListener('click', ()=>{
    const container = document.querySelector('.page-fade');
    if (!container) return;
    container.classList.remove('page-fade');
    void document.body.offsetWidth; // reflow
    container.classList.add('page-fade');
  });
});
