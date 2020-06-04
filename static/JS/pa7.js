
changeColorOfCard()

function changeColorOfCard() {
    let allCards = document.querySelectorAll('.show-cards')
    for (let card of allCards) {
        card.addEventListener('dblclick', (event) => {
            let getActorCount = card.dataset.actorcount
            console.log(getActorCount)
            if(parseInt(getActorCount)%2 == 1) {
                card.classList.add('odd')
            } else {
                card.classList.add('even')
            }

        })
    }
}