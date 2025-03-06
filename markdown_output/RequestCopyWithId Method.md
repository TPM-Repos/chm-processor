       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RequestCopyWithId Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) > [ICopySpecificationHostService Interface](topic11898.md) : RequestCopyWithId Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ctx_
    A specification context for the specification to copy.

Glossary Item Box

Requests that the host copies the specification represented by the given context. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function RequestCopyWithId( _
       ByVal _ctx_ As [SpecificationContext](topic11149.md) _
    ) As Integer  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICopySpecificationHostService](topic11898.md)
    Dim ctx As [SpecificationContext](topic11149.md)
    Dim value As Integer
     
    value = instance.RequestCopyWithId(ctx)  
  
C#|   
---|---  
      
    
    int RequestCopyWithId( 
       [SpecificationContext](topic11149.md) _ctx_
    )  
  
#### Parameters

 _ctx_
    A specification context for the specification to copy.

#### Return Value

The id of the created specification.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICopySpecificationHostService Interface](topic11898.md)   
[ICopySpecificationHostService Members](topic11899.md)


