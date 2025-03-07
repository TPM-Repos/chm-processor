Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetDocument Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocuments Class](topic4434.md) : GetDocument Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the document to get.

Glossary Item Box

Gets the document with the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetDocument( _
       ByVal _name_ As String _
    ) As [ProjectDocument](topic4356.md)  
  
Visual Basic (Usage)| Copy Code  
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

# Exceptions

Exception| Description  
---|---  
[ItemNotFoundException](topic3571.md)| Thrown if a document with the specified name does not exist.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDocuments Class](topic4434.md)   
[ProjectDocuments Members](topic4435.md)


