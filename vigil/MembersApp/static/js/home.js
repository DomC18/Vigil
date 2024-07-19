const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry)
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        }
    });
})

const hiddenElements = document.querySelectorAll('.hidden');
const hiddenLeftElements = document.querySelectorAll('.hidden-left');
const hiddenRightElements = document.querySelectorAll('.hidden-right');
const hiddenUpElements = document.querySelectorAll('.hidden-up');
const hiddenDownElements = document.querySelectorAll('.hidden-down');
const fadeInElements = document.querySelectorAll('.fade-in');
hiddenElements.forEach((element) => observer.observe(element));
hiddenLeftElements.forEach((element) => observer.observe(element));
hiddenRightElements.forEach((element) => observer.observe(element));
hiddenUpElements.forEach((element) => observer.observe(element));
hiddenDownElements.forEach((element) => observer.observe(element));
fadeInElements.forEach((element) => observer.observe(element));