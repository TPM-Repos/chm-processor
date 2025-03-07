Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetSpecificationDocuments Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) : GetSpecificationDocuments Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationId_
    The numerical identifier of the specification for which to get documents.

Glossary Item Box

Gets a specification's documents. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetSpecificationDocuments( _
       ByVal _specificationId_ As Integer _
    ) As IEnumerable(Of SpecificationDocumentDetails)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim specificationId As Integer
    Dim value As IEnumerable(Of SpecificationDocumentDetails)
     
    value = instance.GetSpecificationDocuments(specificationId)  
  
C#|   
---|---  
      
    
    public IEnumerable<SpecificationDocumentDetails> GetSpecificationDocuments( 
       int _specificationId_
    )  
  
#### Parameters

 _specificationId_
    The numerical identifier of the specification for which to get documents.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)


