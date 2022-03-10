from fastapi import APIRouter,Request
from .gms import CreateMeet


api_router = APIRouter()

# retrieve
@api_router.get("/")
async def root():
    return {"Hello" : "World"}

@api_router.get("/api/scheduleMeet")
async def get_articles(request: Request):
    info = await request.json()
    date = info['date']
    start = info['start']
    end = info['end']
    emails = info['emails']
    topic = info['topic']
    time = {
    'start': date+'T'+start+':00.000000',
    'end': date+'T'+end+':00.000000'
    }
    guests = {email: email for email in emails}
    meet = CreateMeet(guests, time, topic)
    keys = ['organizer', 'hangoutLink', 'summary', 'start', 'end', 'attendees']
    details = {key: meet.event_states[key] for key in keys}
    return details
