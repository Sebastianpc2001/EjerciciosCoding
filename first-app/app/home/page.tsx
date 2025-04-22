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
    return (
        <div>
            <h1 className="text-3xl font-bold underline">Hello world!</h1>
            <button className="p-4 bg-blue-500 text-white rounded">Summit</button>
         </div>
    );
}

