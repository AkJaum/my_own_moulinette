"use client"

import { useState, useEffect, useRef } from "react"

const API_URL = process.env.NEXT_PUBLIC_BACKEND_URL?.replace(/\/$/, "")

export default function Home() {
    const [results, setResults] = useState(null)
    const [lists, setLists] = useState([])
    const [selectedList, setSelectedList] = useState("list_00")
    const fileInputRef = useRef(null)

    // Carregar listas disponíveis ao montar o componente
    useEffect(() => {
        fetchLists()
    }, [])

    async function fetchLists() {
        if (!API_URL) {
            console.error("NEXT_PUBLIC_BACKEND_URL não está definida")
            return
        }

        try {
            const response = await fetch(`${API_URL}/lists`)
            if (!response.ok) {
                throw new Error(`Falha ao carregar listas (HTTP ${response.status})`)
            }

            const data = await response.json()
            setLists(data.lists || [])
        } catch (error) {
            console.error("Erro ao carregar listas:", error)
        }
    }

    async function handleUpload(event) {
        const file = event.target.files[0]
        if (!file) return

        if (!API_URL) {
            setResults({
                status: "error",
                message: "URL da API não configurada no frontend",
                exercises: []
            })
            return
        }

        const formData = new FormData()
        formData.append("file", file)
        formData.append("list_name", selectedList)

        try {
            const response = await fetch(`${API_URL}/wowlinette`, {
                method: "POST",
                body: formData
            })

            const data = await response.json().catch(() => ({}))

            if (!response.ok) {
                throw new Error(data.error || data.detail || `Falha na API (HTTP ${response.status})`)
            }

            setResults(data)
        } catch (error) {
            console.error("Erro ao enviar arquivo:", error)
            setResults({
                status: "error",
                message: error.message || "Erro ao enviar arquivo",
                exercises: []
            })
        }
    }

    function handleRefresh() {
        setResults(null)
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
                {results?.status && (
                    <div className={`status-banner ${results.status}`}>
                        <h2>{results.message}</h2>
                        {results?.passing_exercise && (
                            <p className="passing-info">Nota de corte: {results.passing_exercise}</p>
                        )}
                    </div>
                )}
                
                {(results?.exercises || []).map((r, i) => (
                    <p
                        key={i}
                        className={r.success ? "success" : r.error ? "error" : "fail"}
                    >
                        {r.error ? `❌ ${r.error}` : `${r.exercise} → ${r.success ? "✔ OK" : "✘ FAIL"}`}
                    </p>
                ))}
            </div>

            {results ? (
                <button onClick={handleRefresh} className="refresh-btn">
                    🔄 Nova Avaliação
                </button>
            ) : null}
   </div>
)}
