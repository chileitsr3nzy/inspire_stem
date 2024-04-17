const imgs = document.querySelectorAll('.header-slider ul img');
const prev_btn = document.querySelector('.control_prev');
const next_btn = document.querySelector('.control_next');
 
let n = 2;
 
function changeSlide(){
    for (let i = 0; i < imgs.length; i++) {
        imgs[i].style.display = 'none'; //selecting all images in the class making them hidden
    }
    imgs[n].style.display = 'block'; //based on the index of the image it is made visible
}
changeSlide();

prev_btn.addEventListener('click', (e)=>{
    if (n>0) {
        n--;
    }else {
        n = imgs.length - 1;
    }
    changeSlide();
})
next_btn.addEventListener('click', (e)=>{
    if (n < imgs.length - 1) {
        n++;
    }else {
        n = 0;
    }
    changeSlide();
})

const scrollContainer = document.querySelectorAll('.products');
for (const item of scrollContainer) {
    item.addEventListener('wheel',(evt)=>{
        evt.preventDefault();
        item.scrollLeft += evt.deltaY ;

    });


}
