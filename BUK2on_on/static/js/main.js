let whoweare = document.querySelector(".whoweare");

window.addEventListener('scroll', function() {
    let value = window.scrollY
    console.log("scrollY", value);


    if(value>300){
        whoweare.style.animation='disappear 1s ease-out forwards';
    }else{
        whoweare.style.animation='slide 1s ease-out'
    }
});



