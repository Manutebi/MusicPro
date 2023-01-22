var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i <updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productoId = this.dataset.producto
        var action = this.dataset.action
        console.log('productoId:', productoId, 'action:', action )
    
        console.log('USER', user)
        if(user == 'AnonymousUser'){
            console.log('No ha iniciado sesion')
        }else{
            updateUserOrder(productoId, action)
        }
    })
}

function updateUserOrder(productoId, action){
    console.log('Usuario en sesion, enviando datos...')
    var url = '/update_item/'
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body: JSON.stringify({
            'productoId': productoId, 
            'action': action
        })
    })

    .then((response) => {
        if (!response.ok) {
            // error processing
            throw 'Error';
        }
        return response.json()
    })
    .then((data) =>{
        console.log('data:', data)
    })

}