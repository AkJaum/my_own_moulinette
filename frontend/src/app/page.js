"use client"

import { useState } from "react"

export default function Home()
{
    const [results, setResults] = useState([])

    async function handleUpload(event)
    {
        const file = event.target.files[0]

        const formData = new FormData()
        formData.append("file", file)

        const response = await fetch("http://localhost:8000/wowlinette", {
            method: "POST",
            body: formData
        })

        const data = await response.json()
        setResults(data)
    }

    return (
        <div className="container">
            <h1>Moulinette C00</h1>

            <input type="file" onChange={handleUpload} />

            <div className="results">
                {results.map((r, i) => (
                    <p
                        key={i}
                        className={r.success ? "success" : "fail"}
                    >
                        {r.exercise} → {r.success ? "✔ OK" : "✘ FAIL"}
                    </p>
                ))}
            </div>
        </div>
    )
}
