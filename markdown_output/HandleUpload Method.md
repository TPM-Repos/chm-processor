![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
HandleUpload Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9213.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [TinyMCEControl Class](topic9204.md) : HandleUpload Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_imageData_
    A byte array containing the image information.

_uploadingFileName_
    The name of the image being uploaded.

Glossary Item Box

Takes the specified inputs and completes the upload process for this control asynchronously. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub HandleUpload( _
       ByVal _imageData_() As Byte, _
       ByVal _uploadingFileName_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [TinyMCEControl](topic9204.md)
    Dim imageData() As Byte
    Dim uploadingFileName As String
     
    instance.HandleUpload(imageData, uploadingFileName)  
  
C#|   
---|---  
      
    
    public void HandleUpload( 
       byte[] _imageData_ ,
       string _uploadingFileName_
    )  
  
#### Parameters

 _imageData_
    A byte array containing the image information.
_uploadingFileName_
    The name of the image being uploaded.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[TinyMCEControl Class](topic9204.md)   
[TinyMCEControl Members](topic9205.md)

©2024 DriveWorks Ltd. All Rights Reserved.
