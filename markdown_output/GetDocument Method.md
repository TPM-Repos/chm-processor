![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetDocument Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4443.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocuments Class](topic4434.md) : GetDocument Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the document to get.

Glossary Item Box

Gets the document with the specified name. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetDocument( _
       ByVal _name_ As String _
    ) As [ProjectDocument](topic4356.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocuments](topic4434.md)
    Dim name As String
    Dim value As [ProjectDocument](topic4356.md)
     
    value = instance.GetDocument(name)  
  
C#|   
---|---  
      
    
    public [ProjectDocument](topic4356.md) GetDocument( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the document to get.

#### Return Value

The document with the specified name.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
[ItemNotFoundException](topic3571.md)| Thrown if a document with the specified name does not exist.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectDocuments Class](topic4434.md)   
[ProjectDocuments Members](topic4435.md)

©2024 DriveWorks Ltd. All Rights Reserved.
