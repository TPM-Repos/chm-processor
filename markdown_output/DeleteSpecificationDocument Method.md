Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteSpecificationDocument Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) : DeleteSpecificationDocument Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_documentId_
    The document to delete.

Glossary Item Box

Deletes the specification document with the specified identifier. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function DeleteSpecificationDocument( _
       ByVal _documentId_ As Guid _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim documentId As Guid
    Dim value As Boolean
     
    value = instance.DeleteSpecificationDocument(documentId)  
  
C#|   
---|---  
      
    
    public bool DeleteSpecificationDocument( 
       Guid _documentId_
    )  
  
#### Parameters

 _documentId_
    The document to delete.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)


