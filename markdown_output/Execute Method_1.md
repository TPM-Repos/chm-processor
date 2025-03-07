Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Execute Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Task Class](topic11629.md) : Execute Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ctx_
    The specification context for the active specification.

Glossary Item Box

When overridden by a derived class, executes the action represented by the task. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected MustOverride Sub Execute( _
       ByVal _ctx_ As [SpecificationContext](topic11149.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Task](topic11629.md)
    Dim ctx As [SpecificationContext](topic11149.md)
     
    instance.Execute(ctx)  
  
C#|   
---|---  
      
    
    protected abstract void Execute( 
       [SpecificationContext](topic11149.md) _ctx_
    )  
  
#### Parameters

 _ctx_
    The specification context for the active specification.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Task Class](topic11629.md)   
[Task Members](topic11630.md)


