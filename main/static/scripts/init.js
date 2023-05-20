
function openTap(tab){
    console.log('test')
    var i;
    let tabs = document.getElementsByClassName("tab");
    for (i = 0; i < tabs.length; i++) {
        tabs[i].classList.remove('checked');
    }

    document.getElementById(tab).classList.add('checked');

}