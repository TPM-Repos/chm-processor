TryUpdateSpecificationDocumentDirectory Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) : TryUpdateSpecificationDocumentDirectory Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationId_
    The identification of the specification containing the document.

_documentId_
    The identification of the specification document to update.

_newPath_
    The new specification directory.

Glossary Item Box

Attempts to update a specification document location. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryUpdateSpecificationDocumentDirectory( _
       ByVal _specificationId_ As Integer, _
       ByVal _documentId_ As Guid, _
       ByVal _newPath_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim specificationId As Integer
    Dim documentId As Guid
    Dim newPath As String
    Dim value As Boolean
     
    value = instance.TryUpdateSpecificationDocumentDirectory(specificationId, documentId, newPath)  
  
C#|   
---|---  
      
    
    public bool TryUpdateSpecificationDocumentDirectory( 
       int _specificationId_ ,
       Guid _documentId_ ,
       string _newPath_
    )  
  
#### Parameters

 _specificationId_
    The identification of the specification containing the document.
_documentId_
    The identification of the specification document to update.
_newPath_
    The new specification directory.

#### Return Value

True if the specification directory was successfully updated.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)


