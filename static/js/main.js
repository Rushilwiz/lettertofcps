function selectAll() {
     var myForm = document.forms['form'];
     for( var i=0; i < myForm.length; i++ ) { 
        myForm.elements[i].checked = "checked";
     }
    $('html, body').animate({
        scrollTop: $("#div1").offset().top
    }, 1000);
}

function toggle() {
	document.getElementById("who").classList.toggle("hide");
}

function copyLetter() {
	document.getElementById('copyLetterButton').innerHTML = "Copied!";
}

function copySecond() {
	document.getElementById('copyLetterButtonSecond').innerHTML = "Copied!";
}

function copyList() {
	document.getElementById('copyList').innerHTML = "Copied!";
}

var clipboard = new ClipboardJS('.btn');
