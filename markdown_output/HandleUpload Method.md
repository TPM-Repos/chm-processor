Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
HandleUpload Method   
  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub HandleUpload( _
       ByVal _imageData_() As Byte, _
       ByVal _uploadingFileName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TinyMCEControl Class](topic9204.md)   
[TinyMCEControl Members](topic9205.md)


