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
    
    respuesta=document.getElementById("resultado").innerHTML=`<h3>${n1} ${tipoope} ${n2} = ${ope}</h3>`
    }
    else
        alert('Ingresa numeros porfavor...');
    
}

function isNumber(n)
{
    return !isNaN(parseInt(n) && isFinite(n));
}