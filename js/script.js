document.addEventListener("DOMContentLoaded", () => {
    const searchButton = document.getElementById("search-button");
    const searchBox = document.getElementById("search-box");

    searchButton.addEventListener("click", () => {
        const searchTerm = searchBox.value.trim(); // Trim whitespace from the search term
        if (searchTerm) {
            searchPokemon(searchTerm);
        }
    });
});

function searchPokemon(searchTerm) {
    const pokemonDisplay = document.getElementById("pokemon-display");
    pokemonDisplay.innerHTML = ''; // Clear previous results

    fetch(`https://pokeapi.co/api/v2/pokemon/${searchTerm.toLowerCase()}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Pokémon not found'); // Throw an error if response is not OK
            }
            return response.json();
        })
        .then(data => {
            displayPokemon(data);
        })
        .catch(error => {
            pokemonDisplay.innerHTML = `<p class="error-message">${error.message}</p>`; // Display error message
        });
}

function displayPokemon(pokemon) {
    const pokemonDisplay = document.getElementById("pokemon-display");
    pokemonDisplay.innerHTML = `
        <div class="pokemon-card">
            <img src="${pokemon.sprites.front_default}" alt="${pokemon.name}" class="pokemon-image"/>
            <h2>${pokemon.name}</h2>
            <p>Attack: ${pokemon.stats[1].base_stat}</p>
            <p>Defense: ${pokemon.stats[2].base_stat}</p>
            <!-- Add more details as needed -->
        </div>
    `;
}
