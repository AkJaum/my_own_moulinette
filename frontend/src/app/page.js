"use client"

import { useState, useEffect, useRef } from "react"

const API_URL = process.env.NEXT_PRIVATE_BACKEND_URL || "http://localhost:8000"

export default function Home() {
    const [results, setResults] = useState([])
    const [lists, setLists] = useState([])
    const [selectedList, setSelectedList] = useState("list_00")
    const fileInputRef = useRef(null)

    // Carregar listas disponíveis ao montar o componente
    useEffect(() => {
        fetchLists()
    }, [])

    async function fetchLists() {
        try {
            const response = await fetch(`${API_URL}/lists`)
            const data = await response.json()
            setLists(data.lists || [])
        } catch (error) {
            console.error("Erro ao carregar listas:", error)
        }
    }

    async function handleUpload(event) {
        const file = event.target.files[0]
        if (!file) return

        const formData = new FormData()
        formData.append("file", file)
        formData.append("list_name", selectedList)

        try {
            const response = await fetch(`${API_URL}/wowlinette`, {
                method: "POST",
                body: formData
            })

            const data = await response.json()
            setResults(data)
        } catch (error) {
            console.error("Erro ao enviar arquivo:", error)
            setResults([{ error: "Erro ao enviar arquivo" }])
        }
    }

    function handleRefresh() {
        setResults([])
        if (fileInputRef.current) {
            fileInputRef.current.value = ""
        }
    }

    return (
        <div className="container">
            <h1>Wowlinette</h1>

            <div className="controls">
                <select value={selectedList} onChange={(e) => setSelectedList(e.target.value)}>
                    {lists.map((list) => (
                        <option key={list} value={list}>
                            {list}
                        </option>
                    ))}
                </select>

                <input 
                    type="file" 
                    accept=".zip"
                    onChange={handleUpload}
                    ref={fileInputRef}
                />
            </div>

            <div className="results">
                {results.status && (
                    <div className={`status-banner ${results.status}`}>
                        <h2>{results.message}</h2>
                        {results.passing_exercise && (
                            <p className="passing-info">Nota de corte: {results.passing_exercise}</p>
                        )}
                    </div>
                )}
                
                {results.exercises && results.exercises.map((r, i) => (
                    <p
                        key={i}
                        className={r.success ? "success" : r.error ? "error" : "fail"}
                    >
                        {r.error ? `❌ ${r.error}` : `${r.exercise} → ${r.success ? "✔ OK" : "✘ FAIL"}`}
                    </p>
                ))}
            </div>

            {results.length > 0 || results.status ? (
                <button onClick={handleRefresh} className="refresh-btn">
                    🔄 Nova Avaliação
                </button>
            ) : null}
   </div>
)}
