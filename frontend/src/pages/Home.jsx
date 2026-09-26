import { useEffect, useState } from 'react'

import { getHealth } from '../api/client'

function Home() {
  const [apiStatus, setApiStatus] = useState('Checking API...')

  useEffect(() => {
    getHealth()
      .then(() => {
        setApiStatus('API connected')
      })
      .catch(() => {
        setApiStatus('API unavailable')
      })
  }, [])

  return (
    <main className="min-h-screen p-8">
      <h1 className="text-4xl font-bold">PrivateResume</h1>

      <p className="mt-2 text-gray-600">
        AI-powered resume tailoring workspace.
      </p>

      <p className="mt-6">
        Backend status: <strong>{apiStatus}</strong>
      </p>
    </main>
  )
}

export default Home