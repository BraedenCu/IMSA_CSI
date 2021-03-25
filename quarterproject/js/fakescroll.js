function smoothScroll(classId){
    document.querySelector(classId).scrollIntoView({
        behavior: 'smooth'
    });
    document.getElementById("pagetwo").style.opacity = 100;
    document.getElementById("pagetwo").style.pointerEvents = 'auto';
}