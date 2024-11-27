function addition() {
	// ci-dessous récupération de la donnée saisie dans le formulaire
	var input1 = document.forms["mon_formulaire"].elements["saisie"].value;
	var input2 = document.forms["mon_formulaire"].elements["saisie2"].value;
	
	
	// ci-dessous récupération de l'objet de la page web
	var toto = document.getElementById("copie");
	
	// ci-dessous mise ? jour du contenu de l'objet de la page web
	toto.innerHTML = input1*1+input2*1;
	
	
}
function soustraction() {
	// ci-dessous récupération de la donnée saisie dans le formulaire
	var input1 = document.forms["mon_formulaire"].elements["saisie"].value;
	var input2 = document.forms["mon_formulaire"].elements["saisie2"].value;
	
	
	// ci-dessous récupération de l'objet de la page web
	var toto = document.getElementById("copie");
	
	// ci-dessous mise ? jour du contenu de l'objet de la page web
	toto.innerHTML = input1*1-input2*1;
	
	
}
function multiplication() {
	// ci-dessous récupération de la donnée saisie dans le formulaire
	var input1 = document.forms["mon_formulaire"].elements["saisie"].value;
	var input2 = document.forms["mon_formulaire"].elements["saisie2"].value;
	
	
	// ci-dessous récupération de l'objet de la page web
	var toto = document.getElementById("copie");
	
	// ci-dessous mise ? jour du contenu de l'objet de la page web
	toto.innerHTML = input1*input2;
	
	
}
function division() {
	// ci-dessous récupération de la donnée saisie dans le formulaire
	var input1 = document.forms["mon_formulaire"].elements["saisie"].value;
	var input2 = document.forms["mon_formulaire"].elements["saisie2"].value;
	
	
	// ci-dessous récupération de l'objet de la page web
	var toto = document.getElementById("copie");
	
	// ci-dessous mise ? jour du contenu de l'objet de la page web
	toto.innerHTML = input1/input2;
	
	
}
