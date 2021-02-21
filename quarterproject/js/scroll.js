
const pageone = document.getElementById("pageone");
const pagetwo = document.getElementById("pagetwo");
const scrollCount = 0;

function opacity() {
  pageone.style.opacity = '10%';
}

pageone.addEventListener('wheel', opacity);
