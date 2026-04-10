import Link from 'next/link'
import { createClient } from '@/lib/supabase/server'

export default async function ArticlesAdminPage() {
  const supabase = await createClient()
  
  const { data: articles } = await supabase
    .from('articles')
    .select('*')
    .order('created_at', { ascending: false })
    .limit(50)

  return (
    <div className="min-h-screen bg-gray-900">
      <header className="bg-black border-b border-gray-800">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center gap-4">
            <Link href="/admin" className="text-gray-400 hover:text-white">
              ← Admin
            </Link>
            <h1 className="text-2xl font-bold text-white">Articles Management</h1>
          </div>
          <Link
            href="/admin/articles/new"
            className="px-4 py-2 bg-blue-600 hover:bg-blue-700 rounded-lg text-white text-sm transition"
          >
            + New Article
          </Link>
        </div>
      </header>

      <main className="container mx-auto px-4 py-8">
        {/* Filters */}
        <div className="flex gap-4 mb-6">
          <select className="px-4 py-2 bg-gray-800 border border-gray-700 rounded-lg text-white">
            <option>All Status</option>
            <option>Published</option>
            <option>Draft</option>
            <option>Archived</option>
          </select>
          <select className="px-4 py-2 bg-gray-800 border border-gray-700 rounded-lg text-white">
            <option>All Categories</option>
            <option>Legislation</option>
            <option>Technology</option>
            <option>Ethics</option>
            <option>Economics</option>
          </select>
          <input
            type="search"
            placeholder="Search articles..."
            className="flex-1 px-4 py-2 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-500"
          />
        </div>

        {/* Articles Table */}
        <div className="bg-gray-800 rounded-lg overflow-hidden">
          <table className="w-full">
            <thead className="bg-gray-900">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">Title</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">Status</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">Category</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">Views</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase">Date</th>
                <th className="px-6 py-3 text-right text-xs font-medium text-gray-400 uppercase">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-700">
              {articles?.map((article) => (
                <tr key={article.id} className="hover:bg-gray-750">
                  <td className="px-6 py-4">
                    <div className="text-white font-medium">{article.title}</div>
                    <div className="text-sm text-gray-400">{article.slug}</div>
                  </td>
                  <td className="px-6 py-4">
                    <span className={`px-2 py-1 text-xs rounded-full ${
                      article.status === 'published' ? 'bg-green-900/30 text-green-400' :
                      article.status === 'draft' ? 'bg-yellow-900/30 text-yellow-400' :
                      'bg-gray-700 text-gray-400'
                    }`}>
                      {article.status}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-gray-300">{article.category || '-'}</td>
                  <td className="px-6 py-4 text-gray-300">{article.view_count}</td>
                  <td className="px-6 py-4 text-gray-400 text-sm">
                    {new Date(article.created_at).toLocaleDateString()}
                  </td>
                  <td className="px-6 py-4 text-right">
                    <Link
                      href={`/admin/articles/${article.id}`}
                      className="text-blue-400 hover:text-blue-300 text-sm mr-4"
                    >
                      Edit
                    </Link>
                    <button className="text-red-400 hover:text-red-300 text-sm">
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
              {!articles?.length && (
                <tr>
                  <td colSpan={6} className="px-6 py-12 text-center text-gray-500">
                    No articles yet. Create your first article!
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </main>
    </div>
  )
}