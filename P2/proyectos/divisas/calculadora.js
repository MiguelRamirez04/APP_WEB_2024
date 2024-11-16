// Tasas de conversión predefinidas
const tasasConversion = {
    "+": 18.00,
    "-": 0.055,
    "*": 0.90,
    "/": 1.11
};

function mostrarIcono() {
    const tipo = document.getElementById("tipo").value;
    const imagenMoneda = document.getElementById("imagenMoneda");

    switch (tipo) {
        case "+":
            imagenMoneda.src = "peso.jpg";
            imagenMoneda.alt = "Dólares a Pesos";
            break;
        case "-":
            imagenMoneda.src = "dolar.jpg";
            imagenMoneda.alt = "Pesos a Dólares";
            break;
        case "*":
            imagenMoneda.src = "euro.jpg";
            imagenMoneda.alt = "Dólares a Euros";
            break;
        case "/":
            imagenMoneda.src = "dolar.jpg";
            imagenMoneda.alt = "Euros a Dólares";
            break;
    }

    imagenMoneda.style.display = "inline";
}

function operaciones() {
    let n1, tipo, tasaConversion, resultadoOperacion;
    
    n1 = parseFloat(document.getElementById("n1").value);
    tipo = document.getElementById("tipo").value;

    tasaConversion = tasasConversion[tipo];

    if (isNumber(n1) && tasaConversion) {
        resultadoOperacion = n1 * tasaConversion;

        let simbolo = "";

        switch (tipo) {
            case "+":
                simbolo = "MX$"; break;
            case "-":
                simbolo = "$"; break;
            case "*":
                simbolo = "€"; break;
            case "/":
                simbolo = "$"; break;
        }

        document.getElementById("resultado").innerHTML = `<h2>${simbolo} ${resultadoOperacion.toFixed(2)}</h2>`;
    } else {
        document.getElementById("resultado").innerHTML = `<h2>Ingresa una cantidad válida</h2>`;
        alert('Ingresa una cantidad válida');
    }
}

function isNumber(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
}
