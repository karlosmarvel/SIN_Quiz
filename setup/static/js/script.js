document.addEventListener('DOMContentLoaded', function() {
    const respostaContainer = document.getElementById('resposta-container');
    const respostaBotao = document.getElementById('resposta-botao');
    const radios = Array.from(document.querySelectorAll('input[name="resposta"]'));
    const respostaCorreta = respostaContainer.dataset.respostaCorreta;

    respostaContainer.addEventListener('click', function() {
        const respostaSelecionada = radios.find(radio => radio.checked)?.value;

        if (respostaSelecionada) {
            if (respostaSelecionada === respostaCorreta) {
                respostaBotao.textContent = 'Resposta correta!';
                const radioButtonSelecionado = document.querySelector(`input[name="resposta"][value="${respostaSelecionada}"]`);
                if (radioButtonSelecionado) {
                    radioButtonSelecionado.parentElement.style.backgroundColor = 'lightgreen';
                }
            } else {
                respostaBotao.textContent = `Resposta errada! Resposta correta: ${respostaCorreta}`;
                const radioButtonSelecionado = document.querySelector(`input[name="resposta"][value="${respostaSelecionada}"]`);
                if (radioButtonSelecionado) {
                    radioButtonSelecionado.parentElement.style.backgroundColor = 'red';
                }
                const radioButtonCorreto = document.querySelector(`input[name="resposta"][value="${respostaCorreta}"]`);
                if (radioButtonCorreto) {
                    radioButtonCorreto.parentElement.style.backgroundColor = 'lightgreen';
                }
            }
        } else {
            respostaBotao.textContent = 'Nenhuma resposta selecionada.';
        }
    });

    const imagemContainer = document.getElementById('imagem-container');
    imagemContainer.addEventListener('click', function() {
        location.reload(); // Recarrega a página ao clicar na imagem
    });
});