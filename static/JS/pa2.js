function selectCard() {
    let allCards = document.querySelectorAll('.rating-card')
    let sumOfSelected = 0
    let selectedCardsNum = 0
    for (let card of allCards) {
        card.addEventListener('click', (event) => {
            if (card.classList.contains('select')) {
                card.classList.remove('select')
            } else {
                card.classList.add('select')
                let ratingOfCard = card.dataset.rating
                sumOfSelected += parseFloat(ratingOfCard)
                selectedCardsNum += 1
                let averageRating = sumOfSelected / selectedCardsNum
                let averageBox = document.getElementById('average')
                averageBox.innerHTML = averageRating.toFixed(2)

            }


        })
    }
}

selectCard();