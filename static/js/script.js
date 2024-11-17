document.getElementById('download-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const url = document.getElementById('url').value;
    const formatChoice = document.getElementById('format').value;
    const outputFolder = document.getElementById('output-folder').value;

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value; // Pega o token CSRF

    console.log('Dados enviados:', { url, formatChoice, outputFolder }); // Log dos dados enviados

    fetch('/download/video/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken // Inclui o token CSRF no cabeçalho
        },
        body: JSON.stringify({
            url: url,
            format: formatChoice,
            output_folder: outputFolder
        })
    })
        .then(response => {
            if (!response.ok) {
                return response.json().then(errorData => {
                    throw new Error(`Erro do servidor: ${response.status} - ${errorData.message || 'Erro desconhecido'}`);
                });
            }
            return response.json();
        })
        .then(data => {
            const resultado = document.getElementById('resultado');
            if (data.status === 'success') {
                resultado.innerHTML = `<p style="color: green;">${data.message}</p>`;
            } else {
                resultado.innerHTML = `<p style="color: red;">${data.message}</p>`;
            }
        })
        .catch(error => {
            const resultado = document.getElementById('resultado');
            resultado.innerHTML = `<p style="color: red;">Erro: ${error.message}</p>`;
            console.error("Erro na requisição:", error);
        });
});
