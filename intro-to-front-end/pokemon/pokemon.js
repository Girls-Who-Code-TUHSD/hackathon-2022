// TODO: request list of pokemon from API
const apiURL = 'https://pokeapi.co/api/v2/pokemon?limit=20/'

const getPokemon = fetch(apiURL)

getPokemon.then(response => {
  response.json().then(pokemons => {
    pokemons.results.forEach(pokemon => {
      // TODO: go through list of pokemon, adding each one to the DOM
      // Make a link element
      const link = document.createElement('a')
      // add text to be displayed for this link
      link.innerText = pokemon.name
      // add URL that link points to
      link.href = pokemon.url

      const node = document.createElement('div')
      node.appendChild(link)

      // add the elements we just made to the document
      const mainDiv = document.getElementById('pokemons')
      mainDiv.appendChild(node)
    })
  })
})
