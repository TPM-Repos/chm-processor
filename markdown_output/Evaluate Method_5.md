Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Evaluate Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskReleaseCondition Class](topic6647.md) : Evaluate Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationContext_
    The active execution context.

Glossary Item Box

When overridden by a derived class, evaluates the condition. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected MustOverride Function Evaluate( _
       ByVal _specificationContext_ As [SpecificationContext](topic11149.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskReleaseCondition](topic6647.md)
    Dim specificationContext As [SpecificationContext](topic11149.md)
    Dim value As Boolean
     
    value = instance.Evaluate(specificationContext)  
  
C#|   
---|---  
      
    
    protected abstract bool Evaluate( 
       [SpecificationContext](topic11149.md) _specificationContext_
    )  
  
#### Parameters

 _specificationContext_
    The active execution context.

#### Return Value

True if the condition passes, otherwise false.

# Remarks

Returning False from this method in a derived class will prevent the [ComponentTask](topic6407.md) from being released.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskReleaseCondition Class](topic6647.md)   
[ComponentTaskReleaseCondition Members](topic6648.md)


