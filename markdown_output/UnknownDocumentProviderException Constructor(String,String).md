![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UnknownDocumentProviderException Constructor(String,String)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5780.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [UnknownDocumentProviderException Class](topic5772.md) > [UnknownDocumentProviderException Constructor](topic5778.md) : UnknownDocumentProviderException Constructor(String,String)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_documentName_
    The name of the document.

_documentType_
    The type of the document.

Glossary Item Box

Creates a new instance of the [UnknownDocumentProviderException](topic5772.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _documentName_ As String, _
       ByVal _documentType_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim documentName As String
    Dim documentType As String
     
    Dim instance As New [UnknownDocumentProviderException](topic5772.md)(documentName, documentType)  
  
C#|   
---|---  
      
    
    public UnknownDocumentProviderException( 
       string _documentName_ ,
       string _documentType_
    )  
  
#### Parameters

 _documentName_
    The name of the document.
_documentType_
    The type of the document.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[UnknownDocumentProviderException Class](topic5772.md)   
[UnknownDocumentProviderException Members](topic5773.md)   
[Overload List](topic5778.md)

©2024 DriveWorks Ltd. All Rights Reserved.
