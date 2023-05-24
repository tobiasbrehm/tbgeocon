let NavbarBtn;
let btnIcon;
let navLinks;

function init(){
    openTap('mining');
    NavbarBtn = document.getElementById('navbar-btn');
    btnIcon = document.getElementById('btn-icon');
    navLinks = document.getElementById('nav');
}


function toggleNavbar() {
    btnIcon.classList.toggle('openNav');
    navLinks.classList.toggle('openNav');
}


function remove_slider_classes(){
    document.getElementById('slider').classList.remove('slider-one');
    document.getElementById('slider').classList.remove('slider-two');
    document.getElementById('slider').classList.remove('slider-three');
    document.getElementById('slider').classList.remove('slider-four');
}


function animateSlider(tab){
    remove_slider_classes();
    switch (tab) {
        case 'mining':
            document.getElementById('slider').classList.add('slider-one');
            break;

        case 'polar':
            document.getElementById('slider').classList.add('slider-two');
            break; 
            
        case 'photo':
            document.getElementById('slider').classList.add('slider-three');
            break;  

        case 'translations':
            document.getElementById('slider').classList.add('slider-four'); 
            break;

        default:
            break;
    }
}


function checkedButtonStyle(tab){
    var i;
    let tabs = document.getElementsByClassName("tab");
    for (i = 0; i < tabs.length; i++) {
        tabs[i].classList.remove('checked');
    }
    document.getElementById(tab).classList.add('checked');
}


function showSectionContent(tab){
    var i;
    let section = document.getElementsByClassName("section");
    for (i = 0; i < section.length; i++) {
        section[i].style.display = 'none';
    }
    document.getElementById('section_' + tab).style.display = 'block';
}

function openTap(tab){
    checkedButtonStyle(tab);
    animateSlider(tab);
    showSectionContent(tab);
}

function openPopup(popup){
    id = 'popup-'+ popup;
    document.getElementById(id).classList.remove('hidden');
    document.getElementById('body').classList.add('no-scroll');
}

function closePopup(){
    document.getElementById('popup-dataprotection').classList.add('hidden');
    document.getElementById('popup-impressum').classList.add('hidden');
    document.getElementById('body').classList.remove('no-scroll');
}