const { google } = require('googleapis');

export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  const { folderId } = req.query;
  if (!folderId) {
    return res.status(400).json({ error: 'Missing folderId parameter' });
  }

  if (!process.env.GOOGLE_CLIENT_EMAIL || !process.env.GOOGLE_PRIVATE_KEY) {
    return res.status(200).json([
      { id: 'dummy1', name: 'Placeholder 1', url: 'https://placehold.co/600x600/1a1a1f/F2B33D?text=Setup+Keys' },
      { id: 'dummy2', name: 'Placeholder 2', url: 'https://placehold.co/600x600/1a1a1f/F2B33D?text=Setup+Keys' }
    ]);
  }

  try {
    const auth = new google.auth.GoogleAuth({
      credentials: {
        client_email: process.env.GOOGLE_CLIENT_EMAIL,
        private_key: process.env.GOOGLE_PRIVATE_KEY.replace(/\\n/g, '\n'),
      },
      scopes: ['https://www.googleapis.com/auth/drive.readonly'],
    });

    const drive = google.drive({ version: 'v3', auth });

    const response = await drive.files.list({
      q: `'${folderId}' in parents and mimeType contains 'image/' and trashed = false`,
      fields: 'files(id, name, mimeType)',
      pageSize: 200,
    });

    const files = response.data.files;
    
    const images = files.map(file => ({
      id: file.id,
      name: file.name,
      url: `https://drive.google.com/thumbnail?id=${file.id}&sz=w800`
    }));

    res.status(200).json(images);
  } catch (error) {
    console.error('Drive API Error:', error);
    res.status(500).json({ error: 'Failed to fetch images from Google Drive: ' + error.message });
  }
}
