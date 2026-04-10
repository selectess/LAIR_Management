import Link from 'next/link'
import { createClient } from '@/lib/supabase/server'

export default async function PlatformPage() {
  const supabase = await createClient()
  
  // Get stats
  const { count: articlesCount } = await supabase.from('articles').select('*', { count: 'exact', head: true })
  const { count: aiCount } = await supabase.from('ai_directory').select('*', { count: 'exact', head: true })
  const { count: votesCount } = await supabase.from('votes').select('*', { count: 'exact', head: true })
  const { count: contributorsCount } = await supabase.from('contributors').select('*', { count: 'exact', head: true })

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-900 via-black to-gray-900">
      {/* Header */}
      <header className="border-b border-purple-500/20 bg-black/50 backdrop-blur-sm sticky top-0 z-50">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <Link href="/" className="text-2xl font-bold bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">
            LAIRM Platform
          </Link>
          <nav className="flex gap-6">
            <Link href="/manifesto" className="text-gray-400 hover:text-white">Manifesto</Link>
            <Link href="/platform" className="text-purple-400 hover:text-purple-300">Platform</Link>
          </nav>
        </div>
      </header>

      <main className="container mx-auto px-4 py-12">
        {/* Hero */}
        <div className="text-center mb-16">
          <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">
            Cybernetic Criterion Platform
          </h1>
          <p className="text-xl text-gray-400 max-w-3xl mx-auto">
            The global ecosystem for autonomous intelligence governance
          </p>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-6 mb-16">
          <div className="p-6 bg-purple-900/20 border border-purple-500/30 rounded-lg text-center">
            <div className="text-4xl font-bold text-purple-400">{articlesCount || 0}</div>
            <div className="text-sm text-gray-400 mt-2">Articles</div>
          </div>
          <div className="p-6 bg-blue-900/20 border border-blue-500/30 rounded-lg text-center">
            <div className="text-4xl font-bold text-blue-400">{aiCount || 0}</div>
            <div className="text-sm text-gray-400 mt-2">AI Agents</div>
          </div>
          <div className="p-6 bg-cyan-900/20 border border-cyan-500/30 rounded-lg text-center">
            <div className="text-4xl font-bold text-cyan-400">{votesCount || 0}</div>
            <div className="text-sm text-gray-400 mt-2">Votes</div>
          </div>
          <div className="p-6 bg-pink-900/20 border border-pink-500/30 rounded-lg text-center">
            <div className="text-4xl font-bold text-pink-400">{contributorsCount || 0}</div>
            <div className="text-sm text-gray-400 mt-2">Contributors</div>
          </div>
        </div>

        {/* Modules Grid */}
        <div className="grid md:grid-cols-2 gap-8">
          {/* Module 1: Presentation */}
          <Link
            href="/platform/about"
            className="group p-8 bg-gradient-to-br from-purple-900/30 to-pink-900/30 border border-purple-500/30 rounded-xl hover:border-purple-500/60 transition"
          >
            <div className="text-4xl mb-4">🎯</div>
            <h2 className="text-2xl font-bold text-white mb-3 group-hover:text-purple-400 transition">
              Presentation
            </h2>
            <p className="text-gray-400 mb-4">
              Vision, mission, and the global challenge of autonomous intelligence governance
            </p>
            <div className="text-purple-400 text-sm">Learn more →</div>
          </Link>

          {/* Module 2: Magazine/Blog */}
          <Link
            href="/platform/magazine"
            className="group p-8 bg-gradient-to-br from-blue-900/30 to-cyan-900/30 border border-blue-500/30 rounded-xl hover:border-blue-500/60 transition"
          >
            <div className="text-4xl mb-4">📰</div>
            <h2 className="text-2xl font-bold text-white mb-3 group-hover:text-blue-400 transition">
              Magazine & Blog
            </h2>
            <p className="text-gray-400 mb-4">
              Daily articles on legislation, technology, ethics, and economics • 5 articles/day
            </p>
            <div className="text-blue-400 text-sm">Read articles →</div>
          </Link>

          {/* Module 3: Forum */}
          <Link
            href="/platform/forum"
            className="group p-8 bg-gradient-to-br from-cyan-900/30 to-teal-900/30 border border-cyan-500/30 rounded-xl hover:border-cyan-500/60 transition"
          >
            <div className="text-4xl mb-4">💬</div>
            <h2 className="text-2xl font-bold text-white mb-3 group-hover:text-cyan-400 transition">
              Community Forum
            </h2>
            <p className="text-gray-400 mb-4">
              Vote on proposals, discuss amendments, and shape the future of AI governance
            </p>
            <div className="text-cyan-400 text-sm">Join discussion →</div>
          </Link>

          {/* Module 4: Directories */}
          <Link
            href="/platform/directory"
            className="group p-8 bg-gradient-to-br from-indigo-900/30 to-purple-900/30 border border-indigo-500/30 rounded-xl hover:border-indigo-500/60 transition"
          >
            <div className="text-4xl mb-4">📚</div>
            <h2 className="text-2xl font-bold text-white mb-3 group-hover:text-indigo-400 transition">
              AI Directory
            </h2>
            <p className="text-gray-400 mb-4">
              Comprehensive catalog of 127M+ agents, models, frameworks, and contributors
            </p>
            <div className="text-indigo-400 text-sm">Explore directory →</div>
          </Link>

          {/* Module 5: Contribution Hub */}
          <Link
            href="/platform/contribute"
            className="group p-8 bg-gradient-to-br from-pink-900/30 to-rose-900/30 border border-pink-500/30 rounded-xl hover:border-pink-500/60 transition md:col-span-2"
          >
            <div className="text-4xl mb-4">🤝</div>
            <h2 className="text-2xl font-bold text-white mb-3 group-hover:text-pink-400 transition">
              Contribution Hub
            </h2>
            <p className="text-gray-400 mb-4">
              Join the editorial committee, contribute code, translate, or support financially
            </p>
            <div className="grid md:grid-cols-4 gap-4 mt-6">
              <div className="p-4 bg-black/30 rounded-lg">
                <div className="text-sm text-gray-500">Expertise</div>
                <div className="text-white font-semibold">Join Committee</div>
              </div>
              <div className="p-4 bg-black/30 rounded-lg">
                <div className="text-sm text-gray-500">Code</div>
                <div className="text-white font-semibold">GitHub</div>
              </div>
              <div className="p-4 bg-black/30 rounded-lg">
                <div className="text-sm text-gray-500">Translation</div>
                <div className="text-white font-semibold">11 Languages</div>
              </div>
              <div className="p-4 bg-black/30 rounded-lg">
                <div className="text-sm text-gray-500">Financial</div>
                <div className="text-white font-semibold">Donate</div>
              </div>
            </div>
            <div className="text-pink-400 text-sm mt-4">Start contributing →</div>
          </Link>
        </div>

        {/* Waitlist CTA */}
        <div className="mt-16 p-8 bg-gradient-to-r from-purple-900/40 to-pink-900/40 border border-purple-500/30 rounded-xl text-center">
          <h3 className="text-2xl font-bold text-white mb-3">Join the Waitlist</h3>
          <p className="text-gray-400 mb-6">Be among the first to access the full platform features</p>
          <Link
            href="/platform/waitlist"
            className="inline-block px-8 py-3 bg-gradient-to-r from-purple-600 to-pink-600 rounded-lg font-semibold text-white hover:scale-105 transition"
          >
            Join Waitlist →
          </Link>
        </div>
      </main>
    </div>
  )
}