var navbtn = document.getElementById('nav-btn');
var sidebar = document.getElementById('side-bar');
/*
function controlnav(){

    if(navbtn.getAttribute('class') == 'activenav')
    {
        navbtn.setAttribute('class', '');
    }else{
        navbtn.setAttribute('class', 'activenav');
    }
return alert(navbtn.getAttribute('class'));
}
*/

function navcssright(){
    if(sidebar.style.right == '-40vw'){
        sidebar.style.right = '0vw';
    }else{
        sidebar.style.right = '-40vw';
    }
}

navbtn.addEventListener('click', navcssright);
