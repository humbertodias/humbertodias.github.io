// onload listener
window.onload = onload;
document.addEventListener("DOMContentLoaded", onload);

function onload(){
  lastModified();
}

function lastModified(){
	var date = new Date(document.lastModified);
	document.getElementById('lastModified').innerHTML = date;
}