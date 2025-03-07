Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsRunningRequired Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) > [IncrementRevisionNumberTask Class](topic12307.md) : IsRunningRequired Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ctx_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overrides NotOverridable Function IsRunningRequired( _
       ByVal _ctx_ As [SpecificationContext](topic11149.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IncrementRevisionNumberTask](topic12307.md)
    Dim ctx As [SpecificationContext](topic11149.md)
    Dim value As Boolean
     
    value = instance.IsRunningRequired(ctx)  
  
C#|   
---|---  
      
    
    protected override bool IsRunningRequired( 
       [SpecificationContext](topic11149.md) _ctx_
    )  
  
#### Parameters

 _ctx_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IncrementRevisionNumberTask Class](topic12307.md)   
[IncrementRevisionNumberTask Members](topic12308.md)


