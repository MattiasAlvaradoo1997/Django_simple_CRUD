(function(){
    const btnElinimacion=document.querySelectorAll(".btnEliminacion");

    btnElinimacion.forEach(btn => {
        btn.addEventListener('click', (e)=>{
            const confirmacion = confirm('¿Está seguro?');
            if(!confirmacion){
                e.preventDefault();
            }
        })
    })
})();