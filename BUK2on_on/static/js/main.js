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


const modal = document.getElementById("modal_detail_feed");
const buttonAddFeed = document.getElementById("detail_feed");
const buttonCloseModal = document.querySelector("#close_modal");

buttonAddFeed.addEventListener("click", e => {
    modal.style.top = window.pageYOffset + 'px';
    modal.style.display = "flex";
    document.body.style.overflowY = "hidden"; 
});



buttonCloseModal.addEventListener("click", e => {
    modal.style.display = "none";
    document.body.style.overflowY = "visible";
});





