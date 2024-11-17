document.getElementById('download-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const url = document.getElementById('url').value;
    const formatChoice = document.getElementById('format').value;
    const outputFolder = document.getElementById('output-folder').value;

    fetch('http://127.0.0.1:5000/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            url: url,
            format_choice: formatChoice,
            output_folder: outputFolder
        })
    })
        .then(response => response.json())
        .then(data => {
            const resultado = document.getElementById('resultado');
            if (data.message) {
                resultado.innerHTML = `<p>${data.message}</p>`;
            } else if (data.error) {
                resultado.innerHTML = `<p style="color: red;">${data.error}</p>`;
            }
        })
        .catch(error => {
            const resultado = document.getElementById('resultado');
            resultado.innerHTML = `<p style="color: red;">Erro ao se conectar ao servidor: ${error}</p>`;
        });
});
