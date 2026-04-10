import { NextRequest, NextResponse } from 'next/server'
import { createClient } from '@/lib/supabase/server'

// GET /api/articles - List articles
export async function GET(request: NextRequest) {
  const supabase = await createClient()
  const searchParams = request.nextUrl.searchParams
  
  const status = searchParams.get('status')
  const category = searchParams.get('category')
  const limit = parseInt(searchParams.get('limit') || '50')
  
  let query = supabase.from('articles').select('*')
  
  if (status) query = query.eq('status', status)
  if (category) query = query.eq('category', category)
  
  const { data, error } = await query
    .order('created_at', { ascending: false })
    .limit(limit)
  
  if (error) {
    return NextResponse.json({ error: error.message }, { status: 500 })
  }
  
  return NextResponse.json({ data })
}

// POST /api/articles - Create article
export async function POST(request: NextRequest) {
  const supabase = await createClient()
  const body = await request.json()
  
  const { data, error } = await supabase
    .from('articles')
    .insert({
      title: body.title,
      slug: body.slug || body.title.toLowerCase().replace(/\s+/g, '-'),
      content: body.content,
      excerpt: body.excerpt,
      status: body.status || 'draft',
      category: body.category,
      tags: body.tags,
      featured_image: body.featured_image,
      video_url: body.video_url,
    })
    .select()
    .single()
  
  if (error) {
    return NextResponse.json({ error: error.message }, { status: 500 })
  }
  
  return NextResponse.json({ data }, { status: 201 })
}