function operaciones()
{
    let n1,n2,tipoope, respuesta;
    n1=parseInt(document.getElementById("n1").value);
    n2=parseInt(document.getElementById("n2").value);
    tipoope=document.getElementById("tipo").value;
    
    if (isNumber(n1) && isNumber(n2))
    {
       switch(tipoope)
    {
        case "+":ope=n1+n2;break;
        case "-":ope=n1-n2;break;
        case "*":ope=n1*n2;break;
        case "/":ope=n1/n2;break;
        
    }
    
    respuesta=document.getElementById("resultado").innerHTML=`<h2>${n1} ${tipoope} ${n2} = ${ope}</h2>`
    }
    else
        respuesta=document.getElementById("resultado").innerHTML=`<h2>Ingresa numeros porfavor...</h2>`
        alert('Ingresa numeros porfavor...');
    
}

function isNumber(n)
{
    return !isNaN(parseInt(n) && isFinite(n));
}