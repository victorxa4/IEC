document.querySelector('#form').addEventListener('submit', async e => {
    await e.preventDefault()

    const formData = await new FormData(document.querySelector('#form'))

    const fetchOptions = {
        method: 'POST',
        body: formData
    }

    const response = await fetch('http://127.0.0.1:8000/api/read_img/', fetchOptions).then(async response => await response.json()).then(data =>{
        document.querySelector("#textarea").innerHTML = data.result
        document.querySelector("#textarea").style.background = 'rgba(128, 154, 240, 0.5)'
    })
})

document.querySelector('#choose-file').addEventListener('click', e => {
    document.querySelector('#image').click()
})

document.querySelector('#image').addEventListener('input', e =>{
    document.querySelector('#selected-file').innerHTML = document.getElementById('image').value
})

document.querySelector('#textarea').addEventListener('click', e => {
    e.target.style.background = 'rgba(90, 109, 170, 0.5)'
})