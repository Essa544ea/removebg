# AI Background Remover & Resizer Web App

A web application that removes backgrounds from images and resizes them to a standard size, using the ClipDrop API.

## Features

- Drag and drop interface for easy image upload
- Background removal using AI
- Automatic image resizing and centering
- Modern, responsive UI
- Real-time image preview
- Progress indication during processing

## Local Development

1. Install Python 3.8 or higher
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add your ClipDrop API key:
   ```
   CLIPDROP_API_KEY=your_api_key_here
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your browser and navigate to `http://localhost:5000`

## Deployment

### GitHub Setup

1. Create a new repository on GitHub
2. Initialize git and push your code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin your-repository-url
   git push -u origin main
   ```

### Vercel Deployment

1. Create a Vercel account if you don't have one
2. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```
3. Login to Vercel:
   ```bash
   vercel login
   ```
4. Deploy the application:
   ```bash
   vercel
   ```
5. Add your environment variables in the Vercel dashboard:
   - Go to your project settings
   - Navigate to the "Environment Variables" section
   - Add `CLIPDROP_API_KEY` with your API key

## Usage

1. Drag and drop an image onto the upload area or click "Browse Files" to select an image
2. Wait for the processing to complete
3. The processed image will be automatically downloaded

## Supported Image Formats

- PNG
- JPG/JPEG

## Note

The application uses the ClipDrop API for background removal. Make sure you have a valid API key and sufficient credits for the API service.

## License

MIT License - feel free to use this project for your own purposes. 