let team = [];

document.addEventListener("DOMContentLoaded", () => {
    const searchButton = document.getElementById("search-button");
    const searchBox = document.getElementById("search-box");

    searchButton.addEventListener("click", () => {
        const searchTerm = searchBox.value.trim();
        if (searchTerm) {
            fetchAndDisplayPokemon(searchTerm);
        }
    });

    document.getElementById("clear-team").addEventListener("click", () => {
        team = [];
        updateTeamDisplay();
    });
});

function fetchAndDisplayPokemon(pokemonName) {
    const pokemonDisplay = document.getElementById("pokemon-display");
    pokemonDisplay.innerHTML = ''; // Clear previous results

    fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName.toLowerCase()}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Pokémon not found');
            }
            return response.json();
        })
        .then(data => {
            displayPokemon(data);
        })
        .catch(error => {
            pokemonDisplay.innerHTML = `<p class="error-message">${error.message}</p>`;
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
            <button onclick="addToTeam('${pokemon.name}', '${pokemon.sprites.front_default}')">Add to Team</button>
        </div>
    `;
}


// Change to Python
function addToTeam(pokemonName, imageUrl) {
    if (team.length < 6 && !team.some(member => member.name === pokemonName)) {
        team.push({ name: pokemonName, image: imageUrl });
        updateTeamDisplay();
    } else {
        alert("Your team is already full or the Pokémon is already in your team.");
    }
}

// Change to python
function updateTeamDisplay() {
    const teamDisplay = document.getElementById("pokemon-team");
    teamDisplay.innerHTML = team.map(member => `
        <div class="team-member-card">
            <img src="${member.image}" alt="${member.name}" class="team-member-image"/>
            <p>${member.name}</p>
        </div>
    `).join('');
}