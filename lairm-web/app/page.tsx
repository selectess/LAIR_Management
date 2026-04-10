import Image from 'next/image'
import Link from 'next/link'

export default function Home() {
  return (
    <main className="min-h-screen bg-black relative overflow-hidden">
      {/* Cybernetic Grid Background */}
      <div className="absolute inset-0 bg-[linear-gradient(to_right,#1a1a1a_1px,transparent_1px),linear-gradient(to_bottom,#1a1a1a_1px,transparent_1px)] bg-[size:4rem_4rem] [mask-image:radial-gradient(ellipse_80%_50%_at_50%_0%,#000_70%,transparent_110%)]" />
      
      {/* Animated Particles */}
      <div className="absolute inset-0">
        {[...Array(20)].map((_, i) => (
          <div
            key={i}
            className="absolute w-1 h-1 bg-cyan-500 rounded-full animate-pulse"
            style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
              animationDelay: `${Math.random() * 3}s`,
              animationDuration: `${2 + Math.random() * 3}s`
            }}
          />
        ))}
      </div>

      {/* Content */}
      <div className="relative z-10 flex flex-col items-center justify-center min-h-screen px-4">
        {/* Hero Image with Glow Effect */}
        <div className="relative mb-12 group">
          <div className="absolute -inset-4 bg-gradient-to-r from-cyan-500 via-blue-500 to-purple-500 rounded-lg blur-2xl opacity-30 group-hover:opacity-50 transition duration-1000" />
          <Image
            src="/ImFro.jpeg"
            alt="LAIRM - The Cybernetic Criterion"
            width={800}
            height={400}
            className="relative rounded-lg shadow-2xl border border-cyan-500/20"
            priority
          />
        </div>

        {/* Title */}
        <h1 className="text-5xl md:text-7xl font-bold text-center mb-4 bg-gradient-to-r from-cyan-400 via-blue-400 to-purple-400 bg-clip-text text-transparent animate-pulse">
          LAIRM
        </h1>
        <p className="text-xl md:text-2xl text-cyan-300 text-center mb-2">
          The Cybernetic Criterion
        </p>
        <p className="text-sm md:text-base text-gray-400 text-center mb-12 max-w-2xl">
          Legislature for Autonomous Intelligent Resources Management
          <br />
          <span className="text-cyan-500">Global Agentive Constitution 2026–2036</span>
        </p>

        {/* Stats */}
        <div className="grid grid-cols-3 gap-8 mb-16 text-center">
          <div className="group cursor-pointer">
            <div className="text-4xl font-bold text-cyan-400 group-hover:scale-110 transition">19</div>
            <div className="text-sm text-gray-400">Axioms</div>
          </div>
          <div className="group cursor-pointer">
            <div className="text-4xl font-bold text-blue-400 group-hover:scale-110 transition">361</div>
            <div className="text-sm text-gray-400">Articles</div>
          </div>
          <div className="group cursor-pointer">
            <div className="text-4xl font-bold text-purple-400 group-hover:scale-110 transition">28</div>
            <div className="text-sm text-gray-400">Chapters</div>
          </div>
        </div>

        {/* CTA Buttons */}
        <div className="flex flex-col md:flex-row gap-6">
          {/* Button 1: Le Manifeste */}
          <Link
            href="/manifesto"
            className="group relative px-8 py-4 bg-gradient-to-r from-cyan-600 to-blue-600 rounded-lg font-semibold text-white overflow-hidden transition-all hover:scale-105 hover:shadow-[0_0_30px_rgba(6,182,212,0.5)]"
          >
            <div className="absolute inset-0 bg-gradient-to-r from-cyan-400 to-blue-400 opacity-0 group-hover:opacity-20 transition" />
            <span className="relative flex items-center gap-2">
              📖 Le Manifeste
              <svg className="w-5 h-5 group-hover:translate-x-1 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
              </svg>
            </span>
          </Link>

          {/* Button 2: Cybernetic Criterion Platform */}
          <Link
            href="/platform"
            className="group relative px-8 py-4 bg-gradient-to-r from-purple-600 to-pink-600 rounded-lg font-semibold text-white overflow-hidden transition-all hover:scale-105 hover:shadow-[0_0_30px_rgba(168,85,247,0.5)]"
          >
            <div className="absolute inset-0 bg-gradient-to-r from-purple-400 to-pink-400 opacity-0 group-hover:opacity-20 transition" />
            <span className="relative flex items-center gap-2">
              🌐 Cybernetic Criterion Platform
              <svg className="w-5 h-5 group-hover:translate-x-1 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
              </svg>
            </span>
          </Link>
        </div>

        {/* Footer Info */}
        <div className="mt-16 text-center text-gray-500 text-sm">
          <p>127 million autonomous agents • Zero legal framework</p>
          <p className="mt-2">The first international agentive constitution</p>
        </div>
      </div>
    </main>
  )
}