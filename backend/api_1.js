async function getAnimes() {
    let res = await fetch('http://localhost:5555/api/anime')
    let json = await res.json();
    let anime_vm = Object.values(json)
        .map(ani => (
        {
            Name: ani.Name,
            anime_id: ani.anime_id,
            selected: false,
            rating: 6
        }
     ))
    
    return anime_vm
}

async function getRecommendations(animes, strategy) {
    if (animes.length === 0) {
        return []
    }

    let req_url = `http://localhost:5555/api/recommendations`;
    let req_headers = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({animes: animes, strategy: strategy})
     }
    
    let resp = await fetch(req_url, req_headers)
    let recommendations = await resp.json();
    let rec_vm = recommendations.map(r => (
        {
            Name: r.Name
        }
     ));
    
    return rec_vm
}

export { getAnimes, getRecommendations };