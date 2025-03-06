![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InvalidDocumentPathException Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3537.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [InvalidDocumentPathException Class](topic3531.md) : InvalidDocumentPathException Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_documentName_
    The name of the document that threw this exception.

_invalidPathFragment_
    The part of the document path that is invalid.

Glossary Item Box

Creates a new instance of the [InvalidDocumentPathException](topic3531.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _documentName_ As String, _
       ByVal _invalidPathFragment_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim documentName As String
    Dim invalidPathFragment As String
     
    Dim instance As New [InvalidDocumentPathException](topic3531.md)(documentName, invalidPathFragment)  
  
C#|   
---|---  
      
    
    public InvalidDocumentPathException( 
       string _documentName_ ,
       string _invalidPathFragment_
    )  
  
#### Parameters

 _documentName_
    The name of the document that threw this exception.
_invalidPathFragment_
    The part of the document path that is invalid.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[InvalidDocumentPathException Class](topic3531.md)   
[InvalidDocumentPathException Members](topic3532.md)

©2024 DriveWorks Ltd. All Rights Reserved.
