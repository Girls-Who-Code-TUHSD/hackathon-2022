const mainDiv = document.getElementById('pokemons')

// https://developer.mozilla.org/en-US/docs/Web/API/fetch
const fetchPokemon = fetch('https://pokeapi.co/api/v2/pokemon?limit=20/')

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then
fetchPokemon.then(res => {
  // https://developer.mozilla.org/en-US/docs/Web/API/Response/json
  res.json().then(pokemons => {
    pokemons.results.forEach(pokemon => {
      const link = document.createElement('a')
      link.innerText = pokemon.name
      link.href = pokemon.url

      const node = document.createElement('p')
      node.appendChild(link)

      mainDiv.appendChild(node)
    })
  })
})

// TODO: when link is clicked, fetch results at URL and add to DOM.
