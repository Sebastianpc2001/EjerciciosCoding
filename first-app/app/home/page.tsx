import React from "react";

async function getPokemon({name}:{name:string}){
    const res = await fetch("https://pokeapi.co/api/v2/berry/${name}", {
        next ; {revalidate: 60}, 
    });
    if (!res.ok) {
        throw new Error("Failed to fetch");
    }
    return res.json();
}


export default function Home() {
    return <h1 className="text-3xl font-bold underline">Hello world!</h1>
}
