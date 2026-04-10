import Link from 'next/link'
import { createClient } from '@/lib/supabase/server'

export default async function AdminPage() {
  const supabase = await createClient()
  
  // Get counts
  const { count: articlesCount } = await supabase.from('articles').select('*', { count: 'exact', head: true })
  const { count: videosCount } = await supabase.from('videos').select('*', { count: 'exact', head: true })
  const { count: aiCount } = await supabase.from('ai_directory').select('*', { count: 'exact', head: true })
  const { count: topicsCount } = await supabase.from('topics').select('*', { count: 'exact', head: true })
  const { count: votesCount } = await supabase.from('votes').select('*', { count: 'exact', head: true })
  const { count: waitlistCount } = await supabase.from('waitlist').select('*', { count: 'exact', head: true })

  return (
    <div className="min-h-screen bg-gray-900">
      {/* Header */}
      <header className="bg-black border-b border-gray-800">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <h1 className="text-2xl font-bold text-white">LAIRM Admin</h1>
          <Link href="/" className="text-gray-400 hover:text-white">
            ← Back to Site
          </Link>
        </div>
      </header>

      <main className="container mx-auto px-4 py-8">
        {/* Stats Overview */}
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4 mb-8">
          <div className="bg-gray-800 p-4 rounded-lg">
            <div className="text-3xl font-bold text-blue-400">{articlesCount || 0}</div>
            <div className="text-sm text-gray-400">Articles</div>
          </div>
          <div className="bg-gray-800 p-4 rounded-lg">
            <div className="text-3xl font-bold text-purple-400">{videosCount || 0}</div>
            <div className="text-sm text-gray-400">Videos</div>
          </div>
          <div className="bg-gray-800 p-4 rounded-lg">
            <div className="text-3xl font-bold text-cyan-400">{aiCount || 0}</div>
            <div className="text-sm text-gray-400">AI Directory</div>
          </div>
          <div className="bg-gray-800 p-4 rounded-lg">
            <div className="text-3xl font-bold text-green-400">{topicsCount || 0}</div>
            <div className="text-sm text-gray-400">Topics</div>
          </div>
          <div className="bg-gray-800 p-4 rounded-lg">
            <div className="text-3xl font-bold text-yellow-400">{votesCount || 0}</div>
            <div className="text-sm text-gray-400">Votes</div>
          </div>
          <div className="bg-gray-800 p-4 rounded-lg">
            <div className="text-3xl font-bold text-pink-400">{waitlistCount || 0}</div>
            <div className="text-sm text-gray-400">Waitlist</div>
          </div>
        </div>

        {/* Management Sections */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {/* Articles Management */}
          <Link
            href="/admin/articles"
            className="group p-6 bg-gray-800 hover:bg-gray-750 border border-gray-700 hover:border-blue-500 rounded-lg transition"
          >
            <div className="flex items-center gap-4 mb-4">
              <div className="text-3xl">📝</div>
              <h2 className="text-xl font-bold text-white">Articles</h2>
            </div>
            <p className="text-gray-400 text-sm mb-4">
              Create, edit, and manage blog articles
            </p>
            <div className="text-blue-400 text-sm">Manage →</div>
          </Link>

          {/* Videos Management */}
          <Link
            href="/admin/videos"
            className="group p-6 bg-gray-800 hover:bg-gray-750 border border-gray-700 hover:border-purple-500 rounded-lg transition"
          >
            <div className="flex items-center gap-4 mb-4">
              <div className="text-3xl">🎥</div>
              <h2 className="text-xl font-bold text-white">Videos</h2>
            </div>
            <p className="text-gray-400 text-sm mb-4">
              Add and manage YouTube videos
            </p>
            <div className="text-purple-400 text-sm">Manage →</div>
          </Link>

          {/* AI Directory Management */}
          <Link
            href="/admin/directory"
            className="group p-6 bg-gray-800 hover:bg-gray-750 border border-gray-700 hover:border-cyan-500 rounded-lg transition"
          >
            <div className="flex items-center gap-4 mb-4">
              <div className="text-3xl">🤖</div>
              <h2 className="text-xl font-bold text-white">AI Directory</h2>
            </div>
            <p className="text-gray-400 text-sm mb-4">
              Manage agents, models, and tools
            </p>
            <div className="text-cyan-400 text-sm">Manage →</div>
          </Link>

          {/* Topics Management */}
          <Link
            href="/admin/topics"
            className="group p-6 bg-gray-800 hover:bg-gray-750 border border-gray-700 hover:border-green-500 rounded-lg transition"
          >
            <div className="flex items-center gap-4 mb-4">
              <div className="text-3xl">💬</div>
              <h2 className="text-xl font-bold text-white">Topics</h2>
            </div>
            <p className="text-gray-400 text-sm mb-4">
              Moderate forum discussions
            </p>
            <div className="text-green-400 text-sm">Manage →</div>
          </Link>

          {/* Votes Management */}
          <Link
            href="/admin/votes"
            className="group p-6 bg-gray-800 hover:bg-gray-750 border border-gray-700 hover:border-yellow-500 rounded-lg transition"
          >
            <div className="flex items-center gap-4 mb-4">
              <div className="text-3xl">🗳️</div>
              <h2 className="text-xl font-bold text-white">Votes</h2>
            </div>
            <p className="text-gray-400 text-sm mb-4">
              View and analyze community votes
            </p>
            <div className="text-yellow-400 text-sm">View →</div>
          </Link>

          {/* Waitlist Management */}
          <Link
            href="/admin/waitlist"
            className="group p-6 bg-gray-800 hover:bg-gray-750 border border-gray-700 hover:border-pink-500 rounded-lg transition"
          >
            <div className="flex items-center gap-4 mb-4">
              <div className="text-3xl">📋</div>
              <h2 className="text-xl font-bold text-white">Waitlist</h2>
            </div>
            <p className="text-gray-400 text-sm mb-4">
              Review and approve contributors
            </p>
            <div className="text-pink-400 text-sm">Review →</div>
          </Link>
        </div>

        {/* API Access */}
        <div className="mt-8 p-6 bg-gradient-to-r from-indigo-900/30 to-purple-900/30 border border-indigo-500/30 rounded-lg">
          <h3 className="text-xl font-bold text-white mb-3">🔑 API Access</h3>
          <p className="text-gray-400 mb-4">
            Secure REST API for remote content management
          </p>
          <Link
            href="/admin/api"
            className="inline-block px-6 py-2 bg-indigo-600 hover:bg-indigo-700 rounded-lg text-white text-sm transition"
          >
            View API Docs →
          </Link>
        </div>
      </main>
    </div>
  )
}