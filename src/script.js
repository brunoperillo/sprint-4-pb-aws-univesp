import { pesquisaImagem } from url;
const images = pesquisaImagem(UZkWB8GmlHAfcVjn0ps0b24t0f5bf6xATzDfvlff7IywJYQX0DM37KDu);
images.photos.show({id:id.table_name}).then(nome.table_name = {nameImage});

const textInput = document.getElementById('text-input');
const countButton = document.getElementById('nameImage');
const result = document.getElementById('result');

const pesquisaImagem = async() => {
    const textInput = textInput.value;
    const nameImage = document.getElementById('nameImage').value;
    const url = `https://api.pexels.com/v1/search/${nameImage}/json/`;
    const dados = await fetch(url);
    const result = await dados.json();   
    result.textContent = `The text contains ${nameImage} letters.`;
}

document.getElementById('nameImage')
document.addEventListener('click', pesquisaImagem);