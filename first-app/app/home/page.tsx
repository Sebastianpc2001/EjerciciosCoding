"use client";

import React from 'react';
import {useState} from "react"


interface Pokemon {
    id: number;
    name: string;
    height: number;
    weight: number;}


async function getPokemon({name}:{name:string}){
    const res = await fetch('https://pokeapi.co/api/v2/${name}', {
        next : {revalidate: 60}, 
    });
    if (!res.ok) {
        throw new Error('Failed to fetch');
    }
    return res.json();
}

export default function Home() {
    const [pokemonName1, setPokemonName1] = useState("");
    const [pokemon, setPokemon] = useState<Pokemon | null>(null);
    const [pokemonName2, setPokemonName2] = useState("");
    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        console.log("Summited the pokemon",pokemonName1);
        console.log(pokemon)
    const response =  await fetch(
        `https://pokeapi.co/api/v2/pokemon/${pokemonName1.toLowerCase()}`
    );
  
    if (!response.ok) {
        throw new Error("Pokémon not found");
    }
    const data = await response.json();
    setPokemon(data);
    }
    return (
        <div>
            <h1 className="text-3xl font-bold underline">Hello Pokemon Fan!</h1>
            <form onSubmit={handleSubmit}>
                <input value={pokemonName1} type="text" placeholder="Enter your pokemon" id="Pokemon" onChange={e=>setPokemonName1(e.target.value)}/>
                <button type="submit" className="p-4 bg-blue-500 text-white rounded">Submit</button>
            </form>
         </div>
        );
}




