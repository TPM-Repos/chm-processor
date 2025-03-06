![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreatePreviewImage(String,Int32,Int32,RotationZoom) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [PreviewControl Class](topic8709.md) > [CreatePreviewImage Method](topic8719.md) : CreatePreviewImage(String,Int32,Int32,RotationZoom) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_outputPath_
    Path to save the image out to.

_width_
    Pixel width of image to save out.

_height_
    Pixel height of image to save out.

_rotationZoom_
    Orientation to set the camera to.

Glossary Item Box

Generates a preview screenshot from the preview control 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub CreatePreviewImage( _
       ByVal _outputPath_ As String, _
       ByVal _width_ As Integer, _
       ByVal _height_ As Integer, _
       ByVal _rotationZoom_ As DriveWorks.Support.RotationZoom _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [PreviewControl](topic8709.md)
    Dim outputPath As String
    Dim width As Integer
    Dim height As Integer
    Dim rotationZoom As DriveWorks.Support.RotationZoom
     
    instance.CreatePreviewImage(outputPath, width, height, rotationZoom)  
  
C#|   
---|---  
      
    
    public void CreatePreviewImage( 
       string _outputPath_ ,
       int _width_ ,
       int _height_ ,
       DriveWorks.Support.RotationZoom _rotationZoom_
    )  
  
#### Parameters

 _outputPath_
    Path to save the image out to.
_width_
    Pixel width of image to save out.
_height_
    Pixel height of image to save out.
_rotationZoom_
    Orientation to set the camera to.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[PreviewControl Class](topic8709.md)   
[PreviewControl Members](topic8710.md)   
[Overload List](topic8719.md)


