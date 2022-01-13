//creates an one line drawing based on a given image. Has two modes: Mode one always looks for the nearest neighbor and connects this two points. Mode two looks up for the 7 nearest neighbors and chooses one of these randomly. Last one makes it look more like a natural drawing.
//particle number determeines resolution
//connection mode dterines if show connections more(0) or less (1) due to nearest neighbor choice
//mode determines straight (1) or curly (0)

final String inputPath = "prepped_input.jpg";
int particelNum = 80000, speed = 800;

PImage img;         // Source image
PImage destination; // Destination image
PImage input, over;
ArrayList <PVector> pc;
ArrayList <Line> lines;

int mode = 0, connectionMode = 1;

void setup ()
{ 
  size(600,600);
  
  //STEP ONE: first prepp image by converting to bw outline which is pixelated
  img = loadImage("input.jpg");
  img.resize(600, 600);
  destination = createImage(img.width, img.height, RGB);
  
  // We are going to look at both image's pixels
  img.loadPixels();
  destination.loadPixels();
  
  // Since we are looking at left neighbors
  // We skip the first column
  for (int x = 1; x < width; x++ ) {
    for (int y = 0; y < height; y++ ) {
      
      // Pixel location and color
      int loc = x + y*img.width;
      color pix = img.pixels[loc];
      
      // Pixel to the left location and color
      int leftLoc = (x - 1) + y*img.width;
      color leftPix = img.pixels[leftLoc];
      
      // New color is difference between pixel and left neighbor
      float diff = abs(brightness(pix) - brightness(leftPix));
      destination.pixels[loc] = color(diff); 
    }
  }
  
  // We changed the pixels in destination
  destination.updatePixels();
  // Display the destination
  image(destination,0,0);
  // invert from black to white
  filter(INVERT);
  filter(THRESHOLD,0.98);
  saveFrame("prepped_input.jpg");
  
  
  //STEP TWO: use bw outline as input for line drawing
  smooth();
  frameRate (25);

  input = loadImage (inputPath);
  if (input.width != width || input.height != height) input.resize (width, height);

  initPointCloud();

  over = createImage (1, 1, RGB);
  for (int i = 0; i < over.pixels.length; i++) over.pixels [i] = color (245);
  over.updatePixels();
}

void draw ()
{
  background (245);

  strokeWeight (0.5);
  noFill();
  stroke (0);
  PVector pos;
  for (int i = 0; i < pc.size(); i++) 
  {
    pos = pc.get (i);
    point (pos.x, pos.y);
  }

  strokeWeight (1);
  stroke (0);
  for (int i = 0; i < lines.size(); i++) 
  {
    lines.get (i).strokeSytle();
    if (mode == 1) lines.get (i).draw();
    if (mode == 0) lines.get (i).drawSmooth ();
  }

  if (pc.size() > 0)
  {
    fill (245);
    noStroke();
    String txt = "Processing";
    if (frameCount % 3 == 0) txt+=".  ";
    else if (frameCount %3 == 1) txt+=".. ";
    else txt+="...";
    txt+=" [" + nf ((float) (particelNum-pc.size()) / (float) particelNum * 100.0, 0, 2) + "%]";
    text (txt, 20, height-15 );
  }

  for (int i = 0; i < speed; i++) creatConnection(connectionMode);
  blend (over, 0, 0, width, height, 0, 0, width, height, MULTIPLY);
  
  
}

void keyPressed()
{
  saveFrame("output.png");
}


void initPointCloud()
{
  pc = new ArrayList ();
  lines = new ArrayList();

  PVector [] targets = findTargets (particelNum, input);
  for (int i = 0; i < targets.length; i++) pc.add (targets [i]);
}

void creatConnection (int cMode)
{
  if (lines.size() == 0 && pc.size() > 2)
  {
    PVector start, end;
    int startindex = (int) random (pc.size());
    start = pc.get (startindex);
    pc.remove (startindex);
    int endindex = getClosestIndex (start, pc);
    end = pc.get (endindex);
    pc.remove (endindex);
    lines.add (new Line (start, end));
    lines.get (lines.size()-1).setStrokeWeightAndColor(input.pixels, input.width, input.height);
  }
  else {
    if (pc.size() > 0)
    {
      PVector start = lines.get (lines.size()-1).end, end;
      int index = cMode == 0 ? getClosestIndex (start, 7, pc) : getClosestIndex (start, pc);
      end = pc.get (index);
      pc.remove (index);
      lines.add (new Line (start, end));
      lines.get (lines.size()-1).setStrokeWeightAndColor(input.pixels, input.width, input.height);
    }
  }
}

int getClosestIndex (PVector start, ArrayList <PVector> lookup)
{
  float closestDist = width*height;
  int closestIndex = 0;

  float dis = 0;
  for (int i = 0; i < lookup.size(); i++)
  {
    dis = PVector.dist (start, lookup.get(i));
    if (dis < closestDist)
    {
      closestDist = dis;
      closestIndex = i;
    }
  }
  return closestIndex;
}

int getClosestIndex (PVector start, int n, ArrayList <PVector> lookup)
{
  float [] closestDist = new float [n];
  int [] closestIndex = new int [n];

  for (int i = 0; i < n; i++) 
  {
    closestDist [i] = width*height;
    closestIndex [i] = 0;
  }

  float dis = 0;
  float disMin = width*height, disMax = disMin*2;

  for (int i = 0; i < lookup.size(); i++)
  {
    dis = PVector.dist (start, lookup.get(i));
    if (dis < disMin )
    {
      disMin = dis;
      closestDist[0] = dis;
      closestIndex [0] = i;
    }
    else if (dis > disMin && dis < disMax)
    {
      int index = i;
      for (int j = 0; j < n-1; j++)
      {
        if (closestDist[j] < dis &&  closestDist[j+1] > dis)
        {

          index=j+1;
          break;
        }
      }

      for (int j = n-1; j > 0; j--)
      {
        if (j == index)
        {
          closestDist [j] = dis;
          closestIndex [j] = i;
          break;
        }
        else 
        {
          if (j > 0)
          {
            closestIndex [j] = closestIndex [j-1];
            closestDist[j] = closestDist [j-1];
          }
        }
      }
      disMax = closestDist[n-1];
    }
  }

  int index = closestIndex [(int) random (n)];
  return index;
}
