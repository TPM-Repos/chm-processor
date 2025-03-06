![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

_TDocument_
    The type of the document to add.

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateDocument<TDocument>(String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4441.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocuments Class](topic4434.md) > [CreateDocument Method](topic4440.md) : CreateDocument<TDocument>(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the document to add.

Glossary Item Box

Creates and adds a new document to the project. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateDocument(Of TDocument As [ProjectDocument](topic4356.md))( _
       ByVal _name_ As String _
    ) As TDocument  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocuments](topic4434.md)
    Dim name As String
    Dim value As TDocument
     
    value = instance.CreateDocument(Of TDocument)(name)  
  
C#|   
---|---  
      
    
    public TDocument CreateDocument<TDocument>( 
       string _name_
    )
    where TDocument: [ProjectDocument](topic4356.md)  
  
#### Parameters

 _name_
    The name of the document to add.

#### Type Parameters

_TDocument_
    The type of the document to add.

#### Return Value

The newly created document.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
[ItemExistsException](topic3561.md)| A document with the given name already exists.  
System.ArgumentOutOfRangeException| The specified type does not inherit from [ProjectDocument](topic4356.md).  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectDocuments Class](topic4434.md)   
[ProjectDocuments Members](topic4435.md)   
[Overload List](topic4440.md)

©2024 DriveWorks Ltd. All Rights Reserved.
