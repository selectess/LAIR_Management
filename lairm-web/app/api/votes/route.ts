import { NextRequest, NextResponse } from 'next/server'
import { createClient } from '@/lib/supabase/server'

export async function GET(request: NextRequest) {
  const supabase = await createClient()
  const searchParams = request.nextUrl.searchParams
  const axiom_id = searchParams.get('axiom_id')
  
  let query = supabase.from('votes').select('*')
  if (axiom_id) query = query.eq('axiom_id', axiom_id)
  
  const { data, error } = await query.order('created_at', { ascending: false })
  
  if (error) return NextResponse.json({ error: error.message }, { status: 500 })
  return NextResponse.json({ data })
}

export async function POST(request: NextRequest) {
  const supabase = await createClient()
  const body = await request.json()
  
  // Validate message length
  if (body.message.length > 150) {
    return NextResponse.json(
      { error: 'Message must be 150 characters or less' },
      { status: 400 }
    )
  }
  
  const { data, error } = await supabase
    .from('votes')
    .insert({
      user_identifier: body.user_identifier,
      message: body.message,
      axiom_id: body.axiom_id,
      article_id: body.article_id,
      vote_type: body.vote_type,
    })
    .select()
    .single()
  
  if (error) return NextResponse.json({ error: error.message }, { status: 500 })
  return NextResponse.json({ data }, { status: 201 })
}