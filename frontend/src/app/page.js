"use client"

import { useState, useEffect, useRef } from "react"

const API_URL = process.env.NEXT_PUBLIC_BACKEND_URL?.replace(/\/$/, "")

export default function Home() {
    const [results, setResults] = useState(null)
    const [lists, setLists] = useState([])
    const [selectedList, setSelectedList] = useState("list_00")
    const [loading, setLoading] = useState(false)
    const [fileName, setFileName] = useState("Upload")
    const [showModal, setShowModal] = useState(false)
    const [showInfoModal, setShowInfoModal] = useState(false)
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

        setFileName(file.name)

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
            setLoading(true)
            setResults(null)
            setShowModal(true)
            
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
        } finally {
            setLoading(false)
        }
    }

    function handleRefresh() {
        setResults(null)
        setFileName("Upload")
        setShowModal(false)
        if (fileInputRef.current) {
            fileInputRef.current.value = ""
        }
    }

    function handleButtonClick() {
        fileInputRef.current?.click()
    }

    return (
        <div className="container">
            <div className="info-header">
                <img
                    src="/info.png"
                    alt="Info"
                    className="info"
                    onClick={() => setShowInfoModal(true)}
                    style={{ cursor: "pointer" }}>
                </img>
            </div>
            <img 
                src="/wow_logo.png" 
                alt="Wowlinette" 
                className="logo">
            </img>

            <div className="controls">
                <div>
                    <p>Selecione a lista a ser avaliada</p>
                    <select value={selectedList} onChange={(e) => setSelectedList(e.target.value)}>
                        {lists.map((list) => (
                            <option key={list} value={list}>
                                {list}
                            </option>
                        ))}
                    </select>
                </div>

                <button onClick={handleButtonClick} className="file-btn">
                    {fileName}
                </button>
                <input 
                    type="file" 
                    accept=".zip"
                    onChange={handleUpload}
                    ref={fileInputRef}
                    style={{ display: "none" }}
                />
            </div>

            {showInfoModal && (
                <div className="modal-overlay" onClick={() => setShowInfoModal(false)}>
                    <div className="modal-content info-modal" onClick={(e) => e.stopPropagation()}>
                        <h2>ℹ️ Sobre o Wowlinette</h2>
                        <div className="info-content">
                            <p>
                                <strong>Wowlinette</strong> é uma ferramenta automatizada para avaliação de exercícios de programação em C.
                            </p>
                            <h3>Como usar:</h3>
                            <ol>
                                <li>Selecione a lista de exercícios que deseja avaliar</li>
                                <li>Clique no botão "Upload" e selecione o arquivo .zip com seus exercícios</li>
                                <li>Aguarde a avaliação automática</li>
                                <li>Veja o resultado de cada exercício</li>
                            </ol>
                            <h3>Formato do arquivo:</h3>
                            <p>
                                O arquivo .zip deve conter uma pasta com nome no formato <code>c00</code>, <code>c01</code>, etc., 
                                contendo subpastas <code>ex00</code>, <code>ex01</code>, etc., com os arquivos .c dos exercícios.
                            </p>
                            <h3>Resultado:</h3>
                            <p>
                                Cada exercício será marcado como ✔ <span className="success">OK</span> ou 
                                ✘ <span className="fail">FAIL</span> baseado na correção automática.
                            </p>
                            <h3>Projeto feito por AkJaum</h3>
                            <div className="info-labels">
                                <a href="https://github.com/AkJaum">
                                    <img src="https://cdn-icons-png.flaticon.com/256/25/25231.png" className="label"></img>
                                </a>
                                <a href="https://www.linkedin.com/in/akjaum/" target="_blank">
                                    <img src="https://static.vecteezy.com/system/resources/previews/023/986/970/non_2x/linkedin-logo-linkedin-logo-transparent-linkedin-icon-transparent-free-free-png.png" className="label-link"></img>
                                </a>
                            </div>                        
                        </div>
                        <button onClick={() => setShowInfoModal(false)} className="modal-close-btn">
                            ✕ Fechar
                        </button>
                    </div>
                </div>
            )}

            {showModal && (
                <div className="modal-overlay" onClick={handleRefresh}>
                    <div className="modal-content" onClick={(e) => e.stopPropagation()}>
                        {loading && (
                            <div className="loading">
                                <p>⏳ Avaliando seu código...</p>
                            </div>
                        )}
                        
                        {!loading && results?.status && (
                            <>
                                <div className={`status-banner ${results.status}`}>
                                    <h2>{results.message}</h2>
                                    {results?.passing_exercise && (
                                        <p className="passing-info">Nota de corte: {results.passing_exercise}</p>
                                    )}
                                </div>
                                
                                {(results?.exercises || []).map((r, i) => (
                                    <p
                                        key={i}
                                        className={r.success ? "success" : r.error ? "error" : "fail"}
                                    >
                                        {r.error ? `❌ ${r.error}` : `${r.exercise} → ${r.success ? "✔ OK" : "✘ FAIL"}`}
                                    </p>
                                ))}
                                
                                <button onClick={handleRefresh} className="modal-close-btn">
                                    ✕ Fechar
                                </button>
                            </>
                        )}
                    </div>
                </div>
            )}

            <div className="results">
                {!showModal && !loading && results?.status && (
                    <div className={`status-banner ${results.status}`}>
                        <h2>{results.message}</h2>
                        {results?.passing_exercise && (
                            <p className="passing-info">Nota de corte: {results.passing_exercise}</p>
                        )}
                    </div>
                )}

                
                {!showModal && !loading && (results?.exercises || []).map((r, i) => (
                    <div className="results-item" key={i}>
                        <p
                            key={i}
                            className={r.success ? "success" : r.error ? "error" : "fail"}
                        >
                            {r.error ? `❌ ${r.error}` : `${r.exercise} → ${r.success ? "✔ OK" : "✘ FAIL"}`}
                        </p>
                    </div>
                ))}
            </div>

            {results && !loading && !showModal ? (
                <button onClick={handleRefresh} className="refresh-btn">
                    🔄 Nova Avaliação
                </button>
            ) : null}
        </div>
    )
}
