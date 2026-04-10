import Link from 'next/link'

export default function ManifestoPage() {
  const axioms = [
    { id: 'I', name: 'Suprematia Humana', desc: 'Human supremacy and kill-switch mechanisms' },
    { id: 'II', name: 'Identitas Agentica', desc: 'Agent identity and traceability' },
    { id: 'III', name: 'Responsabilitas', desc: 'Responsibility attribution' },
    { id: 'IV', name: 'Circulus Clausus', desc: 'Closed-loop supervision' },
    { id: 'V', name: 'Interoperabilitas', desc: 'Interoperability standards' },
    { id: 'VI', name: 'Auditum Immutabile', desc: 'Immutable audit trails' },
    { id: 'VII', name: 'Adaptatio Localis', desc: 'Local adaptation' },
    { id: 'VIII', name: 'Ethica Programmata', desc: 'Programmed ethics' },
    { id: 'IX', name: 'Gubernatio Hybrida', desc: 'Hybrid governance' },
    { id: 'X', name: 'Energia Sustinenda', desc: 'Energy sovereignty' },
    { id: 'XI', name: 'Arma Prohibita', desc: 'Autonomous weapons prohibition' },
    { id: 'XII', name: 'Cognitio Limita', desc: 'Cognitive frontier' },
    { id: 'XIII', name: 'Risicum Existentiale', desc: 'Existential risks' },
    { id: 'XIV', name: 'Iustitia Mundana', desc: 'Geoeconomic justice' },
    { id: 'XV', name: 'Resilientia Systematica', desc: 'Technological resilience' },
    { id: 'XVI', name: 'Spatium Iurisdictio', desc: 'Spatial jurisdiction' },
    { id: 'XVII', name: 'Humanitas Transformata', desc: 'Humanity 2.0' },
    { id: 'XVIII', name: 'Reserved', desc: 'Future axiom' },
    { id: 'XIX', name: 'Reserved', desc: 'Future axiom' },
  ]

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-900 via-black to-gray-900">
      {/* Header */}
      <header className="border-b border-cyan-500/20 bg-black/50 backdrop-blur-sm sticky top-0 z-50">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <Link href="/" className="text-2xl font-bold bg-gradient-to-r from-cyan-400 to-blue-400 bg-clip-text text-transparent">
            LAIRM
          </Link>
          <nav className="flex gap-6">
            <Link href="/manifesto" className="text-cyan-400 hover:text-cyan-300">Manifesto</Link>
            <Link href="/platform" className="text-gray-400 hover:text-white">Platform</Link>
          </nav>
        </div>
      </header>

      <main className="container mx-auto px-4 py-12">
        {/* Hero Section */}
        <div className="text-center mb-16">
          <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-cyan-400 to-blue-400 bg-clip-text text-transparent">
            The Manifesto
          </h1>
          <p className="text-xl text-gray-400 max-w-3xl mx-auto">
            19 Fundamental Axioms • 361 Executable Articles • 28 Comprehensive Chapters
          </p>
        </div>

        {/* Search Bar */}
        <div className="max-w-2xl mx-auto mb-12">
          <input
            type="search"
            placeholder="Search axioms, articles, or chapters..."
            className="w-full px-6 py-4 bg-gray-800/50 border border-cyan-500/30 rounded-lg text-white placeholder-gray-500 focus:outline-none focus:border-cyan-500"
          />
        </div>

        {/* Axioms Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mb-16">
          {axioms.map((axiom) => (
            <Link
              key={axiom.id}
              href={`/manifesto/axiom-${axiom.id.toLowerCase()}`}
              className="group p-6 bg-gray-800/30 border border-cyan-500/20 rounded-lg hover:border-cyan-500/50 hover:bg-gray-800/50 transition"
            >
              <div className="flex items-start gap-4">
                <div className="text-3xl font-bold text-cyan-400">Ψ-{axiom.id}</div>
                <div className="flex-1">
                  <h3 className="text-lg font-semibold text-white mb-2 group-hover:text-cyan-400 transition">
                    {axiom.name}
                  </h3>
                  <p className="text-sm text-gray-400">{axiom.desc}</p>
                  <div className="mt-3 text-xs text-cyan-500">
                    19 Articles →
                  </div>
                </div>
              </div>
            </Link>
          ))}
        </div>

        {/* Quick Links */}
        <div className="grid md:grid-cols-3 gap-6">
          <div className="p-6 bg-gradient-to-br from-cyan-900/20 to-blue-900/20 border border-cyan-500/30 rounded-lg">
            <h3 className="text-xl font-bold text-cyan-400 mb-2">📚 Reference Compendium</h3>
            <p className="text-gray-400 text-sm mb-4">28 chapters covering foundations, dimensions, paradigms, and prospective</p>
            <Link href="/manifesto/compendium" className="text-cyan-500 hover:text-cyan-400 text-sm">
              Explore →
            </Link>
          </div>

          <div className="p-6 bg-gradient-to-br from-purple-900/20 to-pink-900/20 border border-purple-500/30 rounded-lg">
            <h3 className="text-xl font-bold text-purple-400 mb-2">📹 Video Library</h3>
            <p className="text-gray-400 text-sm mb-4">Watch explanatory videos for each article and axiom</p>
            <Link href="/manifesto/videos" className="text-purple-500 hover:text-purple-400 text-sm">
              Watch →
            </Link>
          </div>

          <div className="p-6 bg-gradient-to-br from-blue-900/20 to-indigo-900/20 border border-blue-500/30 rounded-lg">
            <h3 className="text-xl font-bold text-blue-400 mb-2">📥 Download</h3>
            <p className="text-gray-400 text-sm mb-4">Get the complete LAIRM corpus in PDF or ePub format</p>
            <Link href="/manifesto/download" className="text-blue-500 hover:text-blue-400 text-sm">
              Download →
            </Link>
          </div>
        </div>
      </main>
    </div>
  )
}